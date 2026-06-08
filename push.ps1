param(
    [string]$Message = "",
    [string]$Branch = "main"
)

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Error "git is not installed or not in PATH."
    exit 1
}

if ([string]::IsNullOrWhiteSpace($Message)) {
    $timestamp = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
    $Message = "practice: update $timestamp"
}

git add -A
$commit = & git commit -m "$Message" 2>&1
if ($LASTEXITCODE -ne 0) {
    if ($commit -match "nothing to commit") {
        Write-Host "No changes to commit."
    } else {
        Write-Error $commit
        exit $LASTEXITCODE
    }
} else {
    Write-Host "Committed: $Message"
}

git push origin $Branch
if ($LASTEXITCODE -eq 0) { Write-Host "Pushed to origin/$Branch" }

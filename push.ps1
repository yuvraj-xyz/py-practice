param(
    [string]$Message = "chore: update",
    [string]$Branch = "main"
)

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Error "git is not installed or not in PATH."
    exit 1
}

git add -A
try {
    git commit -m $Message -q
} catch {
    Write-Host "No changes to commit."
}

git push origin $Branch

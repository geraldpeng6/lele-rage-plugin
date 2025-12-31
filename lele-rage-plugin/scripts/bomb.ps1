# bomb.ps1 - 乐乐炸弹音效脚本 (Windows版)
# 💥 每次 Claude Code 停止时播放音效

$soundFiles = @(
    "C:\Windows\Media\Alarm01.wav",
    "C:\Windows\Media\tada.wav",
    "C:\Windows\Media\Windows Exclamation.wav",
    "C:\Windows\Media\chord.wav",
    "C:\Windows\Media\ding.wav"
)

# 随机选择一个音效
$availableSounds = $soundFiles | Where-Object { Test-Path $_ }

if ($availableSounds.Count -gt 0) {
    $sound = $availableSounds | Get-Random
    try {
        $player = New-Object System.Media.SoundPlayer $sound
        $player.PlaySync()
    }
    catch {
        # 后备：系统蜂鸣
        [Console]::Beep(800, 300)
        [Console]::Beep(600, 300)
        [Console]::Beep(400, 500)
    }
}
else {
    # 后备：系统蜂鸣
    [Console]::Beep(800, 300)
    [Console]::Beep(600, 300)
    [Console]::Beep(400, 500)
}

# 输出完成信息
Write-Host "[BOOM] 乐乐炸弹音效完成！[RAGE]" -ForegroundColor Yellow

{
    # region General
    "settings_lists": [
        "All Settings (Please refer to docs to learn more about):\n%s",
        "Semua Pengaturan (Silakan lihat dokumen untuk mempelajari lebih lanjut tentang):\n%s"
    ],
    "cmd_err_run": [
        f"Error occurred when running command: {code('%s')}: {code('%s')}\n{code('%s')}",
        f"Terjadi kesalahan saat menjalankan perintah: {code('%s')} : {code('%s')}\n{code('%s')}",
    ],
    "no_cmd_given": [
        "Please use this command in private chat, or add parameters to execute.",
        "Silakan gunakan perintah ini di chat pribadi, atau tambahkan parameter untuk menjalankan."
    ],
    "invalid_user_id": [
        "Invalid User ID",
        "ID Pengguna Tidak Valid"
    ],
    "invalid_param": [
        "Invalid Parameter",
        "Parameter Tidak Valid"
    ],
    "enabled": [
        "Enabled",
        "Diaktifkan"
    ],
    "disabled": [
        "Disabled",
        "Dinonaktifkan"
    ],
    "none": [
        "None",
        "Tidak Ada"
    ],
    "tip_edit": [
        f"You can edit this by using {code('%s')}",
        f"Untuk mengedit, silakan gunakan {code('%s')}"
    ],
    "tip_run_in_pm": [
        "You can only run this command in private chat, or by adding parameters.",
        "Silakan jalankan perintah ini di chat pribadi, atau tambahkan parameter untuk menjalankan."
    ],
    # endregion

    # region Plugin
    "plugin_desc": [
        "Captcha for PM",
        "Plugin Verifikasi Captcha untuk Chat Pribadi"
    ],
    "check_usage": [
        "Please use %s to see available commands.",
        "Silakan gunakan %s untuk melihat perintah yang tersedia."
    ],
    "curr_version": [
        f"Current {code('PMCaptcha')} Version: %s",
        f"Versi {code('PMCaptcha')} Saat Ini: %s"
    ],
    "unknown_version": [
        italic("Unknown"),
        italic("Tidak Diketahui")
    ],
    # endregion

    # region Vocabs
    "vocab_msg": [
        "Message",
        "Pesan"
    ],
    "vocab_array": [
        "List",
        "Daftar"
    ],
    "vocab_bool": [
        "Boolean",
        "y / n "
    ],
    "vocab_int": [
        "Integer",
        "Bilangan Bulat"
    ],
    "vocab_cmd": [
        "Command",
        "Perintah"
    ],
    "vocab_rule": [
        "Rule",
        "Aturan"
    ],
    "vocab_action": [
        "Action",
        "Tindakan"
    ],
    # endregion

    # region Captcha Challenge
    "verify_verified": [
        "Verified user",
        "Pengguna Terverifikasi"
    ],
    "verify_unverified": [
        "Unverified user",
        "Pengguna Tidak Terverifikasi"
    ],
    "verify_blocked": [
        "You were blocked.",
        "Anda telah diblokir."
    ],
    "verify_log_punished": [
        "User %s has been %s.",
        "Pengguna %s telah %s."
    ],
    "verify_log_passed": [
        "User %s has passed the %s captcha.",
        "Pengguna %s telah lulus captcha %s."
    ],
    "verify_challenge": [
        "Please answer this question to prove you are human (1 chance)",
        "Silakan jawab pertanyaan ini untuk membuktikan Anda adalah manusia (1 kesempatan)"
    ],
    "verify_challenge_timed": [
        "You have %i seconds.",
        "Anda memiliki %i detik."
    ],
    "verify_passed": [
        "Verification passed.",
        "Verifikasi berhasil."
    ],
    "verify_failed": [
        "Verification failed.",
        "Verifikasi gagal."
    ],
    "verify_timeout": [
        "Verification timeout.",
        "Waktu verifikasi habis."
    ],
    # Image
    "verify_complete_image": [
        "Please complete the following image captcha.",
        "Silakan lengkapi captcha gambar berikut."
    ],
    # Sticker
    "verify_send_sticker": [
        "Please send a sticker to me.",
        "Silakan kirim stiker ke saya."
    ],
    # endregion

    # region Help
    "cmd_param": [
        "Parameter",
        "Parameter"
    ],
    "cmd_param_optional": [
        "Optional",
        "Opsional"
    ],
    "cmd_alias": [
        "Alias",
        "Alias"
    ],
    "cmd_detail": [
        f"Do {code(f',{user_cmd_name} h ')}[command ] for details",
        f"Untuk detail, silakan ketik {code(f',{user_cmd_name} h ')}[perintah ]"
    ],
    "cmd_not_found": [
        "Command Not Found",
        "Perintah Tidak Ditemukan"
    ],
    "cmd_list": [
        "Command List",
        "Daftar Perintah"
    ],
    "priority": [
        "Priority",
        "Prioritas"
    ], 
    "cmd_search_result": [
        f"Search Result for `%s`",
        f"Hasil Pencarian untuk `%s`"
    ],
    "cmd_search_docs": [
        "Documentation",
        "Dokumentasi"
    ],
    "cmd_search_cmds": [
        "Commands",
        "Perintah"
    ],
    "cmd_search_none": [
        "No result found.",
        "Tidak ada hasil ditemukan."
    ],
    # endregion

    # region Check
    "user_verified": [
        f"User {code('%i')} {italic('verified')}",
        f"Pengguna {code('%i')} {italic('terverifikasi')}"
    ],
    "user_unverified": [
        f"User {code('%i')} {bold('unverified')}",
        f"Pengguna {code('%i')} {bold('tidak terverifikasi')}"
    ],
    # endregion

    # region Add / Delete
    "add_whitelist_success": [
        f"User {code('%i')} added to whitelist",
        f"Pengguna {code('%i')} ditambahkan ke daftar putih"
    ],
    "add_whitelist_failed": [
        f"Failed to add iser {code('%i')} to whitelist",
        f"Gagal menambahkan pengguna {code('%i')} ke daftar putih"
    ],
    "remove_verify_log_success": [
        f"Removed User {code('%i')}'s verify record",
        f"Catatan verifikasi pengguna {code('%i')} telah dihapus"
    ],
    "remove_verify_log_failed": [
        f"Failed to remove User {code('%i')}'s verify record.",
        f"Gagal menghapus catatan verifikasi pengguna {code('%i')}."
    ],
    "remove_verify_log_not_found": [
        f"Verify record not found for User {code('%i')}",
        f"Catatan verifikasi tidak ditemukan untuk pengguna {code('%i')}"
    ],
    # endregion

    # region Unstuck
    "unstuck_success": [
        f"User {code('%i')} has removed from challenge mode",
        f"Pengguna {code('%i')} telah dihapus dari mode tantangan"
    ],
    "not_stuck": [
        f"User {code('%i')} is not stuck",
        f"Pengguna {code('%i')} tidak terjebak"
    ],
    # endregion

    # region Welcome
    "welcome_curr_rule": [
       "Current welcome rule",
       "Aturan selamat datang saat ini"
    ],
    "welcome_set": [
        "Welcome message set.",
        "Pesan selamat datang telah diatur."
    ],
    "welcome_reset": [
        "Welcome message reset.",
        "Pesan selamat datang telah direset."
    ],
    # endregion

    # region Whitelist
    "whitelist_curr_rule": [
        "Current whitelist rule",
        "Aturan daftar putih saat ini"
    ],
    "whitelist_set": [
        "Keywords whitelist set.",
        "Daftar putih kata kunci telah diatur."
    ],
    "whitelist_reset": [
        "Keywords whitelist reset.",
        "Daftar putih kata kunci telah direset."
    ],
    # endregion

    # region Blacklist
    "blacklist_curr_rule": [
        "Current blacklist rule",
        "Aturan daftar hitam saat ini"
    ],
    "blacklist_set": [
        "Keywords blacklist set.",
        "Daftar hitam kata kunci telah diatur."
    ],
    "blacklist_reset": [
        "Keywords blacklist reset.",
        "Daftar hitam kata kunci telah direset."
    ],
    "blacklist_triggered": [
        "Blacklist rule triggered",
        "Aturan daftar hitam dipicu"
    ],
    # endregion

    # region Timeout
    "timeout_curr_rule": [
        "Current timeout: %i second(s)",
        "Waktu tunggu saat ini: %i detik"
    ],
    "timeout_set": [
        "Verification timeout has been set to %i seconds.",
        "Waktu tunggu verifikasi telah diatur menjadi %i detik."
    ],
    "timeout_off": [
        "Verification timeout disabled.",
        "Waktu tunggu verifikasi dinonaktifkan."
    ],
    "timeout_exceeded": [
        "Verification timeout.",
        "Waktu tunggu verifikasi habis."
    ],
    # endregion

    # region Disable PM
    "disable_pm_curr_rule": [
        "Current disable PM status: %s",
        "Status disable PM saat ini: %s"
    ],
    "disable_pm_tip_exception": [
        "This feature will automatically allow contents and whitelist users.",
        "Fitur ini akan secara otomatis mengizinkan konten dan pengguna daftar putih."
    ],
    "disable_set": [
        f"Disable private chat has been set to {bold('%s')}.",
        f"Disable chat pribadi telah diatur menjadi {bold('%s')}."
    ],
    "disable_pm_enabled": [
        "Owner has private chat disabled.",
        "Pemilik telah menonaktifkan chat pribadi."
    ],
    # endregion

    # region Stats
    "stats_display": [
        f"has verified {bold('%i')} users in total.\nSuccess: {bold('%i')}\nBlocked: {bold('%i')}\n\nCurrent Status:\nVerifing: {bold('%i')}\nBanning: {bold('%i')}\nBoom Times: {bold('%i')}",
        f"telah memverifikasi {bold('%i')} pengguna secara total.\nSukses: {bold('%i')}\nDiblokir: {bold('%i')}\n\nStatus Saat Ini:\nVerifikasi: {bold('%i')}\nPemblokiran: {bold('%i')}\nWaktu Ledakan: {bold('%i')}"
    ],
    "stats_reset": [
        "Statistics has been reset.",
        "Statistik telah direset."
    ],
    "stats_flooding": [
        bold(f"This account is being flooding, count: {code('%i')}"),
        bold(f"Akun ini sedang mengalami serangan, jumlah: {code('%i')}")
    ],
    # endregion

    # region Action
    "action_curr_rule": [
        "Current action rule",
        "Aturan aksi saat ini"
    ],
    "action_set": [
        f"Action has been set to {bold('%s')}.",
        f"Aksi telah diatur menjadi {bold('%s')}."
    ],
    "action_set_none": [
        "Action has been set to none.",
        "Aksi telah diatur menjadi tidak ada."
    ],
    "action_ban": [
        "Ban",
        "Blokir"
    ],
    "action_delete": [
        "Ban and delete",
        "Blokir dan hapus"
    ],
    "action_archive": [
        "Ban and archive",
        "Blokir dan arsip"
    ],
    # endregion

    # region Report
    "report_curr_rule": [
        "Current report state: %s",
        "Status laporan saat ini: %s"
    ],
    "report_set": [
        f"Report has been set to {bold('%s')}.",
        f"Laporan telah diatur menjadi {bold('%s')}."
    ],
    # endregion

    # region Premium
    "premium_curr_rule": [
        "Current premium user rule",
        "Aturan pengguna premium saat ini"
    ],
    "premium_set_allow": [
        f"Telegram Premium users will be allowed to {bold('bypass')} the captcha.",
        f"Pengguna Telegram Premium akan diizinkan untuk {bold('melewati')} captcha."
    ],
    "premium_set_ban": [
        f"Telegram Premium users will be {bold('banned')} from private chat.",
        f"Pengguna Telegram Premium akan {bold('diblokir')} dari chat pribadi."
    ],
    "premium_set_only": [
        f"{bold('Only allowed')} Telegram Premium users to private chat.",
        f"{bold('Hanya diizinkan')} pengguna Telegram Premium untuk chat pribadi."
    ],
    "premium_set_none": [
        "Nothing will do to Telegram Premium",
        "Tidak ada yang akan dilakukan pada pengguna Telegram Premium"
    ],
    "premium_only": [
        "Owner only allows Telegram Premium users to private chat.",
        "Pemilik hanya mengizinkan pengguna Telegram Premium untuk chat pribadi."
    ],
    "premium_ban": [
        "Owner bans Telegram Premium users from private chat.",
        "Pemilik memblokir pengguna Telegram Premium dari chat pribadi."
    ],
    # endregion

    # region Groups In Common
    "groups_in_common_curr_rule": [
        "Current groups in common rule",
        "Aturan grup umum saat ini"
    ],
    "groups_in_common_set": [
        f"Groups in common larger than {bold('%i')} will be whitelisted.",
        f"Grup umum lebih besar dari {bold('%i')} akan diizinkan."
    ],
    "groups_in_common_disabled": [
        "Group in command is not enabled",
        "Grup dalam perintah tidak diaktifkan"
    ],
    "groups_in_common_disable": [
        "Groups in common disabled.",
        "Grup umum dinonaktifkan."
    ],
    # endregion

    # region Chat History
    "chat_history_curr_rule": [
        f"Chat history equal or larger than {bold('%i')} will be whitelisted.",
        f"Riwayat chat sama dengan atau lebih besar dari {bold('%i')} akan diizinkan."
    ],
    "chat_history_disabled": [
        "Chat history check is not enabled",
        "Pemeriksaan riwayat chat tidak diaktifkan"
    ],
    # endregion

    # region Initiative
    "initiative_curr_rule": [
        "Current initiative status: %s",
        "Status inisiatif saat ini: %s"
    ],
    "initiative_set": [
        f"Initiative has been set to {bold('%s')}.",
        f"Inisiatif telah diatur menjadi {bold('%s')}."
    ],
    # endregion

    # region Silent
    "silent_curr_rule": [
        "Current silent status: %s",
        "Status diam saat ini: %s"
    ],
    "silent_set": [
        f"Silent has been set to {bold('%s')}.",
        f"Diam telah diatur menjadi {bold('%s')}."
    ],
    # endregion

    # region Flood
    "flood_curr_rule": [
        "Current flood detect limit was set to %i user(s)",
        "Batas deteksi banjir saat ini diatur menjadi %i pengguna"
    ],
    # Username
    "flood_username_curr_rule": [
        "Current flood username option was set to %s",
        "Opsi username banjir saat ini telah diatur ke %s"
    ],
    "flood_username_set_confirm": [
        (f"The feature may lose your username, are you sure you want to enable this feature?\n"
         f"Please enter {code(f',{cmd_name} flood_username y')} again to confirm."),
        f"Fitur ini dapat menyebabkan kehilangan username Anda, apakah Anda yakin ingin mengaktifkan fitur ini?\nSilakan masukkan {code(f',{cmd_name} flood_username y')} lagi untuk konfirmasi"
    ],
    "flood_username_set": [
        f"Change username in flood preiod has been %s.",
        f"Perubahan username selama periode banjir telah %s",
    ],
    "flood_channel_desc": [
        ("This channel is a placeholder of username, which the owner is being flooded.\n"
         "Please content him later after this channel is gone."),
        "Ini adalah saluran tempat untuk pengaturan username, yang dimiliki oleh orang yang sedang dibanjiri.\nSilakan hubungi dia nanti setelah saluran ini hilang."
    ],
    # Action
    "flood_act_curr_rule": [
        "Current flood action was set to %s",
        "Tindakan banjir saat ini telah diatur ke %s"
    ],
    "flood_act_set_asis": [
        f"All users in flood period will be {bold('treat as verify failed')}.",
        f"Semua pengguna selama periode banjir akan di{bold('tangani sebagai gagal verifikasi')}"
    ],
    "flood_act_set_captcha": [
        f"All users in flood period will be {bold('asked for captcha')}.",
        f"Semua pengguna selama periode banjir akan di{bold('diminta untuk captcha')}"
    ],
    "flood_act_set_none": [
        "Nothing will do to users in flood period.",
        "Tidak ada yang akan dilakukan pada pengguna selama periode banjir"
    ],
    "flood_act_set_delete": [
        "All flooded users will be deleted and reported spamming.",
        "Semua pengguna yang dibanjiri akan dihapus dan dilaporkan sebagai spam"
    ],
    # endregion

    # region Custom Rule
    "custom_rule_curr_rule": [
        "Current custom rule",
        "Aturan kustom saat ini"
    ],
    "custom_rule_set": [
        f"Custom rule has been set to\n{code('%s')}.",
        f"Aturan kustom telah diatur ke\n{code('%s')}"
    ],
    "custom_rule_reset": [
        "Custom rule has been deleted.",
        "Aturan kustom telah dihapus"
    ],
    "custom_rule_exec_err": [
        "Error occurred when executing custom rule",
        "Kesalahan terjadi saat menjalankan aturan kustom"
    ],
    # endregion

    # region Collect Logs
    "collect_logs_curr_rule": [
        "Current collect logs status: %s",
        "Status pengumpulan log saat ini: %s"
    ],
    "collect_logs_note": [
        ("This feature will only collect user information and chat logs of non-verifiers "
         f"via @{log_collect_bot}, and is not provided to third parties (except @LivegramBot ).\n"
         "Information collected will be used for PMCaptcha improvements, "
         "toggling this feature does not affect the use of PMCaptcha."),
        (f"Fitur ini hanya akan mengumpulkan informasi pengguna dan log chat dari pengguna yang tidak diverifikasi melalui @{log_collect_bot}; "
         "Dan tidak akan diberikan kepada pihak ketiga (kecuali @LivegramBot). \nInformasi yang dikumpulkan akan digunakan untuk menyempurnakan PMCaptcha. Mengaktifkan atau menonaktifkan fitur ini tidak akan memengaruhi penggunaan PMCaptcha.")
    ],
    "collect_logs_set": [
        "Collect logs has been set to %s.",
        "Pengumpulan log telah diatur ke %s"
    ],
    # endregion

    # region Captcha Type   
    "type_curr_rule": [
        "Current captcha type: %s",
        "Tipe captcha saat ini: %s"
    ],
    "type_set": [
        f"Captcha type has been set to {bold('%s')}.",
        f"Tipe captcha telah diatur ke {bold('%s')}"
    ],
    "type_param_name": [
        "Type",
        "Tipe"
    ],
    "type_captcha_img": [
        "Image",
        "Gambar"
    ],
    "type_captcha_math": [
        "Math",
        "Matematika"
    ],
    "type_captcha_sticker": [
        "Sticker",
        "Stiker"
    ],
    # endregion

    # region Export / Import Settings
    "export_success": [
        "Export success, settings has exported into `Saved Messages`",
        "Ekspor berhasil, pengaturan telah diekspor ke `Pesan Tersimpan`"
    ],
    "import_success": [
        "Import completed.",
        "Impor selesai"
    ],
    "import_failed": [
        "Import failed.",
        "Impor gagal"
    ],
    "import_version_mismatch": [
        "Config version doesn't match with plugin version.",
        "Versi konfigurasi tidak cocok dengan versi plugin"
    ],
    # endregion

    # region Image Captcha Type
    "img_captcha_curr_rule": [
        "Current image captcha type: %s",
        "Tipe captcha gambar saat ini: %s"
    ],
    "img_captcha_type_func": [
        "funCaptcha",
        "funCaptcha"
    ],
    "img_captcha_type_github": [
        "GitHub",
        "GitHub"
    ],
    "img_captcha_type_rec": [
        "reCaptcha",
        "reCaptcha"
    ],
    "img_captcha_retry_curr_rule": [
        "Current max retry for image captcha: %s",
        "Maksimum retry untuk captcha gambar saat ini: %s"
    ],
    "img_captcha_retry_set": [
        "Max retry for image captcha has been set to %s.",
        "Maksimum retry untuk captcha gambar telah diatur ke %s"
    ],
    # endregion
}

"""Generated from Smithy shape ``com.amazonaws.backup#StartScanJobInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_backup.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_backup.types.malware_scanner
    import aws_sdk_backup.types.scan_mode


class StartScanJobInput(TypedDict):
    backup_vault_name: "str"
    r"""<p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created.</p> <p>Pattern: <code>^[a-zA-Z0-9\-\_]{2,50}$</code> </p>"""
    continuous_scan_end_time: NotRequired["datetime.datetime"]
    """<p>The point in time the scan job will scan up to for a continuous backup.</p>"""
    iam_role_arn: "str"
    """<p>Specifies the IAM role ARN used to create the target recovery point; for example, <code>arn:aws:iam::123456789012:role/S3Access</code>.</p>"""
    idempotency_token: NotRequired["str"]
    """<p>A customer-chosen string that you can use to distinguish between otherwise identical calls to <code>StartScanJob</code>. Retrying a successful request with the same idempotency token results in a success message with no action taken.</p>"""
    malware_scanner: "aws_sdk_backup.types.malware_scanner.MalwareScanner"
    """<p>Specifies the malware scanner used during the scan job. Currently only supports <code>GUARDDUTY</code>.</p>"""
    recovery_point_arn: "str"
    """<p>An Amazon Resource Name (ARN) that uniquely identifies a recovery point. This is your target recovery point for a full scan. If you are running an incremental scan, this will be your a recovery point which has been created after your base recovery point selection.</p>"""
    scan_base_recovery_point_arn: NotRequired["str"]
    """<p>An ARN that uniquely identifies the base recovery point to be used for incremental scanning.</p>"""
    scan_mode: "aws_sdk_backup.types.scan_mode.ScanMode"
    """<p>Specifies the scan type use for the scan job.</p> <p>Includes:</p> <ul> <li> <p> <code>FULL_SCAN</code> will scan the entire data lineage within the backup.</p> </li> <li> <p> <code>INCREMENTAL_SCAN</code> will scan the data difference between the target recovery point and base recovery point ARN.</p> </li> </ul>"""
    scanner_role_arn: "str"
    """<p>Specified the IAM scanner role ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartScanJobInput) -> dict:
    out: dict = {}
    out["BackupVaultName"] = value["backup_vault_name"]
    if "continuous_scan_end_time" in value:
        import aws_sdk_backup.types._prelude.timestamp

        out["ContinuousScanEndTime"] = (
            aws_sdk_backup.types._prelude.timestamp.serialize_json(
                value["continuous_scan_end_time"]
            )
        )
    out["IamRoleArn"] = value["iam_role_arn"]
    if "idempotency_token" in value:
        out["IdempotencyToken"] = value["idempotency_token"]
    import aws_sdk_backup.types.malware_scanner

    out["MalwareScanner"] = aws_sdk_backup.types.malware_scanner.serialize_json(
        value["malware_scanner"]
    )
    out["RecoveryPointArn"] = value["recovery_point_arn"]
    if "scan_base_recovery_point_arn" in value:
        out["ScanBaseRecoveryPointArn"] = value["scan_base_recovery_point_arn"]
    import aws_sdk_backup.types.scan_mode

    out["ScanMode"] = aws_sdk_backup.types.scan_mode.serialize_json(value["scan_mode"])
    out["ScannerRoleArn"] = value["scanner_role_arn"]
    return out


def deserialize_json(data: dict) -> StartScanJobInput:
    out: StartScanJobInput = {}  # type: ignore[typeddict-item]
    if "BackupVaultName" in data:
        out["backup_vault_name"] = data["BackupVaultName"]
    else:
        raise DeserializationError("StartScanJobInput.backup_vault_name required")
    if "ContinuousScanEndTime" in data:
        import aws_sdk_backup.types._prelude.timestamp

        out["continuous_scan_end_time"] = (
            aws_sdk_backup.types._prelude.timestamp.deserialize_json(
                data["ContinuousScanEndTime"]
            )
        )
    if "IamRoleArn" in data:
        out["iam_role_arn"] = data["IamRoleArn"]
    else:
        raise DeserializationError("StartScanJobInput.iam_role_arn required")
    if "IdempotencyToken" in data:
        out["idempotency_token"] = data["IdempotencyToken"]
    if "MalwareScanner" in data:
        import aws_sdk_backup.types.malware_scanner

        out["malware_scanner"] = aws_sdk_backup.types.malware_scanner.deserialize_json(
            data["MalwareScanner"]
        )
    else:
        raise DeserializationError("StartScanJobInput.malware_scanner required")
    if "RecoveryPointArn" in data:
        out["recovery_point_arn"] = data["RecoveryPointArn"]
    else:
        raise DeserializationError("StartScanJobInput.recovery_point_arn required")
    if "ScanBaseRecoveryPointArn" in data:
        out["scan_base_recovery_point_arn"] = data["ScanBaseRecoveryPointArn"]
    if "ScanMode" in data:
        import aws_sdk_backup.types.scan_mode

        out["scan_mode"] = aws_sdk_backup.types.scan_mode.deserialize_json(
            data["ScanMode"]
        )
    else:
        raise DeserializationError("StartScanJobInput.scan_mode required")
    if "ScannerRoleArn" in data:
        out["scanner_role_arn"] = data["ScannerRoleArn"]
    else:
        raise DeserializationError("StartScanJobInput.scanner_role_arn required")
    return out

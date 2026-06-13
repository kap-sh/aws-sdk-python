"""Generated from Smithy shape ``com.amazonaws.ssmsap#BackintConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm_sap.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.backint_mode


class BackintConfig(TypedDict):
    backint_mode: "aws_sdk_ssm_sap.types.backint_mode.BackintMode"
    """<p>AWS service for your database backup.</p>"""
    ensure_no_backup_in_process: "bool"
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: BackintConfig) -> dict:
    out: dict = {}
    import aws_sdk_ssm_sap.types.backint_mode

    out["BackintMode"] = aws_sdk_ssm_sap.types.backint_mode.serialize_json(
        value["backint_mode"]
    )
    out["EnsureNoBackupInProcess"] = value["ensure_no_backup_in_process"]
    return out


def deserialize_json(data: dict) -> BackintConfig:
    out: BackintConfig = {}  # type: ignore[typeddict-item]
    if "BackintMode" in data:
        import aws_sdk_ssm_sap.types.backint_mode

        out["backint_mode"] = aws_sdk_ssm_sap.types.backint_mode.deserialize_json(
            data["BackintMode"]
        )
    else:
        raise DeserializationError("BackintConfig.backint_mode required")
    if "EnsureNoBackupInProcess" in data:
        out["ensure_no_backup_in_process"] = data["EnsureNoBackupInProcess"]
    else:
        raise DeserializationError("BackintConfig.ensure_no_backup_in_process required")
    return out

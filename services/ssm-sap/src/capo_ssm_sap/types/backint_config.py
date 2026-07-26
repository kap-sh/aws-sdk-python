"""Generated from Smithy shape ``com.amazonaws.ssmsap#BackintConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ssm_sap.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm_sap.types.backint_mode


class BackintConfig(TypedDict, closed=True):
    backint_mode: "capo_ssm_sap.types.backint_mode.BackintMode"
    """<p>AWS service for your database backup.</p>"""
    ensure_no_backup_in_process: "bool"
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: BackintConfig) -> dict:
    out: dict = {}
    import capo_ssm_sap.types.backint_mode

    out["BackintMode"] = capo_ssm_sap.types.backint_mode.serialize_json(
        value["backint_mode"]
    )
    out["EnsureNoBackupInProcess"] = value["ensure_no_backup_in_process"]
    return out


def deserialize_json(data: dict) -> BackintConfig:
    out: BackintConfig = {}  # type: ignore[typeddict-item]
    if "BackintMode" in data:
        import capo_ssm_sap.types.backint_mode

        out["backint_mode"] = capo_ssm_sap.types.backint_mode.deserialize_json(
            data["BackintMode"]
        )
    else:
        raise DeserializationError("BackintConfig.backint_mode required")
    if "EnsureNoBackupInProcess" in data:
        out["ensure_no_backup_in_process"] = data["EnsureNoBackupInProcess"]
    else:
        raise DeserializationError("BackintConfig.ensure_no_backup_in_process required")
    return out

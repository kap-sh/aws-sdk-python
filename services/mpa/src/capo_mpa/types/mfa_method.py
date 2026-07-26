"""Generated from Smithy shape ``com.amazonaws.mpa#MfaMethod``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mpa.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mpa.types.mfa_sync_status
    import capo_mpa.types.mfa_type


class MfaMethod(TypedDict, closed=True):
    type: "capo_mpa.types.mfa_type.MfaType"
    """<p>The type of MFA configuration used by the approver</p>"""
    sync_status: "capo_mpa.types.mfa_sync_status.MfaSyncStatus"
    """<p>Indicates if the approver's MFA device is in-sync with the Identity Source</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MfaMethod) -> dict:
    out: dict = {}
    import capo_mpa.types.mfa_type

    out["Type"] = capo_mpa.types.mfa_type.serialize_json(value["type"])
    import capo_mpa.types.mfa_sync_status

    out["SyncStatus"] = capo_mpa.types.mfa_sync_status.serialize_json(
        value["sync_status"]
    )
    return out


def deserialize_json(data: dict) -> MfaMethod:
    out: MfaMethod = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import capo_mpa.types.mfa_type

        out["type"] = capo_mpa.types.mfa_type.deserialize_json(data["Type"])
    else:
        raise DeserializationError("MfaMethod.type required")
    if "SyncStatus" in data:
        import capo_mpa.types.mfa_sync_status

        out["sync_status"] = capo_mpa.types.mfa_sync_status.deserialize_json(
            data["SyncStatus"]
        )
    else:
        raise DeserializationError("MfaMethod.sync_status required")
    return out

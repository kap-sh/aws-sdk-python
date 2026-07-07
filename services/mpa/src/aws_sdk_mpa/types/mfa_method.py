"""Generated from Smithy shape ``com.amazonaws.mpa#MfaMethod``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_mpa.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mpa.types.mfa_sync_status
    import aws_sdk_mpa.types.mfa_type


class MfaMethod(TypedDict, closed=True):
    type: "aws_sdk_mpa.types.mfa_type.MfaType"
    """<p>The type of MFA configuration used by the approver</p>"""
    sync_status: "aws_sdk_mpa.types.mfa_sync_status.MfaSyncStatus"
    """<p>Indicates if the approver's MFA device is in-sync with the Identity Source</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MfaMethod) -> dict:
    out: dict = {}
    import aws_sdk_mpa.types.mfa_type

    out["Type"] = aws_sdk_mpa.types.mfa_type.serialize_json(value["type"])
    import aws_sdk_mpa.types.mfa_sync_status

    out["SyncStatus"] = aws_sdk_mpa.types.mfa_sync_status.serialize_json(
        value["sync_status"]
    )
    return out


def deserialize_json(data: dict) -> MfaMethod:
    out: MfaMethod = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_mpa.types.mfa_type

        out["type"] = aws_sdk_mpa.types.mfa_type.deserialize_json(data["Type"])
    else:
        raise DeserializationError("MfaMethod.type required")
    if "SyncStatus" in data:
        import aws_sdk_mpa.types.mfa_sync_status

        out["sync_status"] = aws_sdk_mpa.types.mfa_sync_status.deserialize_json(
            data["SyncStatus"]
        )
    else:
        raise DeserializationError("MfaMethod.sync_status required")
    return out

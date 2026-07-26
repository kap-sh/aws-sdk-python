"""Generated from Smithy shape ``com.amazonaws.securityhub#StatusReasonsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.status_reason

StatusReasonsList: TypeAlias = list["capo_securityhub.types.status_reason.StatusReason"]


# --- restJson1 ser/de ---
def serialize_json(value: StatusReasonsList) -> list:
    import capo_securityhub.types.status_reason

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.status_reason.serialize_json(item))
    return out


def deserialize_json(data: list) -> StatusReasonsList:
    import capo_securityhub.types.status_reason

    out: StatusReasonsList = []
    for item in data:
        out.append(capo_securityhub.types.status_reason.deserialize_json(item))
    return out

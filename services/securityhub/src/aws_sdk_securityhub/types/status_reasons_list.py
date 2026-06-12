"""Generated from Smithy shape ``com.amazonaws.securityhub#StatusReasonsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.status_reason

StatusReasonsList: TypeAlias = list[
    "aws_sdk_securityhub.types.status_reason.StatusReason"
]


# --- restJson1 ser/de ---
def serialize_json(value: StatusReasonsList) -> list:
    import aws_sdk_securityhub.types.status_reason

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.status_reason.serialize_json(item))
    return out


def deserialize_json(data: list) -> StatusReasonsList:
    import aws_sdk_securityhub.types.status_reason

    out: StatusReasonsList = []
    for item in data:
        out.append(aws_sdk_securityhub.types.status_reason.deserialize_json(item))
    return out

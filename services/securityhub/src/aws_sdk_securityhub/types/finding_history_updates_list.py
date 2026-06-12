"""Generated from Smithy shape ``com.amazonaws.securityhub#FindingHistoryUpdatesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.finding_history_update

FindingHistoryUpdatesList: TypeAlias = list[
    "aws_sdk_securityhub.types.finding_history_update.FindingHistoryUpdate"
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingHistoryUpdatesList) -> list:
    import aws_sdk_securityhub.types.finding_history_update

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.finding_history_update.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FindingHistoryUpdatesList:
    import aws_sdk_securityhub.types.finding_history_update

    out: FindingHistoryUpdatesList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.finding_history_update.deserialize_json(item)
        )
    return out

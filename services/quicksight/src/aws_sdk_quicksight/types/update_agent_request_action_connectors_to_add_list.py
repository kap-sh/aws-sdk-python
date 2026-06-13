"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateAgentRequestActionConnectorsToAddList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn

UpdateAgentRequestActionConnectorsToAddList: TypeAlias = list[
    "aws_sdk_quicksight.types.arn.Arn"
]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentRequestActionConnectorsToAddList) -> list:
    return list(value)


def deserialize_json(data: list) -> UpdateAgentRequestActionConnectorsToAddList:
    return list(data)

"""Generated from Smithy shape ``com.amazonaws.qconnect#AssistantAssociationIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.uuid_or_arn

AssistantAssociationIdList: TypeAlias = list[
    "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssistantAssociationIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> AssistantAssociationIdList:
    return list(data)

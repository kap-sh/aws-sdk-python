"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemRelatedItemsFilterKey``."""

from typing import Literal, TypeAlias, cast

OpsItemRelatedItemsFilterKey: TypeAlias = Literal[
    "ResourceType",
    "AssociationId",
    "ResourceUri",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItemRelatedItemsFilterKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OpsItemRelatedItemsFilterKey:
    return cast(OpsItemRelatedItemsFilterKey, data)

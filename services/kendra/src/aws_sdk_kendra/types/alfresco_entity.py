"""Generated from Smithy shape ``com.amazonaws.kendra#AlfrescoEntity``."""

from typing import Literal, TypeAlias, cast

AlfrescoEntity: TypeAlias = Literal[
    "wiki",
    "blog",
    "documentLibrary",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AlfrescoEntity) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AlfrescoEntity:
    return cast(AlfrescoEntity, data)

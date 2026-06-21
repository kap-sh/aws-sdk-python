"""Generated from Smithy shape ``com.amazonaws.emr#InstanceCollectionType``."""

from typing import Literal, TypeAlias, cast

InstanceCollectionType: TypeAlias = Literal[
    "INSTANCE_FLEET",
    "INSTANCE_GROUP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceCollectionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceCollectionType:
    return cast(InstanceCollectionType, data)

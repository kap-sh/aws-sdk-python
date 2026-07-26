"""Generated from Smithy shape ``com.amazonaws.glue#MetadataOperation``."""

from typing import Literal, TypeAlias, cast

MetadataOperation: TypeAlias = Literal["CREATE",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetadataOperation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MetadataOperation:
    return cast(MetadataOperation, data)

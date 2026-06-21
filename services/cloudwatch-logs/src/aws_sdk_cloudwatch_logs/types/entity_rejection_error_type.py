"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#EntityRejectionErrorType``."""

from typing import Literal, TypeAlias, cast

EntityRejectionErrorType: TypeAlias = Literal[
    "InvalidEntity",
    "InvalidTypeValue",
    "InvalidKeyAttributes",
    "InvalidAttributes",
    "EntitySizeTooLarge",
    "UnsupportedLogGroupType",
    "MissingRequiredFields",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityRejectionErrorType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EntityRejectionErrorType:
    return cast(EntityRejectionErrorType, data)

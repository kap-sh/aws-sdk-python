"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#NamespaceDeletionStatusErrorCodes``."""

from typing import Literal, TypeAlias, cast

NamespaceDeletionStatusErrorCodes: TypeAlias = Literal["VALIDATION_FAILED",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NamespaceDeletionStatusErrorCodes) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NamespaceDeletionStatusErrorCodes:
    return cast(NamespaceDeletionStatusErrorCodes, data)

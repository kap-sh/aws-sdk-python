"""Generated from Smithy shape ``com.amazonaws.fsx#Unit``."""

from typing import Literal, TypeAlias, cast

Unit: TypeAlias = Literal["DAYS",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Unit) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Unit:
    return cast(Unit, data)

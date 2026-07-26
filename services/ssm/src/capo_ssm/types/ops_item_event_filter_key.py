"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemEventFilterKey``."""

from typing import Literal, TypeAlias, cast

OpsItemEventFilterKey: TypeAlias = Literal["OpsItemId",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItemEventFilterKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OpsItemEventFilterKey:
    return cast(OpsItemEventFilterKey, data)

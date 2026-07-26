"""Generated from Smithy shape ``com.amazonaws.configservice#Owner``."""

from typing import Literal, TypeAlias, cast

Owner: TypeAlias = Literal[
    "CUSTOM_LAMBDA",
    "AWS",
    "CUSTOM_POLICY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Owner) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Owner:
    return cast(Owner, data)

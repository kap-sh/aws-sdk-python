"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#orderString``."""

from typing import Literal, TypeAlias, cast

orderString: TypeAlias = Literal[
    "ASC",
    "DESC",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: orderString) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> orderString:
    return cast(orderString, data)

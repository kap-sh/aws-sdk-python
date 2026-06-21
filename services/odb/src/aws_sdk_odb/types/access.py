"""Generated from Smithy shape ``com.amazonaws.odb#Access``."""

from typing import Literal, TypeAlias, cast

Access: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Access) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Access:
    return cast(Access, data)

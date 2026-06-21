"""Generated from Smithy shape ``com.amazonaws.cloudhsm#ClientVersion``."""

from typing import Literal, TypeAlias, cast

ClientVersion: TypeAlias = Literal[
    "5.1",
    "5.3",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClientVersion) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClientVersion:
    return cast(ClientVersion, data)

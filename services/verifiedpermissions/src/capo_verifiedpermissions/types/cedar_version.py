"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#CedarVersion``."""

from typing import Literal, TypeAlias, cast

CedarVersion: TypeAlias = Literal[
    "CEDAR_2",
    "CEDAR_4",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CedarVersion) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CedarVersion:
    return cast(CedarVersion, data)

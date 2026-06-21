"""Generated from Smithy shape ``com.amazonaws.pcs#SlurmRestMode``."""

from typing import Literal, TypeAlias, cast

SlurmRestMode: TypeAlias = Literal[
    "STANDARD",
    "NONE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SlurmRestMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SlurmRestMode:
    return cast(SlurmRestMode, data)

"""Generated from Smithy shape ``com.amazonaws.pcs#EndpointType``."""

from typing import Literal, TypeAlias, cast

EndpointType: TypeAlias = Literal[
    "SLURMCTLD",
    "SLURMDBD",
    "SLURMRESTD",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EndpointType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EndpointType:
    return cast(EndpointType, data)

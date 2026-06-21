"""Generated from Smithy shape ``com.amazonaws.storagegateway#AutomaticUpdatePolicy``."""

from typing import Literal, TypeAlias, cast

AutomaticUpdatePolicy: TypeAlias = Literal[
    "ALL_VERSIONS",
    "EMERGENCY_VERSIONS_ONLY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutomaticUpdatePolicy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutomaticUpdatePolicy:
    return cast(AutomaticUpdatePolicy, data)

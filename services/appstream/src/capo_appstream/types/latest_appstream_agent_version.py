"""Generated from Smithy shape ``com.amazonaws.appstream#LatestAppstreamAgentVersion``."""

from typing import Literal, TypeAlias, cast

LatestAppstreamAgentVersion: TypeAlias = Literal[
    "TRUE",
    "FALSE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LatestAppstreamAgentVersion) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LatestAppstreamAgentVersion:
    return cast(LatestAppstreamAgentVersion, data)

"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ReplicationEndpointTypeValue``."""

from typing import Literal, TypeAlias, cast

ReplicationEndpointTypeValue: TypeAlias = Literal[
    "source",
    "target",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationEndpointTypeValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReplicationEndpointTypeValue:
    return cast(ReplicationEndpointTypeValue, data)

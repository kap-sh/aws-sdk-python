"""Generated from Smithy shape ``com.amazonaws.transfer#ConnectorStatus``."""

from typing import Literal, TypeAlias, cast

ConnectorStatus: TypeAlias = Literal[
    "ACTIVE",
    "ERRORED",
    "PENDING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectorStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConnectorStatus:
    return cast(ConnectorStatus, data)

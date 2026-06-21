"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#DeleteAgentErrorCode``."""

from typing import Literal, TypeAlias, cast

DeleteAgentErrorCode: TypeAlias = Literal[
    "NOT_FOUND",
    "INTERNAL_SERVER_ERROR",
    "AGENT_IN_USE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAgentErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeleteAgentErrorCode:
    return cast(DeleteAgentErrorCode, data)

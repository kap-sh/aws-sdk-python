"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CloudWatchLogsFilterOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore.errors import DeserializationError

"""<p>The comparison operator used to filter CloudWatch Logs entries.</p>"""
CloudWatchLogsFilterOperator: TypeAlias = Literal[
    "Equals",
    "NotEquals",
    "GreaterThan",
    "LessThan",
    "GreaterThanOrEqual",
    "LessThanOrEqual",
    "Contains",
    "NotContains",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Equals",
        "NotEquals",
        "GreaterThan",
        "LessThan",
        "GreaterThanOrEqual",
        "LessThanOrEqual",
        "Contains",
        "NotContains",
    )
)


def serialize_json(value: CloudWatchLogsFilterOperator) -> str:
    return value


def deserialize_json(data: str) -> CloudWatchLogsFilterOperator:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CloudWatchLogsFilterOperator value: {data!r}"
        )
    return cast(CloudWatchLogsFilterOperator, data)

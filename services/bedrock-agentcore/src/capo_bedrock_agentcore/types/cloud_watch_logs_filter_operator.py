"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CloudWatchLogsFilterOperator``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: CloudWatchLogsFilterOperator) -> str:
    return value


def deserialize_json(data: str) -> CloudWatchLogsFilterOperator:
    return cast(CloudWatchLogsFilterOperator, data)

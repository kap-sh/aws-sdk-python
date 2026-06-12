"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GroupingIdentifier``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.grouping_identifier_key
    import aws_sdk_cloudwatch_logs.types.grouping_identifier_value


class GroupingIdentifier(TypedDict):
    key: NotRequired[
        "aws_sdk_cloudwatch_logs.types.grouping_identifier_key.GroupingIdentifierKey"
    ]
    """<p>The key that identifies the grouping characteristic. The format of the key uses dot notation. Examples are, <code>dataSource.Name</code>, <code>dataSource.Type</code>, and <code>dataSource.Format</code>.</p>"""
    value: NotRequired[
        "aws_sdk_cloudwatch_logs.types.grouping_identifier_value.GroupingIdentifierValue"
    ]
    """<p>The value associated with the grouping characteristic. Examples are <code>amazon_vpc</code>, <code>flow</code>, and <code>OCSF</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GroupingIdentifier) -> dict:
    out: dict = {}
    if "key" in value:
        out["key"] = value["key"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GroupingIdentifier:
    out: GroupingIdentifier = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    if "value" in data:
        out["value"] = data["value"]
    return out

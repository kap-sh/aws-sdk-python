"""Generated from Smithy shape ``com.amazonaws.opensearch#Insight``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.boolean
    import aws_sdk_opensearch.types.guid
    import aws_sdk_opensearch.types.insight_priority_level
    import aws_sdk_opensearch.types.insight_status
    import aws_sdk_opensearch.types.insight_type
    import aws_sdk_opensearch.types.string
    import aws_sdk_opensearch.types.update_timestamp


class Insight(TypedDict, closed=True):
    insight_id: NotRequired["aws_sdk_opensearch.types.guid.GUID"]
    """<p>The unique identifier of the insight.</p>"""
    display_name: NotRequired["aws_sdk_opensearch.types.string.String"]
    """<p>The display name of the insight.</p>"""
    type: NotRequired["aws_sdk_opensearch.types.insight_type.InsightType"]
    """<p>The type of the insight. Possible values are <code>EVENT</code> and <code>RECOMMENDATION</code>.</p>"""
    priority: NotRequired[
        "aws_sdk_opensearch.types.insight_priority_level.InsightPriorityLevel"
    ]
    """<p>The priority level of the insight. Possible values are <code>CRITICAL</code>, <code>HIGH</code>, <code>MEDIUM</code>, and <code>LOW</code>.</p>"""
    status: NotRequired["aws_sdk_opensearch.types.insight_status.InsightStatus"]
    """<p>The current status of the insight. Possible values are <code>ACTIVE</code>, <code>RESOLVED</code>, and <code>DISMISSED</code>.</p>"""
    creation_time: NotRequired[
        "aws_sdk_opensearch.types.update_timestamp.UpdateTimestamp"
    ]
    """<p>The timestamp when the insight was created, in epoch milliseconds.</p>"""
    update_time: NotRequired[
        "aws_sdk_opensearch.types.update_timestamp.UpdateTimestamp"
    ]
    """<p>The timestamp when the insight was last updated, in epoch milliseconds.</p>"""
    is_experimental: NotRequired["aws_sdk_opensearch.types.boolean.Boolean"]
    """<p>Indicates whether the insight is experimental.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Insight) -> dict:
    out: dict = {}
    if "insight_id" in value:
        out["InsightId"] = value["insight_id"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "type" in value:
        import aws_sdk_opensearch.types.insight_type

        out["Type"] = aws_sdk_opensearch.types.insight_type.serialize_json(
            value["type"]
        )
    if "priority" in value:
        import aws_sdk_opensearch.types.insight_priority_level

        out["Priority"] = (
            aws_sdk_opensearch.types.insight_priority_level.serialize_json(
                value["priority"]
            )
        )
    if "status" in value:
        import aws_sdk_opensearch.types.insight_status

        out["Status"] = aws_sdk_opensearch.types.insight_status.serialize_json(
            value["status"]
        )
    if "creation_time" in value:
        import aws_sdk_opensearch.types.update_timestamp

        out["CreationTime"] = aws_sdk_opensearch.types.update_timestamp.serialize_json(
            value["creation_time"]
        )
    if "update_time" in value:
        import aws_sdk_opensearch.types.update_timestamp

        out["UpdateTime"] = aws_sdk_opensearch.types.update_timestamp.serialize_json(
            value["update_time"]
        )
    if "is_experimental" in value:
        out["IsExperimental"] = value["is_experimental"]
    return out


def deserialize_json(data: dict) -> Insight:
    out: Insight = {}  # type: ignore[typeddict-item]
    if "InsightId" in data:
        out["insight_id"] = data["InsightId"]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "Type" in data:
        import aws_sdk_opensearch.types.insight_type

        out["type"] = aws_sdk_opensearch.types.insight_type.deserialize_json(
            data["Type"]
        )
    if "Priority" in data:
        import aws_sdk_opensearch.types.insight_priority_level

        out["priority"] = (
            aws_sdk_opensearch.types.insight_priority_level.deserialize_json(
                data["Priority"]
            )
        )
    if "Status" in data:
        import aws_sdk_opensearch.types.insight_status

        out["status"] = aws_sdk_opensearch.types.insight_status.deserialize_json(
            data["Status"]
        )
    if "CreationTime" in data:
        import aws_sdk_opensearch.types.update_timestamp

        out["creation_time"] = (
            aws_sdk_opensearch.types.update_timestamp.deserialize_json(
                data["CreationTime"]
            )
        )
    if "UpdateTime" in data:
        import aws_sdk_opensearch.types.update_timestamp

        out["update_time"] = aws_sdk_opensearch.types.update_timestamp.deserialize_json(
            data["UpdateTime"]
        )
    if "IsExperimental" in data:
        out["is_experimental"] = data["IsExperimental"]
    return out

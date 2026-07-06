"""Generated from Smithy shape ``com.amazonaws.detective#GetInvestigationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_detective.types.entity_arn
    import aws_sdk_detective.types.entity_type
    import aws_sdk_detective.types.graph_arn
    import aws_sdk_detective.types.investigation_id
    import aws_sdk_detective.types.severity
    import aws_sdk_detective.types.state
    import aws_sdk_detective.types.status
    import aws_sdk_detective.types.timestamp


class GetInvestigationResponse(TypedDict, closed=True):
    graph_arn: NotRequired["aws_sdk_detective.types.graph_arn.GraphArn"]
    """<p>The Amazon Resource Name (ARN) of the behavior graph.</p>"""
    investigation_id: NotRequired[
        "aws_sdk_detective.types.investigation_id.InvestigationId"
    ]
    """<p>The investigation ID of the investigation report.</p>"""
    entity_arn: NotRequired["aws_sdk_detective.types.entity_arn.EntityArn"]
    """<p>The unique Amazon Resource Name (ARN). Detective supports IAM user ARNs and IAM role ARNs.</p>"""
    entity_type: NotRequired["aws_sdk_detective.types.entity_type.EntityType"]
    """<p>Type of entity. For example, Amazon Web Services accounts, such as an IAM user and/or IAM role.</p>"""
    created_time: NotRequired["aws_sdk_detective.types.timestamp.Timestamp"]
    """<p>The creation time of the investigation report in UTC time stamp format.</p>"""
    scope_start_time: NotRequired["aws_sdk_detective.types.timestamp.Timestamp"]
    """<p>The start date and time used to set the scope time within which you want to generate the investigation report. The value is an UTC ISO8601 formatted string. For example, <code>2021-08-18T16:35:56.284Z</code>.</p>"""
    scope_end_time: NotRequired["aws_sdk_detective.types.timestamp.Timestamp"]
    """<p>The data and time when the investigation began. The value is an UTC ISO8601 formatted string. For example, <code>2021-08-18T16:35:56.284Z</code>.</p>"""
    status: NotRequired["aws_sdk_detective.types.status.Status"]
    """<p>The status based on the completion status of the investigation.</p>"""
    severity: NotRequired["aws_sdk_detective.types.severity.Severity"]
    """<p>The severity assigned is based on the likelihood and impact of the indicators of compromise discovered in the investigation.</p>"""
    state: NotRequired["aws_sdk_detective.types.state.State"]
    """<p>The current state of the investigation. An archived investigation indicates that you have completed reviewing the investigation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInvestigationResponse) -> dict:
    out: dict = {}
    if "graph_arn" in value:
        out["GraphArn"] = value["graph_arn"]
    if "investigation_id" in value:
        out["InvestigationId"] = value["investigation_id"]
    if "entity_arn" in value:
        out["EntityArn"] = value["entity_arn"]
    if "entity_type" in value:
        import aws_sdk_detective.types.entity_type

        out["EntityType"] = aws_sdk_detective.types.entity_type.serialize_json(
            value["entity_type"]
        )
    if "created_time" in value:
        import aws_sdk_detective.types.timestamp

        out["CreatedTime"] = aws_sdk_detective.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "scope_start_time" in value:
        import aws_sdk_detective.types.timestamp

        out["ScopeStartTime"] = aws_sdk_detective.types.timestamp.serialize_json(
            value["scope_start_time"]
        )
    if "scope_end_time" in value:
        import aws_sdk_detective.types.timestamp

        out["ScopeEndTime"] = aws_sdk_detective.types.timestamp.serialize_json(
            value["scope_end_time"]
        )
    if "status" in value:
        import aws_sdk_detective.types.status

        out["Status"] = aws_sdk_detective.types.status.serialize_json(value["status"])
    if "severity" in value:
        import aws_sdk_detective.types.severity

        out["Severity"] = aws_sdk_detective.types.severity.serialize_json(
            value["severity"]
        )
    if "state" in value:
        import aws_sdk_detective.types.state

        out["State"] = aws_sdk_detective.types.state.serialize_json(value["state"])
    return out


def deserialize_json(data: dict) -> GetInvestigationResponse:
    out: GetInvestigationResponse = {}  # type: ignore[typeddict-item]
    if "GraphArn" in data:
        out["graph_arn"] = data["GraphArn"]
    if "InvestigationId" in data:
        out["investigation_id"] = data["InvestigationId"]
    if "EntityArn" in data:
        out["entity_arn"] = data["EntityArn"]
    if "EntityType" in data:
        import aws_sdk_detective.types.entity_type

        out["entity_type"] = aws_sdk_detective.types.entity_type.deserialize_json(
            data["EntityType"]
        )
    if "CreatedTime" in data:
        import aws_sdk_detective.types.timestamp

        out["created_time"] = aws_sdk_detective.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if "ScopeStartTime" in data:
        import aws_sdk_detective.types.timestamp

        out["scope_start_time"] = aws_sdk_detective.types.timestamp.deserialize_json(
            data["ScopeStartTime"]
        )
    if "ScopeEndTime" in data:
        import aws_sdk_detective.types.timestamp

        out["scope_end_time"] = aws_sdk_detective.types.timestamp.deserialize_json(
            data["ScopeEndTime"]
        )
    if "Status" in data:
        import aws_sdk_detective.types.status

        out["status"] = aws_sdk_detective.types.status.deserialize_json(data["Status"])
    if "Severity" in data:
        import aws_sdk_detective.types.severity

        out["severity"] = aws_sdk_detective.types.severity.deserialize_json(
            data["Severity"]
        )
    if "State" in data:
        import aws_sdk_detective.types.state

        out["state"] = aws_sdk_detective.types.state.deserialize_json(data["State"])
    return out

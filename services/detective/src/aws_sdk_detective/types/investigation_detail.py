"""Generated from Smithy shape ``com.amazonaws.detective#InvestigationDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_detective.types.entity_arn
    import aws_sdk_detective.types.entity_type
    import aws_sdk_detective.types.investigation_id
    import aws_sdk_detective.types.severity
    import aws_sdk_detective.types.state
    import aws_sdk_detective.types.status
    import aws_sdk_detective.types.timestamp


class InvestigationDetail(TypedDict, closed=True):
    investigation_id: NotRequired[
        "aws_sdk_detective.types.investigation_id.InvestigationId"
    ]
    """<p>The investigation ID of the investigation report.</p>"""
    severity: NotRequired["aws_sdk_detective.types.severity.Severity"]
    """<p>Severity based on the likelihood and impact of the indicators of compromise discovered in the investigation.</p>"""
    status: NotRequired["aws_sdk_detective.types.status.Status"]
    """<p>Status based on the completion status of the investigation.</p>"""
    state: NotRequired["aws_sdk_detective.types.state.State"]
    """<p>The current state of the investigation. An archived investigation indicates you have completed reviewing the investigation.</p>"""
    created_time: NotRequired["aws_sdk_detective.types.timestamp.Timestamp"]
    """<p>The time stamp of the creation time of the investigation report. The value is an UTC ISO8601 formatted string. For example, <code>2021-08-18T16:35:56.284Z</code>.</p>"""
    entity_arn: NotRequired["aws_sdk_detective.types.entity_arn.EntityArn"]
    """<p>The unique Amazon Resource Name (ARN) of the IAM user and IAM role.</p>"""
    entity_type: NotRequired["aws_sdk_detective.types.entity_type.EntityType"]
    """<p>Type of entity. For example, Amazon Web Services accounts, such as IAM user and role.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvestigationDetail) -> dict:
    out: dict = {}
    if "investigation_id" in value:
        out["InvestigationId"] = value["investigation_id"]
    if "severity" in value:
        import aws_sdk_detective.types.severity

        out["Severity"] = aws_sdk_detective.types.severity.serialize_json(
            value["severity"]
        )
    if "status" in value:
        import aws_sdk_detective.types.status

        out["Status"] = aws_sdk_detective.types.status.serialize_json(value["status"])
    if "state" in value:
        import aws_sdk_detective.types.state

        out["State"] = aws_sdk_detective.types.state.serialize_json(value["state"])
    if "created_time" in value:
        import aws_sdk_detective.types.timestamp

        out["CreatedTime"] = aws_sdk_detective.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "entity_arn" in value:
        out["EntityArn"] = value["entity_arn"]
    if "entity_type" in value:
        import aws_sdk_detective.types.entity_type

        out["EntityType"] = aws_sdk_detective.types.entity_type.serialize_json(
            value["entity_type"]
        )
    return out


def deserialize_json(data: dict) -> InvestigationDetail:
    out: InvestigationDetail = {}  # type: ignore[typeddict-item]
    if "InvestigationId" in data:
        out["investigation_id"] = data["InvestigationId"]
    if "Severity" in data:
        import aws_sdk_detective.types.severity

        out["severity"] = aws_sdk_detective.types.severity.deserialize_json(
            data["Severity"]
        )
    if "Status" in data:
        import aws_sdk_detective.types.status

        out["status"] = aws_sdk_detective.types.status.deserialize_json(data["Status"])
    if "State" in data:
        import aws_sdk_detective.types.state

        out["state"] = aws_sdk_detective.types.state.deserialize_json(data["State"])
    if "CreatedTime" in data:
        import aws_sdk_detective.types.timestamp

        out["created_time"] = aws_sdk_detective.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if "EntityArn" in data:
        out["entity_arn"] = data["EntityArn"]
    if "EntityType" in data:
        import aws_sdk_detective.types.entity_type

        out["entity_type"] = aws_sdk_detective.types.entity_type.deserialize_json(
            data["EntityType"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.quicksight#DashboardVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.resource_status
    import aws_sdk_quicksight.types.timestamp
    import aws_sdk_quicksight.types.version_description
    import aws_sdk_quicksight.types.version_number


class DashboardVersionSummary(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    created_time: NotRequired["aws_sdk_quicksight.types.timestamp.Timestamp"]
    """<p>The time that this dashboard version was created.</p>"""
    version_number: NotRequired["aws_sdk_quicksight.types.version_number.VersionNumber"]
    """<p>Version number.</p>"""
    status: NotRequired["aws_sdk_quicksight.types.resource_status.ResourceStatus"]
    """<p>The HTTP status of the request.</p>"""
    source_entity_arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>Source entity ARN.</p>"""
    description: NotRequired[
        "aws_sdk_quicksight.types.version_description.VersionDescription"
    ]
    """<p>Description.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DashboardVersionSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "created_time" in value:
        import aws_sdk_quicksight.types.timestamp

        out["CreatedTime"] = aws_sdk_quicksight.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "version_number" in value:
        out["VersionNumber"] = value["version_number"]
    if "status" in value:
        import aws_sdk_quicksight.types.resource_status

        out["Status"] = aws_sdk_quicksight.types.resource_status.serialize_json(
            value["status"]
        )
    if "source_entity_arn" in value:
        out["SourceEntityArn"] = value["source_entity_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> DashboardVersionSummary:
    out: DashboardVersionSummary = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "CreatedTime" in data:
        import aws_sdk_quicksight.types.timestamp

        out["created_time"] = aws_sdk_quicksight.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if "VersionNumber" in data:
        out["version_number"] = data["VersionNumber"]
    if "Status" in data:
        import aws_sdk_quicksight.types.resource_status

        out["status"] = aws_sdk_quicksight.types.resource_status.deserialize_json(
            data["Status"]
        )
    if "SourceEntityArn" in data:
        out["source_entity_arn"] = data["SourceEntityArn"]
    if "Description" in data:
        out["description"] = data["Description"]
    return out

"""Generated from Smithy shape ``com.amazonaws.quicksight#TemplateVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.resource_status
    import aws_sdk_quicksight.types.timestamp
    import aws_sdk_quicksight.types.version_description
    import aws_sdk_quicksight.types.version_number


class TemplateVersionSummary(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the template version.</p>"""
    version_number: NotRequired["aws_sdk_quicksight.types.version_number.VersionNumber"]
    """<p>The version number of the template version.</p>"""
    created_time: NotRequired["aws_sdk_quicksight.types.timestamp.Timestamp"]
    """<p>The time that this template version was created.</p>"""
    status: NotRequired["aws_sdk_quicksight.types.resource_status.ResourceStatus"]
    """<p>The status of the template version.</p>"""
    description: NotRequired[
        "aws_sdk_quicksight.types.version_description.VersionDescription"
    ]
    """<p>The description of the template version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TemplateVersionSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "version_number" in value:
        out["VersionNumber"] = value["version_number"]
    if "created_time" in value:
        import aws_sdk_quicksight.types.timestamp

        out["CreatedTime"] = aws_sdk_quicksight.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "status" in value:
        import aws_sdk_quicksight.types.resource_status

        out["Status"] = aws_sdk_quicksight.types.resource_status.serialize_json(
            value["status"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> TemplateVersionSummary:
    out: TemplateVersionSummary = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "VersionNumber" in data:
        out["version_number"] = data["VersionNumber"]
    if "CreatedTime" in data:
        import aws_sdk_quicksight.types.timestamp

        out["created_time"] = aws_sdk_quicksight.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if "Status" in data:
        import aws_sdk_quicksight.types.resource_status

        out["status"] = aws_sdk_quicksight.types.resource_status.deserialize_json(
            data["Status"]
        )
    if "Description" in data:
        out["description"] = data["Description"]
    return out

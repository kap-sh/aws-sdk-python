"""Generated from Smithy shape ``com.amazonaws.quicksight#TemplateSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.template_name
    import aws_sdk_quicksight.types.timestamp
    import aws_sdk_quicksight.types.version_number


class TemplateSummary(TypedDict):
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>A summary of a template.</p>"""
    template_id: NotRequired[
        "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The ID of the template. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""
    name: NotRequired["aws_sdk_quicksight.types.template_name.TemplateName"]
    """<p>A display name for the template.</p>"""
    latest_version_number: NotRequired[
        "aws_sdk_quicksight.types.version_number.VersionNumber"
    ]
    """<p>A structure containing a list of version numbers for the template summary.</p>"""
    created_time: NotRequired["aws_sdk_quicksight.types.timestamp.Timestamp"]
    """<p>The last time that this template was created.</p>"""
    last_updated_time: NotRequired["aws_sdk_quicksight.types.timestamp.Timestamp"]
    """<p>The last time that this template was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TemplateSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "template_id" in value:
        out["TemplateId"] = value["template_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "latest_version_number" in value:
        out["LatestVersionNumber"] = value["latest_version_number"]
    if "created_time" in value:
        import aws_sdk_quicksight.types.timestamp

        out["CreatedTime"] = aws_sdk_quicksight.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "last_updated_time" in value:
        import aws_sdk_quicksight.types.timestamp

        out["LastUpdatedTime"] = aws_sdk_quicksight.types.timestamp.serialize_json(
            value["last_updated_time"]
        )
    return out


def deserialize_json(data: dict) -> TemplateSummary:
    out: TemplateSummary = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "TemplateId" in data:
        out["template_id"] = data["TemplateId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "LatestVersionNumber" in data:
        out["latest_version_number"] = data["LatestVersionNumber"]
    if "CreatedTime" in data:
        import aws_sdk_quicksight.types.timestamp

        out["created_time"] = aws_sdk_quicksight.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if "LastUpdatedTime" in data:
        import aws_sdk_quicksight.types.timestamp

        out["last_updated_time"] = aws_sdk_quicksight.types.timestamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    return out

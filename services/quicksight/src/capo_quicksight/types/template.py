"""Generated from Smithy shape ``com.amazonaws.quicksight#Template``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.template_name
    import capo_quicksight.types.template_version
    import capo_quicksight.types.timestamp


class Template(TypedDict, closed=True):
    arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the template.</p>"""
    name: NotRequired["capo_quicksight.types.template_name.TemplateName"]
    """<p>The display name of the template.</p>"""
    version: NotRequired["capo_quicksight.types.template_version.TemplateVersion"]
    """<p>A structure describing the versions of the template.</p>"""
    template_id: NotRequired[
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The ID for the template. This is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""
    last_updated_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>Time when this was last updated.</p>"""
    created_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>Time when this was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Template) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "version" in value:
        import capo_quicksight.types.template_version

        out["Version"] = capo_quicksight.types.template_version.serialize_json(
            value["version"]
        )
    if "template_id" in value:
        out["TemplateId"] = value["template_id"]
    if "last_updated_time" in value:
        import capo_quicksight.types.timestamp

        out["LastUpdatedTime"] = capo_quicksight.types.timestamp.serialize_json(
            value["last_updated_time"]
        )
    if "created_time" in value:
        import capo_quicksight.types.timestamp

        out["CreatedTime"] = capo_quicksight.types.timestamp.serialize_json(
            value["created_time"]
        )
    return out


def deserialize_json(data: dict) -> Template:
    out: Template = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Version" in data:
        import capo_quicksight.types.template_version

        out["version"] = capo_quicksight.types.template_version.deserialize_json(
            data["Version"]
        )
    if "TemplateId" in data:
        out["template_id"] = data["TemplateId"]
    if "LastUpdatedTime" in data:
        import capo_quicksight.types.timestamp

        out["last_updated_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    if "CreatedTime" in data:
        import capo_quicksight.types.timestamp

        out["created_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    return out

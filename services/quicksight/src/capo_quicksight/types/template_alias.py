"""Generated from Smithy shape ``com.amazonaws.quicksight#TemplateAlias``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.alias_name
    import capo_quicksight.types.arn
    import capo_quicksight.types.version_number


class TemplateAlias(TypedDict, closed=True):
    alias_name: NotRequired["capo_quicksight.types.alias_name.AliasName"]
    """<p>The display name of the template alias.</p>"""
    arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the template alias.</p>"""
    template_version_number: NotRequired[
        "capo_quicksight.types.version_number.VersionNumber"
    ]
    """<p>The version number of the template alias.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TemplateAlias) -> dict:
    out: dict = {}
    if "alias_name" in value:
        out["AliasName"] = value["alias_name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "template_version_number" in value:
        out["TemplateVersionNumber"] = value["template_version_number"]
    return out


def deserialize_json(data: dict) -> TemplateAlias:
    out: TemplateAlias = {}  # type: ignore[typeddict-item]
    if "AliasName" in data:
        out["alias_name"] = data["AliasName"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "TemplateVersionNumber" in data:
        out["template_version_number"] = data["TemplateVersionNumber"]
    return out

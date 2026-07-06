"""Generated from Smithy shape ``com.amazonaws.ssoadmin#DisplayData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.description
    import aws_sdk_sso_admin.types.icon_url
    import aws_sdk_sso_admin.types.name


class DisplayData(TypedDict, closed=True):
    display_name: NotRequired["aws_sdk_sso_admin.types.name.Name"]
    """<p>The name of the application provider that appears in the portal.</p>"""
    icon_url: NotRequired["aws_sdk_sso_admin.types.icon_url.IconUrl"]
    """<p>A URL that points to an icon that represents the application provider.</p>"""
    description: NotRequired["aws_sdk_sso_admin.types.description.Description"]
    """<p>The description of the application provider that appears in the portal.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisplayData) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "icon_url" in value:
        out["IconUrl"] = value["icon_url"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DisplayData:
    out: DisplayData = {}  # type: ignore[typeddict-item]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "IconUrl" in data:
        out["icon_url"] = data["IconUrl"]
    if "Description" in data:
        out["description"] = data["Description"]
    return out

"""Generated from Smithy shape ``com.amazonaws.workspacesweb#IpRule``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.description
    import aws_sdk_workspaces_web.types.ip_range


class IpRule(TypedDict):
    ip_range: "aws_sdk_workspaces_web.types.ip_range.IpRange"
    """<p>The IP range of the IP rule.</p>"""
    description: NotRequired["aws_sdk_workspaces_web.types.description.Description"]
    """<p>The description of the IP rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IpRule) -> dict:
    out: dict = {}
    out["ipRange"] = value["ip_range"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> IpRule:
    out: IpRule = {}  # type: ignore[typeddict-item]
    if "ipRange" in data:
        out["ip_range"] = data["ipRange"]
    else:
        raise DeserializationError("IpRule.ip_range required")
    if "description" in data:
        out["description"] = data["description"]
    return out

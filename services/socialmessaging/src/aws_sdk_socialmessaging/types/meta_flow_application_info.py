"""Generated from Smithy shape ``com.amazonaws.socialmessaging#MetaFlowApplicationInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_socialmessaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.meta_flow_application_id
    import aws_sdk_socialmessaging.types.meta_flow_application_link
    import aws_sdk_socialmessaging.types.meta_flow_application_name


class MetaFlowApplicationInfo(TypedDict, closed=True):
    link: NotRequired[
        "aws_sdk_socialmessaging.types.meta_flow_application_link.MetaFlowApplicationLink"
    ]
    """<p>The URL link for the Meta application.</p>"""
    name: "aws_sdk_socialmessaging.types.meta_flow_application_name.MetaFlowApplicationName"
    """<p>The name of the Meta application.</p>"""
    id: "aws_sdk_socialmessaging.types.meta_flow_application_id.MetaFlowApplicationId"
    """<p>The unique identifier of the Meta application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetaFlowApplicationInfo) -> dict:
    out: dict = {}
    if "link" in value:
        out["link"] = value["link"]
    out["name"] = value["name"]
    out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> MetaFlowApplicationInfo:
    out: MetaFlowApplicationInfo = {}  # type: ignore[typeddict-item]
    if "link" in data:
        out["link"] = data["link"]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("MetaFlowApplicationInfo.name required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("MetaFlowApplicationInfo.id required")
    return out

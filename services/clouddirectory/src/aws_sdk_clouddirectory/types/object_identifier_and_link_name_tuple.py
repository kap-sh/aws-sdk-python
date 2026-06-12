"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ObjectIdentifierAndLinkNameTuple``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.link_name
    import aws_sdk_clouddirectory.types.object_identifier


class ObjectIdentifierAndLinkNameTuple(TypedDict):
    object_identifier: NotRequired[
        "aws_sdk_clouddirectory.types.object_identifier.ObjectIdentifier"
    ]
    """<p>The ID that is associated with the object.</p>"""
    link_name: NotRequired["aws_sdk_clouddirectory.types.link_name.LinkName"]
    """<p>The name of the link between the parent and the child object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ObjectIdentifierAndLinkNameTuple) -> dict:
    out: dict = {}
    if "object_identifier" in value:
        out["ObjectIdentifier"] = value["object_identifier"]
    if "link_name" in value:
        out["LinkName"] = value["link_name"]
    return out


def deserialize_json(data: dict) -> ObjectIdentifierAndLinkNameTuple:
    out: ObjectIdentifierAndLinkNameTuple = {}  # type: ignore[typeddict-item]
    if "ObjectIdentifier" in data:
        out["object_identifier"] = data["ObjectIdentifier"]
    if "LinkName" in data:
        out["link_name"] = data["LinkName"]
    return out

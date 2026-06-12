"""Generated from Smithy shape ``com.amazonaws.clouddirectory#AttachObjectResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.object_identifier


class AttachObjectResponse(TypedDict):
    attached_object_identifier: NotRequired[
        "aws_sdk_clouddirectory.types.object_identifier.ObjectIdentifier"
    ]
    """<p>The attached <code>ObjectIdentifier</code>, which is the child <code>ObjectIdentifier</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttachObjectResponse) -> dict:
    out: dict = {}
    if "attached_object_identifier" in value:
        out["AttachedObjectIdentifier"] = value["attached_object_identifier"]
    return out


def deserialize_json(data: dict) -> AttachObjectResponse:
    out: AttachObjectResponse = {}  # type: ignore[typeddict-item]
    if "AttachedObjectIdentifier" in data:
        out["attached_object_identifier"] = data["AttachedObjectIdentifier"]
    return out

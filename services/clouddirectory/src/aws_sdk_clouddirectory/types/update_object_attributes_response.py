"""Generated from Smithy shape ``com.amazonaws.clouddirectory#UpdateObjectAttributesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.object_identifier


class UpdateObjectAttributesResponse(TypedDict, closed=True):
    object_identifier: NotRequired[
        "aws_sdk_clouddirectory.types.object_identifier.ObjectIdentifier"
    ]
    """<p>The <code>ObjectIdentifier</code> of the updated object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateObjectAttributesResponse) -> dict:
    out: dict = {}
    if "object_identifier" in value:
        out["ObjectIdentifier"] = value["object_identifier"]
    return out


def deserialize_json(data: dict) -> UpdateObjectAttributesResponse:
    out: UpdateObjectAttributesResponse = {}  # type: ignore[typeddict-item]
    if "ObjectIdentifier" in data:
        out["object_identifier"] = data["ObjectIdentifier"]
    return out

"""Generated from Smithy shape ``com.amazonaws.clouddirectory#CreateObjectResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.object_identifier


class CreateObjectResponse(TypedDict, closed=True):
    object_identifier: NotRequired[
        "capo_clouddirectory.types.object_identifier.ObjectIdentifier"
    ]
    """<p>The identifier that is associated with the object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateObjectResponse) -> dict:
    out: dict = {}
    if "object_identifier" in value:
        out["ObjectIdentifier"] = value["object_identifier"]
    return out


def deserialize_json(data: dict) -> CreateObjectResponse:
    out: CreateObjectResponse = {}  # type: ignore[typeddict-item]
    if "ObjectIdentifier" in data:
        out["object_identifier"] = data["ObjectIdentifier"]
    return out

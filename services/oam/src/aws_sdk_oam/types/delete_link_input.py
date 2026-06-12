"""Generated from Smithy shape ``com.amazonaws.oam#DeleteLinkInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_oam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_oam.types.resource_identifier


class DeleteLinkInput(TypedDict):
    identifier: "aws_sdk_oam.types.resource_identifier.ResourceIdentifier"
    """<p>The ARN of the link to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteLinkInput) -> dict:
    out: dict = {}
    out["Identifier"] = value["identifier"]
    return out


def deserialize_json(data: dict) -> DeleteLinkInput:
    out: DeleteLinkInput = {}  # type: ignore[typeddict-item]
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError("DeleteLinkInput.identifier required")
    return out

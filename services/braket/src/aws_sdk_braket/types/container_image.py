"""Generated from Smithy shape ``com.amazonaws.braket#ContainerImage``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_braket.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_braket.types.uri


class ContainerImage(TypedDict):
    uri: "aws_sdk_braket.types.uri.Uri"
    """<p>The URI locating the container image.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContainerImage) -> dict:
    out: dict = {}
    out["uri"] = value["uri"]
    return out


def deserialize_json(data: dict) -> ContainerImage:
    out: ContainerImage = {}  # type: ignore[typeddict-item]
    if "uri" in data:
        out["uri"] = data["uri"]
    else:
        raise DeserializationError("ContainerImage.uri required")
    return out

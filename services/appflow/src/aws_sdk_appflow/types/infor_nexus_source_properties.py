"""Generated from Smithy shape ``com.amazonaws.appflow#InforNexusSourceProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.object


class InforNexusSourceProperties(TypedDict, closed=True):
    object: "aws_sdk_appflow.types.object.Object"
    """<p> The object specified in the Infor Nexus flow source. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InforNexusSourceProperties) -> dict:
    out: dict = {}
    out["object"] = value["object"]
    return out


def deserialize_json(data: dict) -> InforNexusSourceProperties:
    out: InforNexusSourceProperties = {}  # type: ignore[typeddict-item]
    if "object" in data:
        out["object"] = data["object"]
    else:
        raise DeserializationError("InforNexusSourceProperties.object required")
    return out

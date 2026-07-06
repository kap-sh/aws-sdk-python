"""Generated from Smithy shape ``com.amazonaws.appflow#PardotSourceProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.object


class PardotSourceProperties(TypedDict, closed=True):
    object: "aws_sdk_appflow.types.object.Object"
    """<p>The object specified in the Salesforce Pardot flow source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PardotSourceProperties) -> dict:
    out: dict = {}
    out["object"] = value["object"]
    return out


def deserialize_json(data: dict) -> PardotSourceProperties:
    out: PardotSourceProperties = {}  # type: ignore[typeddict-item]
    if "object" in data:
        out["object"] = data["object"]
    else:
        raise DeserializationError("PardotSourceProperties.object required")
    return out

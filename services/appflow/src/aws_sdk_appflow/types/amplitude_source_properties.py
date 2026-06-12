"""Generated from Smithy shape ``com.amazonaws.appflow#AmplitudeSourceProperties``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.object


class AmplitudeSourceProperties(TypedDict):
    object: "aws_sdk_appflow.types.object.Object"
    """<p> The object specified in the Amplitude flow source. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AmplitudeSourceProperties) -> dict:
    out: dict = {}
    out["object"] = value["object"]
    return out


def deserialize_json(data: dict) -> AmplitudeSourceProperties:
    out: AmplitudeSourceProperties = {}  # type: ignore[typeddict-item]
    if "object" in data:
        out["object"] = data["object"]
    else:
        raise DeserializationError("AmplitudeSourceProperties.object required")
    return out

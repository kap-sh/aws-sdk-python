"""Generated from Smithy shape ``com.amazonaws.appflow#MarketoSourceProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appflow.types.object


class MarketoSourceProperties(TypedDict, closed=True):
    object: "capo_appflow.types.object.Object"
    """<p> The object specified in the Marketo flow source. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MarketoSourceProperties) -> dict:
    out: dict = {}
    out["object"] = value["object"]
    return out


def deserialize_json(data: dict) -> MarketoSourceProperties:
    out: MarketoSourceProperties = {}  # type: ignore[typeddict-item]
    if "object" in data:
        out["object"] = data["object"]
    else:
        raise DeserializationError("MarketoSourceProperties.object required")
    return out

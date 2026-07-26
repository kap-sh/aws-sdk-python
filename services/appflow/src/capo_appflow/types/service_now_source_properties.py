"""Generated from Smithy shape ``com.amazonaws.appflow#ServiceNowSourceProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appflow.types.object


class ServiceNowSourceProperties(TypedDict, closed=True):
    object: "capo_appflow.types.object.Object"
    """<p> The object specified in the ServiceNow flow source. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceNowSourceProperties) -> dict:
    out: dict = {}
    out["object"] = value["object"]
    return out


def deserialize_json(data: dict) -> ServiceNowSourceProperties:
    out: ServiceNowSourceProperties = {}  # type: ignore[typeddict-item]
    if "object" in data:
        out["object"] = data["object"]
    else:
        raise DeserializationError("ServiceNowSourceProperties.object required")
    return out

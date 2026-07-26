"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ServiceNowSourceProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import capo_customer_profiles.types.object


class ServiceNowSourceProperties(TypedDict, closed=True):
    object: "capo_customer_profiles.types.object.Object"
    """<p>The object specified in the ServiceNow flow source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceNowSourceProperties) -> dict:
    out: dict = {}
    out["Object"] = value["object"]
    return out


def deserialize_json(data: dict) -> ServiceNowSourceProperties:
    out: ServiceNowSourceProperties = {}  # type: ignore[typeddict-item]
    if "Object" in data:
        out["object"] = data["Object"]
    else:
        raise DeserializationError("ServiceNowSourceProperties.object required")
    return out

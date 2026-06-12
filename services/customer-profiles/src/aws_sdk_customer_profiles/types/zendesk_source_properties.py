"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ZendeskSourceProperties``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.object


class ZendeskSourceProperties(TypedDict):
    object: "aws_sdk_customer_profiles.types.object.Object"
    """<p>The object specified in the Zendesk flow source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ZendeskSourceProperties) -> dict:
    out: dict = {}
    out["Object"] = value["object"]
    return out


def deserialize_json(data: dict) -> ZendeskSourceProperties:
    out: ZendeskSourceProperties = {}  # type: ignore[typeddict-item]
    if "Object" in data:
        out["object"] = data["Object"]
    else:
        raise DeserializationError("ZendeskSourceProperties.object required")
    return out

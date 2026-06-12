"""Generated from Smithy shape ``com.amazonaws.customerprofiles#PutProfileObjectRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.stringified_json
    import aws_sdk_customer_profiles.types.type_name


class PutProfileObjectRequest(TypedDict):
    object_type_name: "aws_sdk_customer_profiles.types.type_name.typeName"
    """<p>The name of the profile object type.</p>"""
    object: "aws_sdk_customer_profiles.types.stringified_json.stringifiedJson"
    """<p>A string that is serialized from a JSON object.</p>"""
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutProfileObjectRequest) -> dict:
    out: dict = {}
    out["ObjectTypeName"] = value["object_type_name"]
    out["Object"] = value["object"]
    return out


def deserialize_json(data: dict) -> PutProfileObjectRequest:
    out: PutProfileObjectRequest = {}  # type: ignore[typeddict-item]
    if "ObjectTypeName" in data:
        out["object_type_name"] = data["ObjectTypeName"]
    else:
        raise DeserializationError("PutProfileObjectRequest.object_type_name required")
    if "Object" in data:
        out["object"] = data["Object"]
    else:
        raise DeserializationError("PutProfileObjectRequest.object required")
    return out

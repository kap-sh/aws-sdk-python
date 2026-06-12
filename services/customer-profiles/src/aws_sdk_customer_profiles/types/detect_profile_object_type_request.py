"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DetectProfileObjectTypeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.objects


class DetectProfileObjectTypeRequest(TypedDict):
    objects: "aws_sdk_customer_profiles.types.objects.Objects"
    """<p>A string that is serialized from a JSON object.</p>"""
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetectProfileObjectTypeRequest) -> dict:
    out: dict = {}
    import aws_sdk_customer_profiles.types.objects

    out["Objects"] = aws_sdk_customer_profiles.types.objects.serialize_json(
        value["objects"]
    )
    return out


def deserialize_json(data: dict) -> DetectProfileObjectTypeRequest:
    out: DetectProfileObjectTypeRequest = {}  # type: ignore[typeddict-item]
    if "Objects" in data:
        import aws_sdk_customer_profiles.types.objects

        out["objects"] = aws_sdk_customer_profiles.types.objects.deserialize_json(
            data["Objects"]
        )
    else:
        raise DeserializationError("DetectProfileObjectTypeRequest.objects required")
    return out

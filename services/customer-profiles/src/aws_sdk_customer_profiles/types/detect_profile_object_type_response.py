"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DetectProfileObjectTypeResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.detected_profile_object_types


class DetectProfileObjectTypeResponse(TypedDict):
    detected_profile_object_types: NotRequired[
        "aws_sdk_customer_profiles.types.detected_profile_object_types.DetectedProfileObjectTypes"
    ]
    """<p>Detected <code>ProfileObjectType</code> mappings from given objects. A maximum of one mapping is supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetectProfileObjectTypeResponse) -> dict:
    out: dict = {}
    if "detected_profile_object_types" in value:
        import aws_sdk_customer_profiles.types.detected_profile_object_types

        out["DetectedProfileObjectTypes"] = (
            aws_sdk_customer_profiles.types.detected_profile_object_types.serialize_json(
                value["detected_profile_object_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> DetectProfileObjectTypeResponse:
    out: DetectProfileObjectTypeResponse = {}  # type: ignore[typeddict-item]
    if "DetectedProfileObjectTypes" in data:
        import aws_sdk_customer_profiles.types.detected_profile_object_types

        out["detected_profile_object_types"] = (
            aws_sdk_customer_profiles.types.detected_profile_object_types.deserialize_json(
                data["DetectedProfileObjectTypes"]
            )
        )
    return out

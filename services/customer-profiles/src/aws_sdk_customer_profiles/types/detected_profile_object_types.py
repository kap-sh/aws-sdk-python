"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DetectedProfileObjectTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.detected_profile_object_type

DetectedProfileObjectTypes: TypeAlias = list[
    "aws_sdk_customer_profiles.types.detected_profile_object_type.DetectedProfileObjectType"
]


# --- restJson1 ser/de ---
def serialize_json(value: DetectedProfileObjectTypes) -> list:
    import aws_sdk_customer_profiles.types.detected_profile_object_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_customer_profiles.types.detected_profile_object_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DetectedProfileObjectTypes:
    import aws_sdk_customer_profiles.types.detected_profile_object_type

    out: DetectedProfileObjectTypes = []
    for item in data:
        out.append(
            aws_sdk_customer_profiles.types.detected_profile_object_type.deserialize_json(
                item
            )
        )
    return out

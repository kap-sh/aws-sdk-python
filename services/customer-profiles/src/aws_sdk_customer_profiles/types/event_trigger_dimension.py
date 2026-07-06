"""Generated from Smithy shape ``com.amazonaws.customerprofiles#EventTriggerDimension``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.object_attributes


class EventTriggerDimension(TypedDict, closed=True):
    object_attributes: (
        "aws_sdk_customer_profiles.types.object_attributes.ObjectAttributes"
    )
    """<p>A list of object attributes to be evaluated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventTriggerDimension) -> dict:
    out: dict = {}
    import aws_sdk_customer_profiles.types.object_attributes

    out["ObjectAttributes"] = (
        aws_sdk_customer_profiles.types.object_attributes.serialize_json(
            value["object_attributes"]
        )
    )
    return out


def deserialize_json(data: dict) -> EventTriggerDimension:
    out: EventTriggerDimension = {}  # type: ignore[typeddict-item]
    if "ObjectAttributes" in data:
        import aws_sdk_customer_profiles.types.object_attributes

        out["object_attributes"] = (
            aws_sdk_customer_profiles.types.object_attributes.deserialize_json(
                data["ObjectAttributes"]
            )
        )
    else:
        raise DeserializationError("EventTriggerDimension.object_attributes required")
    return out

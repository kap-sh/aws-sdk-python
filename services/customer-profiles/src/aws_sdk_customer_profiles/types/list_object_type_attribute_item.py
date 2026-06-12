"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListObjectTypeAttributeItem``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.timestamp


class ListObjectTypeAttributeItem(TypedDict):
    attribute_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>Name of the attribute.</p>"""
    last_updated_at: "aws_sdk_customer_profiles.types.timestamp.timestamp"
    """<p>When the attribute was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListObjectTypeAttributeItem) -> dict:
    out: dict = {}
    out["AttributeName"] = value["attribute_name"]
    import aws_sdk_customer_profiles.types.timestamp

    out["LastUpdatedAt"] = aws_sdk_customer_profiles.types.timestamp.serialize_json(
        value["last_updated_at"]
    )
    return out


def deserialize_json(data: dict) -> ListObjectTypeAttributeItem:
    out: ListObjectTypeAttributeItem = {}  # type: ignore[typeddict-item]
    if "AttributeName" in data:
        out["attribute_name"] = data["AttributeName"]
    else:
        raise DeserializationError(
            "ListObjectTypeAttributeItem.attribute_name required"
        )
    if "LastUpdatedAt" in data:
        import aws_sdk_customer_profiles.types.timestamp

        out["last_updated_at"] = (
            aws_sdk_customer_profiles.types.timestamp.deserialize_json(
                data["LastUpdatedAt"]
            )
        )
    else:
        raise DeserializationError(
            "ListObjectTypeAttributeItem.last_updated_at required"
        )
    return out

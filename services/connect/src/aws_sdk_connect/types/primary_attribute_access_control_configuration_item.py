"""Generated from Smithy shape ``com.amazonaws.connect#PrimaryAttributeAccessControlConfigurationItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.primary_attribute_values_set


class PrimaryAttributeAccessControlConfigurationItem(TypedDict, closed=True):
    primary_attribute_values: NotRequired[
        "aws_sdk_connect.types.primary_attribute_values_set.PrimaryAttributeValuesSet"
    ]
    """<p>The item's primary attribute values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrimaryAttributeAccessControlConfigurationItem) -> dict:
    out: dict = {}
    if "primary_attribute_values" in value:
        import aws_sdk_connect.types.primary_attribute_values_set

        out["PrimaryAttributeValues"] = (
            aws_sdk_connect.types.primary_attribute_values_set.serialize_json(
                value["primary_attribute_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> PrimaryAttributeAccessControlConfigurationItem:
    out: PrimaryAttributeAccessControlConfigurationItem = {}  # type: ignore[typeddict-item]
    if "PrimaryAttributeValues" in data:
        import aws_sdk_connect.types.primary_attribute_values_set

        out["primary_attribute_values"] = (
            aws_sdk_connect.types.primary_attribute_values_set.deserialize_json(
                data["PrimaryAttributeValues"]
            )
        )
    return out

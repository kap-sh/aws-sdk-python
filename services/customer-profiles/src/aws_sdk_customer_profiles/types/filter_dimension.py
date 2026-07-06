"""Generated from Smithy shape ``com.amazonaws.customerprofiles#FilterDimension``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.attribute_map


class FilterDimension(TypedDict, closed=True):
    attributes: "aws_sdk_customer_profiles.types.attribute_map.AttributeMap"
    """<p>Is the attribute within the FilterDimension map</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterDimension) -> dict:
    out: dict = {}
    import aws_sdk_customer_profiles.types.attribute_map

    out["Attributes"] = aws_sdk_customer_profiles.types.attribute_map.serialize_json(
        value["attributes"]
    )
    return out


def deserialize_json(data: dict) -> FilterDimension:
    out: FilterDimension = {}  # type: ignore[typeddict-item]
    if "Attributes" in data:
        import aws_sdk_customer_profiles.types.attribute_map

        out["attributes"] = (
            aws_sdk_customer_profiles.types.attribute_map.deserialize_json(
                data["Attributes"]
            )
        )
    else:
        raise DeserializationError("FilterDimension.attributes required")
    return out

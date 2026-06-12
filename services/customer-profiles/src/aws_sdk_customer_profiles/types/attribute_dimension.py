"""Generated from Smithy shape ``com.amazonaws.customerprofiles#AttributeDimension``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.attribute_dimension_type
    import aws_sdk_customer_profiles.types.values


class AttributeDimension(TypedDict):
    dimension_type: "aws_sdk_customer_profiles.types.attribute_dimension_type.AttributeDimensionType"
    """<p>The action to segment with.</p>"""
    values: "aws_sdk_customer_profiles.types.values.Values"
    """<p>The values to apply the DimensionType on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttributeDimension) -> dict:
    out: dict = {}
    import aws_sdk_customer_profiles.types.attribute_dimension_type

    out["DimensionType"] = (
        aws_sdk_customer_profiles.types.attribute_dimension_type.serialize_json(
            value["dimension_type"]
        )
    )
    import aws_sdk_customer_profiles.types.values

    out["Values"] = aws_sdk_customer_profiles.types.values.serialize_json(
        value["values"]
    )
    return out


def deserialize_json(data: dict) -> AttributeDimension:
    out: AttributeDimension = {}  # type: ignore[typeddict-item]
    if "DimensionType" in data:
        import aws_sdk_customer_profiles.types.attribute_dimension_type

        out["dimension_type"] = (
            aws_sdk_customer_profiles.types.attribute_dimension_type.deserialize_json(
                data["DimensionType"]
            )
        )
    else:
        raise DeserializationError("AttributeDimension.dimension_type required")
    if "Values" in data:
        import aws_sdk_customer_profiles.types.values

        out["values"] = aws_sdk_customer_profiles.types.values.deserialize_json(
            data["Values"]
        )
    else:
        raise DeserializationError("AttributeDimension.values required")
    return out

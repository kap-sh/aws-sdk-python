"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CalculatedAttributeDimension``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.attribute_dimension_type
    import aws_sdk_customer_profiles.types.condition_overrides
    import aws_sdk_customer_profiles.types.values


class CalculatedAttributeDimension(TypedDict, closed=True):
    dimension_type: "aws_sdk_customer_profiles.types.attribute_dimension_type.AttributeDimensionType"
    """<p>The action to segment with.</p>"""
    values: "aws_sdk_customer_profiles.types.values.Values"
    """<p>The values to apply the DimensionType with.</p>"""
    condition_overrides: NotRequired[
        "aws_sdk_customer_profiles.types.condition_overrides.ConditionOverrides"
    ]
    """<p>Applies the given condition over the initial Calculated Attribute's definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CalculatedAttributeDimension) -> dict:
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
    if "condition_overrides" in value:
        import aws_sdk_customer_profiles.types.condition_overrides

        out["ConditionOverrides"] = (
            aws_sdk_customer_profiles.types.condition_overrides.serialize_json(
                value["condition_overrides"]
            )
        )
    return out


def deserialize_json(data: dict) -> CalculatedAttributeDimension:
    out: CalculatedAttributeDimension = {}  # type: ignore[typeddict-item]
    if "DimensionType" in data:
        import aws_sdk_customer_profiles.types.attribute_dimension_type

        out["dimension_type"] = (
            aws_sdk_customer_profiles.types.attribute_dimension_type.deserialize_json(
                data["DimensionType"]
            )
        )
    else:
        raise DeserializationError(
            "CalculatedAttributeDimension.dimension_type required"
        )
    if "Values" in data:
        import aws_sdk_customer_profiles.types.values

        out["values"] = aws_sdk_customer_profiles.types.values.deserialize_json(
            data["Values"]
        )
    else:
        raise DeserializationError("CalculatedAttributeDimension.values required")
    if "ConditionOverrides" in data:
        import aws_sdk_customer_profiles.types.condition_overrides

        out["condition_overrides"] = (
            aws_sdk_customer_profiles.types.condition_overrides.deserialize_json(
                data["ConditionOverrides"]
            )
        )
    return out

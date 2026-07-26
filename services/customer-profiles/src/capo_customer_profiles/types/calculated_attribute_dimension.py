"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CalculatedAttributeDimension``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import capo_customer_profiles.types.attribute_dimension_type
    import capo_customer_profiles.types.condition_overrides
    import capo_customer_profiles.types.values


class CalculatedAttributeDimension(TypedDict, closed=True):
    dimension_type: (
        "capo_customer_profiles.types.attribute_dimension_type.AttributeDimensionType"
    )
    """<p>The action to segment with.</p>"""
    values: "capo_customer_profiles.types.values.Values"
    """<p>The values to apply the DimensionType with.</p>"""
    condition_overrides: NotRequired[
        "capo_customer_profiles.types.condition_overrides.ConditionOverrides"
    ]
    """<p>Applies the given condition over the initial Calculated Attribute's definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CalculatedAttributeDimension) -> dict:
    out: dict = {}
    import capo_customer_profiles.types.attribute_dimension_type

    out["DimensionType"] = (
        capo_customer_profiles.types.attribute_dimension_type.serialize_json(
            value["dimension_type"]
        )
    )
    import capo_customer_profiles.types.values

    out["Values"] = capo_customer_profiles.types.values.serialize_json(value["values"])
    if "condition_overrides" in value:
        import capo_customer_profiles.types.condition_overrides

        out["ConditionOverrides"] = (
            capo_customer_profiles.types.condition_overrides.serialize_json(
                value["condition_overrides"]
            )
        )
    return out


def deserialize_json(data: dict) -> CalculatedAttributeDimension:
    out: CalculatedAttributeDimension = {}  # type: ignore[typeddict-item]
    if "DimensionType" in data:
        import capo_customer_profiles.types.attribute_dimension_type

        out["dimension_type"] = (
            capo_customer_profiles.types.attribute_dimension_type.deserialize_json(
                data["DimensionType"]
            )
        )
    else:
        raise DeserializationError(
            "CalculatedAttributeDimension.dimension_type required"
        )
    if "Values" in data:
        import capo_customer_profiles.types.values

        out["values"] = capo_customer_profiles.types.values.deserialize_json(
            data["Values"]
        )
    else:
        raise DeserializationError("CalculatedAttributeDimension.values required")
    if "ConditionOverrides" in data:
        import capo_customer_profiles.types.condition_overrides

        out["condition_overrides"] = (
            capo_customer_profiles.types.condition_overrides.deserialize_json(
                data["ConditionOverrides"]
            )
        )
    return out

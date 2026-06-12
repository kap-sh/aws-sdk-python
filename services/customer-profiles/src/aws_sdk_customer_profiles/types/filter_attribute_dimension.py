"""Generated from Smithy shape ``com.amazonaws.customerprofiles#FilterAttributeDimension``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.filter_dimension_type
    import aws_sdk_customer_profiles.types.value_list


class FilterAttributeDimension(TypedDict):
    dimension_type: (
        "aws_sdk_customer_profiles.types.filter_dimension_type.FilterDimensionType"
    )
    """<p>The action to filter with.</p>"""
    values: "aws_sdk_customer_profiles.types.value_list.ValueList"
    """<p>The values to apply the DimensionType on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterAttributeDimension) -> dict:
    out: dict = {}
    import aws_sdk_customer_profiles.types.filter_dimension_type

    out["DimensionType"] = (
        aws_sdk_customer_profiles.types.filter_dimension_type.serialize_json(
            value["dimension_type"]
        )
    )
    import aws_sdk_customer_profiles.types.value_list

    out["Values"] = aws_sdk_customer_profiles.types.value_list.serialize_json(
        value["values"]
    )
    return out


def deserialize_json(data: dict) -> FilterAttributeDimension:
    out: FilterAttributeDimension = {}  # type: ignore[typeddict-item]
    if "DimensionType" in data:
        import aws_sdk_customer_profiles.types.filter_dimension_type

        out["dimension_type"] = (
            aws_sdk_customer_profiles.types.filter_dimension_type.deserialize_json(
                data["DimensionType"]
            )
        )
    else:
        raise DeserializationError("FilterAttributeDimension.dimension_type required")
    if "Values" in data:
        import aws_sdk_customer_profiles.types.value_list

        out["values"] = aws_sdk_customer_profiles.types.value_list.deserialize_json(
            data["Values"]
        )
    else:
        raise DeserializationError("FilterAttributeDimension.values required")
    return out

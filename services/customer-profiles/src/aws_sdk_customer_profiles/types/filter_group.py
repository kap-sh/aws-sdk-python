"""Generated from Smithy shape ``com.amazonaws.customerprofiles#FilterGroup``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.filter_dimension_list
    import aws_sdk_customer_profiles.types.type


class FilterGroup(TypedDict):
    type: "aws_sdk_customer_profiles.types.type.Type"
    """<p>The type of logical relationship between the dimensions of the Filter group.</p>"""
    dimensions: (
        "aws_sdk_customer_profiles.types.filter_dimension_list.FilterDimensionList"
    )
    """<p>Object that holds the attributes to filter on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterGroup) -> dict:
    out: dict = {}
    import aws_sdk_customer_profiles.types.type

    out["Type"] = aws_sdk_customer_profiles.types.type.serialize_json(value["type"])
    import aws_sdk_customer_profiles.types.filter_dimension_list

    out["Dimensions"] = (
        aws_sdk_customer_profiles.types.filter_dimension_list.serialize_json(
            value["dimensions"]
        )
    )
    return out


def deserialize_json(data: dict) -> FilterGroup:
    out: FilterGroup = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_customer_profiles.types.type

        out["type"] = aws_sdk_customer_profiles.types.type.deserialize_json(
            data["Type"]
        )
    else:
        raise DeserializationError("FilterGroup.type required")
    if "Dimensions" in data:
        import aws_sdk_customer_profiles.types.filter_dimension_list

        out["dimensions"] = (
            aws_sdk_customer_profiles.types.filter_dimension_list.deserialize_json(
                data["Dimensions"]
            )
        )
    else:
        raise DeserializationError("FilterGroup.dimensions required")
    return out

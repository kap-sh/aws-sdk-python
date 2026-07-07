"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ExtraLengthValueProfileDimension``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.extra_length_values
    import aws_sdk_customer_profiles.types.string_dimension_type


class ExtraLengthValueProfileDimension(TypedDict, closed=True):
    dimension_type: (
        "aws_sdk_customer_profiles.types.string_dimension_type.StringDimensionType"
    )
    """<p>The action to segment with.</p>"""
    values: "aws_sdk_customer_profiles.types.extra_length_values.ExtraLengthValues"
    """<p>The values to apply the DimensionType on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExtraLengthValueProfileDimension) -> dict:
    out: dict = {}
    import aws_sdk_customer_profiles.types.string_dimension_type

    out["DimensionType"] = (
        aws_sdk_customer_profiles.types.string_dimension_type.serialize_json(
            value["dimension_type"]
        )
    )
    import aws_sdk_customer_profiles.types.extra_length_values

    out["Values"] = aws_sdk_customer_profiles.types.extra_length_values.serialize_json(
        value["values"]
    )
    return out


def deserialize_json(data: dict) -> ExtraLengthValueProfileDimension:
    out: ExtraLengthValueProfileDimension = {}  # type: ignore[typeddict-item]
    if "DimensionType" in data:
        import aws_sdk_customer_profiles.types.string_dimension_type

        out["dimension_type"] = (
            aws_sdk_customer_profiles.types.string_dimension_type.deserialize_json(
                data["DimensionType"]
            )
        )
    else:
        raise DeserializationError(
            "ExtraLengthValueProfileDimension.dimension_type required"
        )
    if "Values" in data:
        import aws_sdk_customer_profiles.types.extra_length_values

        out["values"] = (
            aws_sdk_customer_profiles.types.extra_length_values.deserialize_json(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("ExtraLengthValueProfileDimension.values required")
    return out

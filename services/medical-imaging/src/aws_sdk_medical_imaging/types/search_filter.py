"""Generated from Smithy shape ``com.amazonaws.medicalimaging#SearchFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_medical_imaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_medical_imaging.types.operator
    import aws_sdk_medical_imaging.types.search_by_attribute_values


class SearchFilter(TypedDict, closed=True):
    values: "aws_sdk_medical_imaging.types.search_by_attribute_values.SearchByAttributeValues"
    """<p>The search filter values.</p>"""
    operator: "aws_sdk_medical_imaging.types.operator.Operator"
    """<p>The search filter operator for <code>imageSetDateTime</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchFilter) -> dict:
    out: dict = {}
    import aws_sdk_medical_imaging.types.search_by_attribute_values

    out["values"] = (
        aws_sdk_medical_imaging.types.search_by_attribute_values.serialize_json(
            value["values"]
        )
    )
    import aws_sdk_medical_imaging.types.operator

    out["operator"] = aws_sdk_medical_imaging.types.operator.serialize_json(
        value["operator"]
    )
    return out


def deserialize_json(data: dict) -> SearchFilter:
    out: SearchFilter = {}  # type: ignore[typeddict-item]
    if "values" in data:
        import aws_sdk_medical_imaging.types.search_by_attribute_values

        out["values"] = (
            aws_sdk_medical_imaging.types.search_by_attribute_values.deserialize_json(
                data["values"]
            )
        )
    else:
        raise DeserializationError("SearchFilter.values required")
    if "operator" in data:
        import aws_sdk_medical_imaging.types.operator

        out["operator"] = aws_sdk_medical_imaging.types.operator.deserialize_json(
            data["operator"]
        )
    else:
        raise DeserializationError("SearchFilter.operator required")
    return out

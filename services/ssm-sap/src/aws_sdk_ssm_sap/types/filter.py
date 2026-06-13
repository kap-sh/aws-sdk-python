"""Generated from Smithy shape ``com.amazonaws.ssmsap#Filter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm_sap.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.filter_name
    import aws_sdk_ssm_sap.types.filter_operator
    import aws_sdk_ssm_sap.types.filter_value


class Filter(TypedDict):
    name: "aws_sdk_ssm_sap.types.filter_name.FilterName"
    """<p>The name of the filter. Filter names are case-sensitive. </p>"""
    value: "aws_sdk_ssm_sap.types.filter_value.FilterValue"
    """<p>The filter values. Filter values are case-sensitive. If you specify multiple values for a filter, the values are joined with an OR, and the request returns all results that match any of the specified values</p>"""
    operator: "aws_sdk_ssm_sap.types.filter_operator.FilterOperator"
    """<p>The operator for the filter. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Filter) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Value"] = value["value"]
    import aws_sdk_ssm_sap.types.filter_operator

    out["Operator"] = aws_sdk_ssm_sap.types.filter_operator.serialize_json(
        value["operator"]
    )
    return out


def deserialize_json(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("Filter.name required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("Filter.value required")
    if "Operator" in data:
        import aws_sdk_ssm_sap.types.filter_operator

        out["operator"] = aws_sdk_ssm_sap.types.filter_operator.deserialize_json(
            data["Operator"]
        )
    else:
        raise DeserializationError("Filter.operator required")
    return out

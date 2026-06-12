"""Generated from Smithy shape ``com.amazonaws.costexplorer#TotalImpactFilter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.generic_double
    import aws_sdk_cost_explorer.types.numeric_operator


class TotalImpactFilter(TypedDict):
    numeric_operator: "aws_sdk_cost_explorer.types.numeric_operator.NumericOperator"
    """<p>The comparing value that's used in the filter. </p>"""
    start_value: "aws_sdk_cost_explorer.types.generic_double.GenericDouble"
    """<p>The lower bound dollar value that's used in the filter. </p>"""
    end_value: "aws_sdk_cost_explorer.types.generic_double.GenericDouble"
    """<p>The upper bound dollar value that's used in the filter. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TotalImpactFilter) -> dict:
    out: dict = {}
    import aws_sdk_cost_explorer.types.numeric_operator

    out["NumericOperator"] = (
        aws_sdk_cost_explorer.types.numeric_operator.serialize_aws_json_1_1(
            value["numeric_operator"]
        )
    )
    out["StartValue"] = value.get("start_value", 0)
    out["EndValue"] = value.get("end_value", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> TotalImpactFilter:
    out: TotalImpactFilter = {}  # type: ignore[typeddict-item]
    if "NumericOperator" in data:
        import aws_sdk_cost_explorer.types.numeric_operator

        out["numeric_operator"] = (
            aws_sdk_cost_explorer.types.numeric_operator.deserialize_aws_json_1_1(
                data["NumericOperator"]
            )
        )
    else:
        raise DeserializationError("TotalImpactFilter.numeric_operator required")
    if "StartValue" in data:
        out["start_value"] = data["StartValue"]
    else:
        out["start_value"] = 0
    if "EndValue" in data:
        out["end_value"] = data["EndValue"]
    else:
        out["end_value"] = 0
    return out

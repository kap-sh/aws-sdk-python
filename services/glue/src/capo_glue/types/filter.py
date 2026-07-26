"""Generated from Smithy shape ``com.amazonaws.glue#Filter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.filter_expressions
    import capo_glue.types.filter_logical_operator
    import capo_glue.types.node_name
    import capo_glue.types.one_input


class Filter(TypedDict, closed=True):
    name: "capo_glue.types.node_name.NodeName"
    """<p>The name of the transform node.</p>"""
    inputs: "capo_glue.types.one_input.OneInput"
    """<p>The data inputs identified by their node names.</p>"""
    logical_operator: "capo_glue.types.filter_logical_operator.FilterLogicalOperator"
    """<p>The operator used to filter rows by comparing the key value to a specified value.</p>"""
    filters: "capo_glue.types.filter_expressions.FilterExpressions"
    """<p>Specifies a filter expression.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Filter) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_glue.types.one_input

    out["Inputs"] = capo_glue.types.one_input.serialize_aws_json_1_1(value["inputs"])
    import capo_glue.types.filter_logical_operator

    out["LogicalOperator"] = (
        capo_glue.types.filter_logical_operator.serialize_aws_json_1_1(
            value["logical_operator"]
        )
    )
    import capo_glue.types.filter_expressions

    out["Filters"] = capo_glue.types.filter_expressions.serialize_aws_json_1_1(
        value["filters"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("Filter.name required")
    if "Inputs" in data:
        import capo_glue.types.one_input

        out["inputs"] = capo_glue.types.one_input.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    else:
        raise DeserializationError("Filter.inputs required")
    if "LogicalOperator" in data:
        import capo_glue.types.filter_logical_operator

        out["logical_operator"] = (
            capo_glue.types.filter_logical_operator.deserialize_aws_json_1_1(
                data["LogicalOperator"]
            )
        )
    else:
        raise DeserializationError("Filter.logical_operator required")
    if "Filters" in data:
        import capo_glue.types.filter_expressions

        out["filters"] = capo_glue.types.filter_expressions.deserialize_aws_json_1_1(
            data["Filters"]
        )
    else:
        raise DeserializationError("Filter.filters required")
    return out

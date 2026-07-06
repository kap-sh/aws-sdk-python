"""Generated from Smithy shape ``com.amazonaws.glue#Union``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.node_name
    import aws_sdk_glue.types.two_inputs
    import aws_sdk_glue.types.union_type


class Union(TypedDict, closed=True):
    name: "aws_sdk_glue.types.node_name.NodeName"
    """<p>The name of the transform node.</p>"""
    inputs: "aws_sdk_glue.types.two_inputs.TwoInputs"
    """<p>The node ID inputs to the transform.</p>"""
    union_type: "aws_sdk_glue.types.union_type.UnionType"
    """<p>Indicates the type of Union transform. </p> <p>Specify <code>ALL</code> to join all rows from data sources to the resulting DynamicFrame. The resulting union does not remove duplicate rows.</p> <p>Specify <code>DISTINCT</code> to remove duplicate rows in the resulting DynamicFrame.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Union) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_glue.types.two_inputs

    out["Inputs"] = aws_sdk_glue.types.two_inputs.serialize_aws_json_1_1(
        value["inputs"]
    )
    import aws_sdk_glue.types.union_type

    out["UnionType"] = aws_sdk_glue.types.union_type.serialize_aws_json_1_1(
        value["union_type"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Union:
    out: Union = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("Union.name required")
    if "Inputs" in data:
        import aws_sdk_glue.types.two_inputs

        out["inputs"] = aws_sdk_glue.types.two_inputs.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    else:
        raise DeserializationError("Union.inputs required")
    if "UnionType" in data:
        import aws_sdk_glue.types.union_type

        out["union_type"] = aws_sdk_glue.types.union_type.deserialize_aws_json_1_1(
            data["UnionType"]
        )
    else:
        raise DeserializationError("Union.union_type required")
    return out

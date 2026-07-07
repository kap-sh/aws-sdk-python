"""Generated from Smithy shape ``com.amazonaws.glue#Join``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.join_columns
    import aws_sdk_glue.types.join_type
    import aws_sdk_glue.types.node_name
    import aws_sdk_glue.types.two_inputs


class Join(TypedDict, closed=True):
    name: "aws_sdk_glue.types.node_name.NodeName"
    """<p>The name of the transform node.</p>"""
    inputs: "aws_sdk_glue.types.two_inputs.TwoInputs"
    """<p>The data inputs identified by their node names.</p>"""
    join_type: "aws_sdk_glue.types.join_type.JoinType"
    """<p>Specifies the type of join to be performed on the datasets.</p>"""
    columns: "aws_sdk_glue.types.join_columns.JoinColumns"
    """<p>A list of the two columns to be joined.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Join) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_glue.types.two_inputs

    out["Inputs"] = aws_sdk_glue.types.two_inputs.serialize_aws_json_1_1(
        value["inputs"]
    )
    import aws_sdk_glue.types.join_type

    out["JoinType"] = aws_sdk_glue.types.join_type.serialize_aws_json_1_1(
        value["join_type"]
    )
    import aws_sdk_glue.types.join_columns

    out["Columns"] = aws_sdk_glue.types.join_columns.serialize_aws_json_1_1(
        value["columns"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Join:
    out: Join = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("Join.name required")
    if "Inputs" in data:
        import aws_sdk_glue.types.two_inputs

        out["inputs"] = aws_sdk_glue.types.two_inputs.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    else:
        raise DeserializationError("Join.inputs required")
    if "JoinType" in data:
        import aws_sdk_glue.types.join_type

        out["join_type"] = aws_sdk_glue.types.join_type.deserialize_aws_json_1_1(
            data["JoinType"]
        )
    else:
        raise DeserializationError("Join.join_type required")
    if "Columns" in data:
        import aws_sdk_glue.types.join_columns

        out["columns"] = aws_sdk_glue.types.join_columns.deserialize_aws_json_1_1(
            data["Columns"]
        )
    else:
        raise DeserializationError("Join.columns required")
    return out

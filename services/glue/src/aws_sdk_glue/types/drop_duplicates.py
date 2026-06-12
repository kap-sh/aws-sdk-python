"""Generated from Smithy shape ``com.amazonaws.glue#DropDuplicates``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.limited_path_list
    import aws_sdk_glue.types.node_name
    import aws_sdk_glue.types.one_input


class DropDuplicates(TypedDict):
    name: "aws_sdk_glue.types.node_name.NodeName"
    """<p>The name of the transform node.</p>"""
    inputs: "aws_sdk_glue.types.one_input.OneInput"
    """<p>The data inputs identified by their node names.</p>"""
    columns: NotRequired["aws_sdk_glue.types.limited_path_list.LimitedPathList"]
    """<p>The name of the columns to be merged or removed if repeating.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DropDuplicates) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_glue.types.one_input

    out["Inputs"] = aws_sdk_glue.types.one_input.serialize_aws_json_1_1(value["inputs"])
    if "columns" in value:
        import aws_sdk_glue.types.limited_path_list

        out["Columns"] = aws_sdk_glue.types.limited_path_list.serialize_aws_json_1_1(
            value["columns"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DropDuplicates:
    out: DropDuplicates = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DropDuplicates.name required")
    if "Inputs" in data:
        import aws_sdk_glue.types.one_input

        out["inputs"] = aws_sdk_glue.types.one_input.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    else:
        raise DeserializationError("DropDuplicates.inputs required")
    if "Columns" in data:
        import aws_sdk_glue.types.limited_path_list

        out["columns"] = aws_sdk_glue.types.limited_path_list.deserialize_aws_json_1_1(
            data["Columns"]
        )
    return out

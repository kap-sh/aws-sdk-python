"""Generated from Smithy shape ``com.amazonaws.glue#SplitFields``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.glue_studio_path_list
    import aws_sdk_glue.types.node_name
    import aws_sdk_glue.types.one_input


class SplitFields(TypedDict, closed=True):
    name: "aws_sdk_glue.types.node_name.NodeName"
    """<p>The name of the transform node.</p>"""
    inputs: "aws_sdk_glue.types.one_input.OneInput"
    """<p>The data inputs identified by their node names.</p>"""
    paths: "aws_sdk_glue.types.glue_studio_path_list.GlueStudioPathList"
    """<p>A JSON path to a variable in the data structure.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SplitFields) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_glue.types.one_input

    out["Inputs"] = aws_sdk_glue.types.one_input.serialize_aws_json_1_1(value["inputs"])
    import aws_sdk_glue.types.glue_studio_path_list

    out["Paths"] = aws_sdk_glue.types.glue_studio_path_list.serialize_aws_json_1_1(
        value["paths"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SplitFields:
    out: SplitFields = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("SplitFields.name required")
    if "Inputs" in data:
        import aws_sdk_glue.types.one_input

        out["inputs"] = aws_sdk_glue.types.one_input.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    else:
        raise DeserializationError("SplitFields.inputs required")
    if "Paths" in data:
        import aws_sdk_glue.types.glue_studio_path_list

        out["paths"] = (
            aws_sdk_glue.types.glue_studio_path_list.deserialize_aws_json_1_1(
                data["Paths"]
            )
        )
    else:
        raise DeserializationError("SplitFields.paths required")
    return out

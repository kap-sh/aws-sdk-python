"""Generated from Smithy shape ``com.amazonaws.glue#DropFields``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.glue_studio_path_list
    import capo_glue.types.node_name
    import capo_glue.types.one_input


class DropFields(TypedDict, closed=True):
    name: "capo_glue.types.node_name.NodeName"
    """<p>The name of the transform node.</p>"""
    inputs: "capo_glue.types.one_input.OneInput"
    """<p>The data inputs identified by their node names.</p>"""
    paths: "capo_glue.types.glue_studio_path_list.GlueStudioPathList"
    """<p>A JSON path to a variable in the data structure.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DropFields) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_glue.types.one_input

    out["Inputs"] = capo_glue.types.one_input.serialize_aws_json_1_1(value["inputs"])
    import capo_glue.types.glue_studio_path_list

    out["Paths"] = capo_glue.types.glue_studio_path_list.serialize_aws_json_1_1(
        value["paths"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DropFields:
    out: DropFields = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DropFields.name required")
    if "Inputs" in data:
        import capo_glue.types.one_input

        out["inputs"] = capo_glue.types.one_input.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    else:
        raise DeserializationError("DropFields.inputs required")
    if "Paths" in data:
        import capo_glue.types.glue_studio_path_list

        out["paths"] = capo_glue.types.glue_studio_path_list.deserialize_aws_json_1_1(
            data["Paths"]
        )
    else:
        raise DeserializationError("DropFields.paths required")
    return out

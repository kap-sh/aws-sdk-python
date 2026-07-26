"""Generated from Smithy shape ``com.amazonaws.glue#Merge``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.glue_studio_path_list
    import capo_glue.types.node_id
    import capo_glue.types.node_name
    import capo_glue.types.two_inputs


class Merge(TypedDict, closed=True):
    name: "capo_glue.types.node_name.NodeName"
    """<p>The name of the transform node.</p>"""
    inputs: "capo_glue.types.two_inputs.TwoInputs"
    """<p>The data inputs identified by their node names.</p>"""
    source: "capo_glue.types.node_id.NodeId"
    """<p>The source <code>DynamicFrame</code> that will be merged with a staging <code>DynamicFrame</code>.</p>"""
    primary_keys: "capo_glue.types.glue_studio_path_list.GlueStudioPathList"
    """<p>The list of primary key fields to match records from the source and staging dynamic frames.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Merge) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_glue.types.two_inputs

    out["Inputs"] = capo_glue.types.two_inputs.serialize_aws_json_1_1(value["inputs"])
    out["Source"] = value["source"]
    import capo_glue.types.glue_studio_path_list

    out["PrimaryKeys"] = capo_glue.types.glue_studio_path_list.serialize_aws_json_1_1(
        value["primary_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Merge:
    out: Merge = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("Merge.name required")
    if "Inputs" in data:
        import capo_glue.types.two_inputs

        out["inputs"] = capo_glue.types.two_inputs.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    else:
        raise DeserializationError("Merge.inputs required")
    if "Source" in data:
        out["source"] = data["Source"]
    else:
        raise DeserializationError("Merge.source required")
    if "PrimaryKeys" in data:
        import capo_glue.types.glue_studio_path_list

        out["primary_keys"] = (
            capo_glue.types.glue_studio_path_list.deserialize_aws_json_1_1(
                data["PrimaryKeys"]
            )
        )
    else:
        raise DeserializationError("Merge.primary_keys required")
    return out

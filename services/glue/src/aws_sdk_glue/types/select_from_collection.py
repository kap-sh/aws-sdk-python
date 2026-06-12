"""Generated from Smithy shape ``com.amazonaws.glue#SelectFromCollection``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.node_name
    import aws_sdk_glue.types.non_negative_int
    import aws_sdk_glue.types.one_input


class SelectFromCollection(TypedDict):
    name: "aws_sdk_glue.types.node_name.NodeName"
    """<p>The name of the transform node.</p>"""
    inputs: "aws_sdk_glue.types.one_input.OneInput"
    """<p>The data inputs identified by their node names.</p>"""
    index: "aws_sdk_glue.types.non_negative_int.NonNegativeInt"
    """<p>The index for the DynamicFrame to be selected.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SelectFromCollection) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_glue.types.one_input

    out["Inputs"] = aws_sdk_glue.types.one_input.serialize_aws_json_1_1(value["inputs"])
    out["Index"] = value.get("index", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> SelectFromCollection:
    out: SelectFromCollection = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("SelectFromCollection.name required")
    if "Inputs" in data:
        import aws_sdk_glue.types.one_input

        out["inputs"] = aws_sdk_glue.types.one_input.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    else:
        raise DeserializationError("SelectFromCollection.inputs required")
    if "Index" in data:
        out["index"] = data["Index"]
    else:
        out["index"] = 0
    return out

"""Generated from Smithy shape ``com.amazonaws.glue#DropNullFields``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.node_name
    import aws_sdk_glue.types.null_check_box_list
    import aws_sdk_glue.types.null_value_fields
    import aws_sdk_glue.types.one_input


class DropNullFields(TypedDict):
    name: "aws_sdk_glue.types.node_name.NodeName"
    """<p>The name of the transform node.</p>"""
    inputs: "aws_sdk_glue.types.one_input.OneInput"
    """<p>The data inputs identified by their node names.</p>"""
    null_check_box_list: NotRequired[
        "aws_sdk_glue.types.null_check_box_list.NullCheckBoxList"
    ]
    """<p>A structure that represents whether certain values are recognized as null values for removal.</p>"""
    null_text_list: NotRequired["aws_sdk_glue.types.null_value_fields.NullValueFields"]
    """<p>A structure that specifies a list of NullValueField structures that represent a custom null value such as zero or other value being used as a null placeholder unique to the dataset.</p> <p>The <code>DropNullFields</code> transform removes custom null values only if both the value of the null placeholder and the datatype match the data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DropNullFields) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_glue.types.one_input

    out["Inputs"] = aws_sdk_glue.types.one_input.serialize_aws_json_1_1(value["inputs"])
    if "null_check_box_list" in value:
        import aws_sdk_glue.types.null_check_box_list

        out["NullCheckBoxList"] = (
            aws_sdk_glue.types.null_check_box_list.serialize_aws_json_1_1(
                value["null_check_box_list"]
            )
        )
    if "null_text_list" in value:
        import aws_sdk_glue.types.null_value_fields

        out["NullTextList"] = (
            aws_sdk_glue.types.null_value_fields.serialize_aws_json_1_1(
                value["null_text_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DropNullFields:
    out: DropNullFields = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DropNullFields.name required")
    if "Inputs" in data:
        import aws_sdk_glue.types.one_input

        out["inputs"] = aws_sdk_glue.types.one_input.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    else:
        raise DeserializationError("DropNullFields.inputs required")
    if "NullCheckBoxList" in data:
        import aws_sdk_glue.types.null_check_box_list

        out["null_check_box_list"] = (
            aws_sdk_glue.types.null_check_box_list.deserialize_aws_json_1_1(
                data["NullCheckBoxList"]
            )
        )
    if "NullTextList" in data:
        import aws_sdk_glue.types.null_value_fields

        out["null_text_list"] = (
            aws_sdk_glue.types.null_value_fields.deserialize_aws_json_1_1(
                data["NullTextList"]
            )
        )
    return out

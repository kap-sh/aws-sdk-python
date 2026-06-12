"""Generated from Smithy shape ``com.amazonaws.glue#RenameField``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.enclosed_in_string_properties
    import aws_sdk_glue.types.node_name
    import aws_sdk_glue.types.one_input


class RenameField(TypedDict):
    name: "aws_sdk_glue.types.node_name.NodeName"
    """<p>The name of the transform node.</p>"""
    inputs: "aws_sdk_glue.types.one_input.OneInput"
    """<p>The data inputs identified by their node names.</p>"""
    source_path: (
        "aws_sdk_glue.types.enclosed_in_string_properties.EnclosedInStringProperties"
    )
    """<p>A JSON path to a variable in the data structure for the source data.</p>"""
    target_path: (
        "aws_sdk_glue.types.enclosed_in_string_properties.EnclosedInStringProperties"
    )
    """<p>A JSON path to a variable in the data structure for the target data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RenameField) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_glue.types.one_input

    out["Inputs"] = aws_sdk_glue.types.one_input.serialize_aws_json_1_1(value["inputs"])
    import aws_sdk_glue.types.enclosed_in_string_properties

    out["SourcePath"] = (
        aws_sdk_glue.types.enclosed_in_string_properties.serialize_aws_json_1_1(
            value["source_path"]
        )
    )
    import aws_sdk_glue.types.enclosed_in_string_properties

    out["TargetPath"] = (
        aws_sdk_glue.types.enclosed_in_string_properties.serialize_aws_json_1_1(
            value["target_path"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RenameField:
    out: RenameField = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("RenameField.name required")
    if "Inputs" in data:
        import aws_sdk_glue.types.one_input

        out["inputs"] = aws_sdk_glue.types.one_input.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    else:
        raise DeserializationError("RenameField.inputs required")
    if "SourcePath" in data:
        import aws_sdk_glue.types.enclosed_in_string_properties

        out["source_path"] = (
            aws_sdk_glue.types.enclosed_in_string_properties.deserialize_aws_json_1_1(
                data["SourcePath"]
            )
        )
    else:
        raise DeserializationError("RenameField.source_path required")
    if "TargetPath" in data:
        import aws_sdk_glue.types.enclosed_in_string_properties

        out["target_path"] = (
            aws_sdk_glue.types.enclosed_in_string_properties.deserialize_aws_json_1_1(
                data["TargetPath"]
            )
        )
    else:
        raise DeserializationError("RenameField.target_path required")
    return out

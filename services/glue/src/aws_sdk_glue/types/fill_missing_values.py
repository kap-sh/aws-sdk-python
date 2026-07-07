"""Generated from Smithy shape ``com.amazonaws.glue#FillMissingValues``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.enclosed_in_string_property
    import aws_sdk_glue.types.node_name
    import aws_sdk_glue.types.one_input


class FillMissingValues(TypedDict, closed=True):
    name: "aws_sdk_glue.types.node_name.NodeName"
    """<p>The name of the transform node.</p>"""
    inputs: "aws_sdk_glue.types.one_input.OneInput"
    """<p>The data inputs identified by their node names.</p>"""
    imputed_path: (
        "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    )
    """<p>A JSON path to a variable in the data structure for the dataset that is imputed.</p>"""
    filled_path: NotRequired[
        "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>A JSON path to a variable in the data structure for the dataset that is filled.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FillMissingValues) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_glue.types.one_input

    out["Inputs"] = aws_sdk_glue.types.one_input.serialize_aws_json_1_1(value["inputs"])
    out["ImputedPath"] = value["imputed_path"]
    if "filled_path" in value:
        out["FilledPath"] = value["filled_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FillMissingValues:
    out: FillMissingValues = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("FillMissingValues.name required")
    if "Inputs" in data:
        import aws_sdk_glue.types.one_input

        out["inputs"] = aws_sdk_glue.types.one_input.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    else:
        raise DeserializationError("FillMissingValues.inputs required")
    if "ImputedPath" in data:
        out["imputed_path"] = data["ImputedPath"]
    else:
        raise DeserializationError("FillMissingValues.imputed_path required")
    if "FilledPath" in data:
        out["filled_path"] = data["FilledPath"]
    return out

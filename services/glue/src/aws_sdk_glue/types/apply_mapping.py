"""Generated from Smithy shape ``com.amazonaws.glue#ApplyMapping``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.mappings
    import aws_sdk_glue.types.node_name
    import aws_sdk_glue.types.one_input


class ApplyMapping(TypedDict):
    name: "aws_sdk_glue.types.node_name.NodeName"
    """<p>The name of the transform node.</p>"""
    inputs: "aws_sdk_glue.types.one_input.OneInput"
    """<p>The data inputs identified by their node names.</p>"""
    mapping: "aws_sdk_glue.types.mappings.Mappings"
    """<p>Specifies the mapping of data property keys in the data source to data property keys in the data target.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplyMapping) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_glue.types.one_input

    out["Inputs"] = aws_sdk_glue.types.one_input.serialize_aws_json_1_1(value["inputs"])
    import aws_sdk_glue.types.mappings

    out["Mapping"] = aws_sdk_glue.types.mappings.serialize_aws_json_1_1(
        value["mapping"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplyMapping:
    out: ApplyMapping = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("ApplyMapping.name required")
    if "Inputs" in data:
        import aws_sdk_glue.types.one_input

        out["inputs"] = aws_sdk_glue.types.one_input.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    else:
        raise DeserializationError("ApplyMapping.inputs required")
    if "Mapping" in data:
        import aws_sdk_glue.types.mappings

        out["mapping"] = aws_sdk_glue.types.mappings.deserialize_aws_json_1_1(
            data["Mapping"]
        )
    else:
        raise DeserializationError("ApplyMapping.mapping required")
    return out

"""Generated from Smithy shape ``com.amazonaws.entityresolution#IdNamespaceInputSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_entityresolution.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.entity_name
    import aws_sdk_entityresolution.types.input_source_arn


class IdNamespaceInputSource(TypedDict, closed=True):
    input_source_arn: "aws_sdk_entityresolution.types.input_source_arn.InputSourceARN"
    """<p>An Glue table Amazon Resource Name (ARN) or a matching workflow ARN for the input source table.</p>"""
    schema_name: NotRequired["aws_sdk_entityresolution.types.entity_name.EntityName"]
    """<p>The name of the schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdNamespaceInputSource) -> dict:
    out: dict = {}
    out["inputSourceARN"] = value["input_source_arn"]
    if "schema_name" in value:
        out["schemaName"] = value["schema_name"]
    return out


def deserialize_json(data: dict) -> IdNamespaceInputSource:
    out: IdNamespaceInputSource = {}  # type: ignore[typeddict-item]
    if "inputSourceARN" in data:
        out["input_source_arn"] = data["inputSourceARN"]
    else:
        raise DeserializationError("IdNamespaceInputSource.input_source_arn required")
    if "schemaName" in data:
        out["schema_name"] = data["schemaName"]
    return out

"""Generated from Smithy shape ``com.amazonaws.firehose#SchemaEvolutionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_firehose.types.boolean_object


class SchemaEvolutionConfiguration(TypedDict, closed=True):
    enabled: "aws_sdk_firehose.types.boolean_object.BooleanObject"
    """<p> Specify whether you want to enable schema evolution. </p> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SchemaEvolutionConfiguration) -> dict:
    out: dict = {}
    out["Enabled"] = value["enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SchemaEvolutionConfiguration:
    out: SchemaEvolutionConfiguration = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    else:
        raise DeserializationError("SchemaEvolutionConfiguration.enabled required")
    return out

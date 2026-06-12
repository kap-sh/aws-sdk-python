"""Generated from Smithy shape ``com.amazonaws.datapipeline#PipelineObject``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_data_pipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_data_pipeline.types.field_list
    import aws_sdk_data_pipeline.types.id


class PipelineObject(TypedDict):
    id: "aws_sdk_data_pipeline.types.id.id"
    """<p>The ID of the object.</p>"""
    name: "aws_sdk_data_pipeline.types.id.id"
    """<p>The name of the object.</p>"""
    fields: "aws_sdk_data_pipeline.types.field_list.fieldList"
    """<p>Key-value pairs that define the properties of the object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineObject) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    import aws_sdk_data_pipeline.types.field_list

    out["fields"] = aws_sdk_data_pipeline.types.field_list.serialize_aws_json_1_1(
        value["fields"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PipelineObject:
    out: PipelineObject = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("PipelineObject.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("PipelineObject.name required")
    if "fields" in data:
        import aws_sdk_data_pipeline.types.field_list

        out["fields"] = aws_sdk_data_pipeline.types.field_list.deserialize_aws_json_1_1(
            data["fields"]
        )
    else:
        raise DeserializationError("PipelineObject.fields required")
    return out

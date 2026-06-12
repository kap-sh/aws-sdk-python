"""Generated from Smithy shape ``com.amazonaws.datapipeline#Selector``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_data_pipeline.types.operator
    import aws_sdk_data_pipeline.types.string


class Selector(TypedDict):
    field_name: NotRequired["aws_sdk_data_pipeline.types.string.string"]
    """<p>The name of the field that the operator will be applied to. The field name is the \"key\" portion of the field definition in the pipeline definition syntax that is used by the AWS Data Pipeline API. If the field is not set on the object, the condition fails.</p>"""
    operator: NotRequired["aws_sdk_data_pipeline.types.operator.Operator"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Selector) -> dict:
    out: dict = {}
    if "field_name" in value:
        out["fieldName"] = value["field_name"]
    if "operator" in value:
        import aws_sdk_data_pipeline.types.operator

        out["operator"] = aws_sdk_data_pipeline.types.operator.serialize_aws_json_1_1(
            value["operator"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Selector:
    out: Selector = {}  # type: ignore[typeddict-item]
    if "fieldName" in data:
        out["field_name"] = data["fieldName"]
    if "operator" in data:
        import aws_sdk_data_pipeline.types.operator

        out["operator"] = aws_sdk_data_pipeline.types.operator.deserialize_aws_json_1_1(
            data["operator"]
        )
    return out

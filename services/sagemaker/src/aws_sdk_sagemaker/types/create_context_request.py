"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateContextRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.context_name
    import aws_sdk_sagemaker.types.context_source
    import aws_sdk_sagemaker.types.experiment_description
    import aws_sdk_sagemaker.types.lineage_entity_parameters
    import aws_sdk_sagemaker.types.string256
    import aws_sdk_sagemaker.types.tag_list


class CreateContextRequest(TypedDict, closed=True):
    context_name: NotRequired["aws_sdk_sagemaker.types.context_name.ContextName"]
    """<p>The name of the context. Must be unique to your account in an Amazon Web Services Region.</p>"""
    source: NotRequired["aws_sdk_sagemaker.types.context_source.ContextSource"]
    """<p>The source type, ID, and URI.</p>"""
    context_type: NotRequired["aws_sdk_sagemaker.types.string256.String256"]
    """<p>The context type.</p>"""
    description: NotRequired[
        "aws_sdk_sagemaker.types.experiment_description.ExperimentDescription"
    ]
    """<p>The description of the context.</p>"""
    properties: NotRequired[
        "aws_sdk_sagemaker.types.lineage_entity_parameters.LineageEntityParameters"
    ]
    """<p>A list of properties to add to the context.</p>"""
    tags: NotRequired["aws_sdk_sagemaker.types.tag_list.TagList"]
    """<p>A list of tags to apply to the context.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateContextRequest) -> dict:
    out: dict = {}
    if "context_name" in value:
        out["ContextName"] = value["context_name"]
    if "source" in value:
        import aws_sdk_sagemaker.types.context_source

        out["Source"] = aws_sdk_sagemaker.types.context_source.serialize_aws_json_1_1(
            value["source"]
        )
    if "context_type" in value:
        out["ContextType"] = value["context_type"]
    if "description" in value:
        out["Description"] = value["description"]
    if "properties" in value:
        import aws_sdk_sagemaker.types.lineage_entity_parameters

        out["Properties"] = (
            aws_sdk_sagemaker.types.lineage_entity_parameters.serialize_aws_json_1_1(
                value["properties"]
            )
        )
    if "tags" in value:
        import aws_sdk_sagemaker.types.tag_list

        out["Tags"] = aws_sdk_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateContextRequest:
    out: CreateContextRequest = {}  # type: ignore[typeddict-item]
    if "ContextName" in data:
        out["context_name"] = data["ContextName"]
    if "Source" in data:
        import aws_sdk_sagemaker.types.context_source

        out["source"] = aws_sdk_sagemaker.types.context_source.deserialize_aws_json_1_1(
            data["Source"]
        )
    if "ContextType" in data:
        out["context_type"] = data["ContextType"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Properties" in data:
        import aws_sdk_sagemaker.types.lineage_entity_parameters

        out["properties"] = (
            aws_sdk_sagemaker.types.lineage_entity_parameters.deserialize_aws_json_1_1(
                data["Properties"]
            )
        )
    if "Tags" in data:
        import aws_sdk_sagemaker.types.tag_list

        out["tags"] = aws_sdk_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.sagemaker#ContextSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.context_arn
    import aws_sdk_sagemaker.types.context_name
    import aws_sdk_sagemaker.types.context_source
    import aws_sdk_sagemaker.types.string256
    import aws_sdk_sagemaker.types.timestamp


class ContextSummary(TypedDict, closed=True):
    context_arn: NotRequired["aws_sdk_sagemaker.types.context_arn.ContextArn"]
    """<p>The Amazon Resource Name (ARN) of the context.</p>"""
    context_name: NotRequired["aws_sdk_sagemaker.types.context_name.ContextName"]
    """<p>The name of the context.</p>"""
    source: NotRequired["aws_sdk_sagemaker.types.context_source.ContextSource"]
    """<p>The source of the context.</p>"""
    context_type: NotRequired["aws_sdk_sagemaker.types.string256.String256"]
    """<p>The type of the context.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>When the context was created.</p>"""
    last_modified_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>When the context was last modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContextSummary) -> dict:
    out: dict = {}
    if "context_arn" in value:
        out["ContextArn"] = value["context_arn"]
    if "context_name" in value:
        out["ContextName"] = value["context_name"]
    if "source" in value:
        import aws_sdk_sagemaker.types.context_source

        out["Source"] = aws_sdk_sagemaker.types.context_source.serialize_aws_json_1_1(
            value["source"]
        )
    if "context_type" in value:
        out["ContextType"] = value["context_type"]
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContextSummary:
    out: ContextSummary = {}  # type: ignore[typeddict-item]
    if "ContextArn" in data:
        out["context_arn"] = data["ContextArn"]
    if "ContextName" in data:
        out["context_name"] = data["ContextName"]
    if "Source" in data:
        import aws_sdk_sagemaker.types.context_source

        out["source"] = aws_sdk_sagemaker.types.context_source.deserialize_aws_json_1_1(
            data["Source"]
        )
    if "ContextType" in data:
        out["context_type"] = data["ContextType"]
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    return out

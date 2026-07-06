"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#InputSourceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_resiliencehubv2.types.arn
    import aws_sdk_resiliencehubv2.types.eks_source
    import aws_sdk_resiliencehubv2.types.input_source_id
    import aws_sdk_resiliencehubv2.types.input_source_type
    import aws_sdk_resiliencehubv2.types.resource_tag_list
    import aws_sdk_resiliencehubv2.types.s3_url


class InputSourceSummary(TypedDict, closed=True):
    input_source_id: "aws_sdk_resiliencehubv2.types.input_source_id.InputSourceId"
    """<p>The unique identifier of the input source.</p>"""
    type: NotRequired["aws_sdk_resiliencehubv2.types.input_source_type.InputSourceType"]
    """<p>The type of the input source.</p>"""
    resource_tags: NotRequired[
        "aws_sdk_resiliencehubv2.types.resource_tag_list.ResourceTagList"
    ]
    """<p>The resource tags used for discovery, if this input source uses tags.</p>"""
    cfn_stack_arn: NotRequired["aws_sdk_resiliencehubv2.types.arn.Arn"]
    tf_state_file_url: NotRequired["aws_sdk_resiliencehubv2.types.s3_url.S3Url"]
    eks: NotRequired["aws_sdk_resiliencehubv2.types.eks_source.EksSource"]
    """<p>The Amazon EKS configuration, if this input source uses EKS.</p>"""
    design_file_s3_url: NotRequired["aws_sdk_resiliencehubv2.types.s3_url.S3Url"]
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the input source was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InputSourceSummary) -> dict:
    out: dict = {}
    out["inputSourceId"] = value["input_source_id"]
    if "type" in value:
        import aws_sdk_resiliencehubv2.types.input_source_type

        out["type"] = aws_sdk_resiliencehubv2.types.input_source_type.serialize_json(
            value["type"]
        )
    if "resource_tags" in value:
        import aws_sdk_resiliencehubv2.types.resource_tag_list

        out["resourceTags"] = (
            aws_sdk_resiliencehubv2.types.resource_tag_list.serialize_json(
                value["resource_tags"]
            )
        )
    if "cfn_stack_arn" in value:
        out["cfnStackArn"] = value["cfn_stack_arn"]
    if "tf_state_file_url" in value:
        out["tfStateFileUrl"] = value["tf_state_file_url"]
    if "eks" in value:
        import aws_sdk_resiliencehubv2.types.eks_source

        out["eks"] = aws_sdk_resiliencehubv2.types.eks_source.serialize_json(
            value["eks"]
        )
    if "design_file_s3_url" in value:
        out["designFileS3Url"] = value["design_file_s3_url"]
    if "created_at" in value:
        import aws_sdk_resiliencehubv2.types._prelude.timestamp

        out["createdAt"] = (
            aws_sdk_resiliencehubv2.types._prelude.timestamp.serialize_json(
                value["created_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> InputSourceSummary:
    out: InputSourceSummary = {}  # type: ignore[typeddict-item]
    if "inputSourceId" in data:
        out["input_source_id"] = data["inputSourceId"]
    else:
        raise DeserializationError("InputSourceSummary.input_source_id required")
    if "type" in data:
        import aws_sdk_resiliencehubv2.types.input_source_type

        out["type"] = aws_sdk_resiliencehubv2.types.input_source_type.deserialize_json(
            data["type"]
        )
    if "resourceTags" in data:
        import aws_sdk_resiliencehubv2.types.resource_tag_list

        out["resource_tags"] = (
            aws_sdk_resiliencehubv2.types.resource_tag_list.deserialize_json(
                data["resourceTags"]
            )
        )
    if "cfnStackArn" in data:
        out["cfn_stack_arn"] = data["cfnStackArn"]
    if "tfStateFileUrl" in data:
        out["tf_state_file_url"] = data["tfStateFileUrl"]
    if "eks" in data:
        import aws_sdk_resiliencehubv2.types.eks_source

        out["eks"] = aws_sdk_resiliencehubv2.types.eks_source.deserialize_json(
            data["eks"]
        )
    if "designFileS3Url" in data:
        out["design_file_s3_url"] = data["designFileS3Url"]
    if "createdAt" in data:
        import aws_sdk_resiliencehubv2.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    return out

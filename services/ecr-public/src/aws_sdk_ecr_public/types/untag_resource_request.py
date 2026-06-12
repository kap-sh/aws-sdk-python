"""Generated from Smithy shape ``com.amazonaws.ecrpublic#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ecr_public.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecr_public.types.arn
    import aws_sdk_ecr_public.types.tag_key_list


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_ecr_public.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource to delete tags from. Currently, the supported resource is an Amazon ECR Public repository.</p>"""
    tag_keys: "aws_sdk_ecr_public.types.tag_key_list.TagKeyList"
    """<p>The keys of the tags to be removed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import aws_sdk_ecr_public.types.tag_key_list

    out["tagKeys"] = aws_sdk_ecr_public.types.tag_key_list.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_arn required")
    if "tagKeys" in data:
        import aws_sdk_ecr_public.types.tag_key_list

        out["tag_keys"] = (
            aws_sdk_ecr_public.types.tag_key_list.deserialize_aws_json_1_1(
                data["tagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out

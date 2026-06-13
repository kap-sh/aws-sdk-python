"""Generated from Smithy shape ``com.amazonaws.invoicing#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_invoicing.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_invoicing.types.resource_tag_key_list
    import aws_sdk_invoicing.types.tagris_arn


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_invoicing.types.tagris_arn.TagrisArn"
    """<p> The Amazon Resource Name (ARN) to untag. </p>"""
    resource_tag_keys: (
        "aws_sdk_invoicing.types.resource_tag_key_list.ResourceTagKeyList"
    )
    """<p> Keys for the tags to be removed. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import aws_sdk_invoicing.types.resource_tag_key_list

    out["ResourceTagKeys"] = (
        aws_sdk_invoicing.types.resource_tag_key_list.serialize_aws_json_1_0(
            value["resource_tag_keys"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_arn required")
    if "ResourceTagKeys" in data:
        import aws_sdk_invoicing.types.resource_tag_key_list

        out["resource_tag_keys"] = (
            aws_sdk_invoicing.types.resource_tag_key_list.deserialize_aws_json_1_0(
                data["ResourceTagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourceRequest.resource_tag_keys required")
    return out

"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bcm_data_exports.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_data_exports.types.arn
    import aws_sdk_bcm_data_exports.types.resource_tag_key_list


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_bcm_data_exports.types.arn.Arn"
    """<p>The unique identifier for the resource.</p>"""
    resource_tag_keys: (
        "aws_sdk_bcm_data_exports.types.resource_tag_key_list.ResourceTagKeyList"
    )
    """<p>The tag keys that are associated with the resource ARN.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import aws_sdk_bcm_data_exports.types.resource_tag_key_list

    out["ResourceTagKeys"] = (
        aws_sdk_bcm_data_exports.types.resource_tag_key_list.serialize_aws_json_1_1(
            value["resource_tag_keys"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_arn required")
    if "ResourceTagKeys" in data:
        import aws_sdk_bcm_data_exports.types.resource_tag_key_list

        out["resource_tag_keys"] = (
            aws_sdk_bcm_data_exports.types.resource_tag_key_list.deserialize_aws_json_1_1(
                data["ResourceTagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourceRequest.resource_tag_keys required")
    return out

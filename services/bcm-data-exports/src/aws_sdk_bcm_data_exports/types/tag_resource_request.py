"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bcm_data_exports.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_data_exports.types.arn
    import aws_sdk_bcm_data_exports.types.resource_tag_list


class TagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_bcm_data_exports.types.arn.Arn"
    """<p>The unique identifier for the resource.</p>"""
    resource_tags: "aws_sdk_bcm_data_exports.types.resource_tag_list.ResourceTagList"
    """<p>The tags to associate with the resource. Each tag consists of a key and a value, and each key must be unique for the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import aws_sdk_bcm_data_exports.types.resource_tag_list

    out["ResourceTags"] = (
        aws_sdk_bcm_data_exports.types.resource_tag_list.serialize_aws_json_1_1(
            value["resource_tags"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if "ResourceTags" in data:
        import aws_sdk_bcm_data_exports.types.resource_tag_list

        out["resource_tags"] = (
            aws_sdk_bcm_data_exports.types.resource_tag_list.deserialize_aws_json_1_1(
                data["ResourceTags"]
            )
        )
    else:
        raise DeserializationError("TagResourceRequest.resource_tags required")
    return out

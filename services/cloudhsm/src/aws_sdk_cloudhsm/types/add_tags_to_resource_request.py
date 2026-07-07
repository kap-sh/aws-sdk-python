"""Generated from Smithy shape ``com.amazonaws.cloudhsm#AddTagsToResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudhsm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudhsm.types.string
    import aws_sdk_cloudhsm.types.tag_list


class AddTagsToResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_cloudhsm.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the AWS CloudHSM resource to tag.</p>"""
    tag_list: "aws_sdk_cloudhsm.types.tag_list.TagList"
    """<p>One or more tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddTagsToResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import aws_sdk_cloudhsm.types.tag_list

    out["TagList"] = aws_sdk_cloudhsm.types.tag_list.serialize_aws_json_1_1(
        value["tag_list"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AddTagsToResourceRequest:
    out: AddTagsToResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("AddTagsToResourceRequest.resource_arn required")
    if "TagList" in data:
        import aws_sdk_cloudhsm.types.tag_list

        out["tag_list"] = aws_sdk_cloudhsm.types.tag_list.deserialize_aws_json_1_1(
            data["TagList"]
        )
    else:
        raise DeserializationError("AddTagsToResourceRequest.tag_list required")
    return out

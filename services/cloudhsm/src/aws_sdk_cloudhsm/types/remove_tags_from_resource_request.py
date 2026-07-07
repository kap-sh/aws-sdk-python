"""Generated from Smithy shape ``com.amazonaws.cloudhsm#RemoveTagsFromResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudhsm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudhsm.types.string
    import aws_sdk_cloudhsm.types.tag_key_list


class RemoveTagsFromResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_cloudhsm.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the AWS CloudHSM resource.</p>"""
    tag_key_list: "aws_sdk_cloudhsm.types.tag_key_list.TagKeyList"
    """<p>The tag key or keys to remove.</p> <p>Specify only the tag key to remove (not the value). To overwrite the value for an existing tag, use <a>AddTagsToResource</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveTagsFromResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import aws_sdk_cloudhsm.types.tag_key_list

    out["TagKeyList"] = aws_sdk_cloudhsm.types.tag_key_list.serialize_aws_json_1_1(
        value["tag_key_list"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoveTagsFromResourceRequest:
    out: RemoveTagsFromResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError(
            "RemoveTagsFromResourceRequest.resource_arn required"
        )
    if "TagKeyList" in data:
        import aws_sdk_cloudhsm.types.tag_key_list

        out["tag_key_list"] = (
            aws_sdk_cloudhsm.types.tag_key_list.deserialize_aws_json_1_1(
                data["TagKeyList"]
            )
        )
    else:
        raise DeserializationError(
            "RemoveTagsFromResourceRequest.tag_key_list required"
        )
    return out

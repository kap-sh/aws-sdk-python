"""Generated from Smithy shape ``com.amazonaws.apprunner#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.app_runner_resource_arn
    import aws_sdk_apprunner.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource that you want to remove tags from.</p> <p>It must be the ARN of an App Runner resource.</p>"""
    tag_keys: "aws_sdk_apprunner.types.tag_key_list.TagKeyList"
    """<p>A list of tag keys that you want to remove.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import aws_sdk_apprunner.types.tag_key_list

    out["TagKeys"] = aws_sdk_apprunner.types.tag_key_list.serialize_aws_json_1_0(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_arn required")
    if "TagKeys" in data:
        import aws_sdk_apprunner.types.tag_key_list

        out["tag_keys"] = aws_sdk_apprunner.types.tag_key_list.deserialize_aws_json_1_0(
            data["TagKeys"]
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out

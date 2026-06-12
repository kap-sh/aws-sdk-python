"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_application_auto_scaling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_auto_scaling.types.amazon_resource_name
    import aws_sdk_application_auto_scaling.types.tag_key_list


class UntagResourceRequest(TypedDict):
    resource_arn: (
        "aws_sdk_application_auto_scaling.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>Identifies the Application Auto Scaling scalable target from which to remove tags.</p> <p>For example: <code>arn:aws:application-autoscaling:us-east-1:123456789012:scalable-target/1234abcd56ab78cd901ef1234567890ab123</code> </p> <p>To get the ARN for a scalable target, use <a>DescribeScalableTargets</a>.</p>"""
    tag_keys: "aws_sdk_application_auto_scaling.types.tag_key_list.TagKeyList"
    """<p>One or more tag keys. Specify only the tag keys, not the tag values.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import aws_sdk_application_auto_scaling.types.tag_key_list

    out["TagKeys"] = (
        aws_sdk_application_auto_scaling.types.tag_key_list.serialize_aws_json_1_1(
            value["tag_keys"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_arn required")
    if "TagKeys" in data:
        import aws_sdk_application_auto_scaling.types.tag_key_list

        out["tag_keys"] = (
            aws_sdk_application_auto_scaling.types.tag_key_list.deserialize_aws_json_1_1(
                data["TagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out

"""Generated from Smithy shape ``com.amazonaws.frauddetector#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.fraud_detector_arn
    import aws_sdk_frauddetector.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_frauddetector.types.fraud_detector_arn.fraudDetectorArn"
    """<p>The ARN of the resource from which to remove the tag.</p>"""
    tag_keys: "aws_sdk_frauddetector.types.tag_key_list.tagKeyList"
    """<p>The resource ARN.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["resourceARN"] = value["resource_arn"]
    import aws_sdk_frauddetector.types.tag_key_list

    out["tagKeys"] = aws_sdk_frauddetector.types.tag_key_list.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "resourceARN" in data:
        out["resource_arn"] = data["resourceARN"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_arn required")
    if "tagKeys" in data:
        import aws_sdk_frauddetector.types.tag_key_list

        out["tag_keys"] = (
            aws_sdk_frauddetector.types.tag_key_list.deserialize_aws_json_1_1(
                data["tagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out

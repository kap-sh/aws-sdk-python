"""Generated from Smithy shape ``com.amazonaws.frauddetector#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.fraud_detector_arn
    import aws_sdk_frauddetector.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_frauddetector.types.fraud_detector_arn.fraudDetectorArn"
    """<p>The resource ARN.</p>"""
    tags: "aws_sdk_frauddetector.types.tag_list.tagList"
    """<p>The tags to assign to the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["resourceARN"] = value["resource_arn"]
    import aws_sdk_frauddetector.types.tag_list

    out["tags"] = aws_sdk_frauddetector.types.tag_list.serialize_aws_json_1_1(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "resourceARN" in data:
        out["resource_arn"] = data["resourceARN"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if "tags" in data:
        import aws_sdk_frauddetector.types.tag_list

        out["tags"] = aws_sdk_frauddetector.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out

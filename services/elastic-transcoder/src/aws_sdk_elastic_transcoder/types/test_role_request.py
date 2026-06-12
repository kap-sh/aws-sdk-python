"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#TestRoleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_elastic_transcoder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elastic_transcoder.types.bucket_name
    import aws_sdk_elastic_transcoder.types.role
    import aws_sdk_elastic_transcoder.types.sns_topics


class TestRoleRequest(TypedDict):
    role: "aws_sdk_elastic_transcoder.types.role.Role"
    """<p>The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to test.</p>"""
    input_bucket: "aws_sdk_elastic_transcoder.types.bucket_name.BucketName"
    """<p>The Amazon S3 bucket that contains media files to be transcoded. The action attempts to read from this bucket.</p>"""
    output_bucket: "aws_sdk_elastic_transcoder.types.bucket_name.BucketName"
    """<p>The Amazon S3 bucket that Elastic Transcoder writes transcoded media files to. The action attempts to read from this bucket.</p>"""
    topics: "aws_sdk_elastic_transcoder.types.sns_topics.SnsTopics"
    """<p>The ARNs of one or more Amazon Simple Notification Service (Amazon SNS) topics that you want the action to send a test notification to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestRoleRequest) -> dict:
    out: dict = {}
    out["Role"] = value["role"]
    out["InputBucket"] = value["input_bucket"]
    out["OutputBucket"] = value["output_bucket"]
    import aws_sdk_elastic_transcoder.types.sns_topics

    out["Topics"] = aws_sdk_elastic_transcoder.types.sns_topics.serialize_json(
        value["topics"]
    )
    return out


def deserialize_json(data: dict) -> TestRoleRequest:
    out: TestRoleRequest = {}  # type: ignore[typeddict-item]
    if "Role" in data:
        out["role"] = data["Role"]
    else:
        raise DeserializationError("TestRoleRequest.role required")
    if "InputBucket" in data:
        out["input_bucket"] = data["InputBucket"]
    else:
        raise DeserializationError("TestRoleRequest.input_bucket required")
    if "OutputBucket" in data:
        out["output_bucket"] = data["OutputBucket"]
    else:
        raise DeserializationError("TestRoleRequest.output_bucket required")
    if "Topics" in data:
        import aws_sdk_elastic_transcoder.types.sns_topics

        out["topics"] = aws_sdk_elastic_transcoder.types.sns_topics.deserialize_json(
            data["Topics"]
        )
    else:
        raise DeserializationError("TestRoleRequest.topics required")
    return out

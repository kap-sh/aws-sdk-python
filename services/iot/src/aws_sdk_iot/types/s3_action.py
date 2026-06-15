"""Generated from Smithy shape ``com.amazonaws.iot#S3Action``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.aws_arn
    import aws_sdk_iot.types.bucket_name
    import aws_sdk_iot.types.canned_access_control_list
    import aws_sdk_iot.types.key


class S3Action(TypedDict):
    role_arn: "aws_sdk_iot.types.aws_arn.AwsArn"
    """<p>The ARN of the IAM role that grants access.</p>"""
    bucket_name: "aws_sdk_iot.types.bucket_name.BucketName"
    """<p>The Amazon S3 bucket.</p>"""
    key: "aws_sdk_iot.types.key.Key"
    r"""<p>The object key. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/dev/list_amazons3.html\">Actions, resources, and condition keys for Amazon S3</a>.</p>"""
    canned_acl: NotRequired[
        "aws_sdk_iot.types.canned_access_control_list.CannedAccessControlList"
    ]
    r"""<p>The Amazon S3 canned ACL that controls access to the object identified by the object key. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl\">S3 canned ACLs</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Action) -> dict:
    out: dict = {}
    out["roleArn"] = value["role_arn"]
    out["bucketName"] = value["bucket_name"]
    out["key"] = value["key"]
    if "canned_acl" in value:
        import aws_sdk_iot.types.canned_access_control_list

        out["cannedAcl"] = aws_sdk_iot.types.canned_access_control_list.serialize_json(
            value["canned_acl"]
        )
    return out


def deserialize_json(data: dict) -> S3Action:
    out: S3Action = {}  # type: ignore[typeddict-item]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("S3Action.role_arn required")
    if "bucketName" in data:
        out["bucket_name"] = data["bucketName"]
    else:
        raise DeserializationError("S3Action.bucket_name required")
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("S3Action.key required")
    if "cannedAcl" in data:
        import aws_sdk_iot.types.canned_access_control_list

        out["canned_acl"] = (
            aws_sdk_iot.types.canned_access_control_list.deserialize_json(
                data["cannedAcl"]
            )
        )
    return out

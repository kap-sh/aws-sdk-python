"""Generated from Smithy shape ``com.amazonaws.waf#CreateWebACLMigrationStackRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_waf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf.types.ignore_unsupported_type
    import aws_sdk_waf.types.resource_id
    import aws_sdk_waf.types.s3_bucket_name


class CreateWebACLMigrationStackRequest(TypedDict, closed=True):
    web_acl_id: "aws_sdk_waf.types.resource_id.ResourceId"
    """<p>The UUID of the WAF Classic web ACL that you want to migrate to WAF v2.</p>"""
    s3_bucket_name: "aws_sdk_waf.types.s3_bucket_name.S3BucketName"
    """<p>The name of the Amazon S3 bucket to store the CloudFormation template in. The S3 bucket must be configured as follows for the migration: </p> <ul> <li> <p>The bucket name must start with <code>aws-waf-migration-</code>. For example, <code>aws-waf-migration-my-web-acl</code>.</p> </li> <li> <p>The bucket must be in the Region where you are deploying the template. For example, for a web ACL in us-west-2, you must use an Amazon S3 bucket in us-west-2 and you must deploy the template stack to us-west-2. </p> </li> <li> <p>The bucket policies must permit the migration process to write data. For listings of the bucket policies, see the Examples section. </p> </li> </ul>"""
    ignore_unsupported_type: (
        "aws_sdk_waf.types.ignore_unsupported_type.IgnoreUnsupportedType"
    )
    """<p>Indicates whether to exclude entities that can't be migrated or to stop the migration. Set this to true to ignore unsupported entities in the web ACL during the migration. Otherwise, if AWS WAF encounters unsupported entities, it stops the process and throws an exception. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateWebACLMigrationStackRequest) -> dict:
    out: dict = {}
    out["WebACLId"] = value["web_acl_id"]
    out["S3BucketName"] = value["s3_bucket_name"]
    out["IgnoreUnsupportedType"] = value["ignore_unsupported_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateWebACLMigrationStackRequest:
    out: CreateWebACLMigrationStackRequest = {}  # type: ignore[typeddict-item]
    if "WebACLId" in data:
        out["web_acl_id"] = data["WebACLId"]
    else:
        raise DeserializationError(
            "CreateWebACLMigrationStackRequest.web_acl_id required"
        )
    if "S3BucketName" in data:
        out["s3_bucket_name"] = data["S3BucketName"]
    else:
        raise DeserializationError(
            "CreateWebACLMigrationStackRequest.s3_bucket_name required"
        )
    if "IgnoreUnsupportedType" in data:
        out["ignore_unsupported_type"] = data["IgnoreUnsupportedType"]
    else:
        raise DeserializationError(
            "CreateWebACLMigrationStackRequest.ignore_unsupported_type required"
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3AccountPublicAccessBlockDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean


class AwsS3AccountPublicAccessBlockDetails(TypedDict):
    block_public_acls: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether to reject calls to update an S3 bucket if the calls include a public access control list (ACL).</p>"""
    block_public_policy: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether to reject calls to update the access policy for an S3 bucket or access point if the policy allows public access.</p>"""
    ignore_public_acls: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether Amazon S3 ignores public ACLs that are associated with an S3 bucket.</p>"""
    restrict_public_buckets: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether to restrict access to an access point or S3 bucket that has a public policy to only Amazon Web Services service principals and authorized users within the S3 bucket owner's account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsS3AccountPublicAccessBlockDetails) -> dict:
    out: dict = {}
    if "block_public_acls" in value:
        out["BlockPublicAcls"] = value["block_public_acls"]
    if "block_public_policy" in value:
        out["BlockPublicPolicy"] = value["block_public_policy"]
    if "ignore_public_acls" in value:
        out["IgnorePublicAcls"] = value["ignore_public_acls"]
    if "restrict_public_buckets" in value:
        out["RestrictPublicBuckets"] = value["restrict_public_buckets"]
    return out


def deserialize_json(data: dict) -> AwsS3AccountPublicAccessBlockDetails:
    out: AwsS3AccountPublicAccessBlockDetails = {}  # type: ignore[typeddict-item]
    if "BlockPublicAcls" in data:
        out["block_public_acls"] = data["BlockPublicAcls"]
    if "BlockPublicPolicy" in data:
        out["block_public_policy"] = data["BlockPublicPolicy"]
    if "IgnorePublicAcls" in data:
        out["ignore_public_acls"] = data["IgnorePublicAcls"]
    if "RestrictPublicBuckets" in data:
        out["restrict_public_buckets"] = data["RestrictPublicBuckets"]
    return out

"""Generated from Smithy shape ``com.amazonaws.securitylake#CustomLogSourceProvider``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_securitylake.types.role_arn
    import aws_sdk_securitylake.types.s3_uri

class CustomLogSourceProvider(TypedDict):
    role_arn: NotRequired["aws_sdk_securitylake.types.role_arn.RoleArn"]
    """<p>The ARN of the IAM role to be used by the entity putting logs into your custom source partition. Security Lake will apply the correct access policies to this role, but you must first manually create the trust policy for this role. The IAM role name must start with the text 'Security Lake'. The IAM role must trust the <code>logProviderAccountId</code> to assume the role.</p>"""
    location: NotRequired["aws_sdk_securitylake.types.s3_uri.S3URI"]
    """<p>The location of the partition in the Amazon S3 bucket for Security Lake.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CustomLogSourceProvider) -> dict:
    out: dict = {}
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "location" in value:
        out["location"] = value["location"]
    return out


def deserialize_json(data: dict) -> CustomLogSourceProvider:
    out: CustomLogSourceProvider = {}  # type: ignore[typeddict-item]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "location" in data:
        out["location"] = data["location"]
    return out
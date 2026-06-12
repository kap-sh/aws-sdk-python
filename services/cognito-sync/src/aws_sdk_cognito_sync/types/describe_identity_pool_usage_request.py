"""Generated from Smithy shape ``com.amazonaws.cognitosync#DescribeIdentityPoolUsageRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cognito_sync.types.identity_pool_id


class DescribeIdentityPoolUsageRequest(TypedDict):
    identity_pool_id: "aws_sdk_cognito_sync.types.identity_pool_id.IdentityPoolId"
    """A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region."""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeIdentityPoolUsageRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeIdentityPoolUsageRequest:
    out: DescribeIdentityPoolUsageRequest = {}  # type: ignore[typeddict-item]
    return out

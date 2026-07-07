"""Generated from Smithy shape ``com.amazonaws.cognitosync#DescribeIdentityPoolUsageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cognito_sync.types.identity_pool_usage


class DescribeIdentityPoolUsageResponse(TypedDict, closed=True):
    identity_pool_usage: NotRequired[
        "aws_sdk_cognito_sync.types.identity_pool_usage.IdentityPoolUsage"
    ]
    """Information about the usage of the identity pool."""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeIdentityPoolUsageResponse) -> dict:
    out: dict = {}
    if "identity_pool_usage" in value:
        import aws_sdk_cognito_sync.types.identity_pool_usage

        out["IdentityPoolUsage"] = (
            aws_sdk_cognito_sync.types.identity_pool_usage.serialize_json(
                value["identity_pool_usage"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeIdentityPoolUsageResponse:
    out: DescribeIdentityPoolUsageResponse = {}  # type: ignore[typeddict-item]
    if "IdentityPoolUsage" in data:
        import aws_sdk_cognito_sync.types.identity_pool_usage

        out["identity_pool_usage"] = (
            aws_sdk_cognito_sync.types.identity_pool_usage.deserialize_json(
                data["IdentityPoolUsage"]
            )
        )
    return out

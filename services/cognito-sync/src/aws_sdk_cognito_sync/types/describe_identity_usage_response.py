"""Generated from Smithy shape ``com.amazonaws.cognitosync#DescribeIdentityUsageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cognito_sync.types.identity_usage


class DescribeIdentityUsageResponse(TypedDict, closed=True):
    identity_usage: NotRequired[
        "aws_sdk_cognito_sync.types.identity_usage.IdentityUsage"
    ]
    """Usage information for the identity."""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeIdentityUsageResponse) -> dict:
    out: dict = {}
    if "identity_usage" in value:
        import aws_sdk_cognito_sync.types.identity_usage

        out["IdentityUsage"] = aws_sdk_cognito_sync.types.identity_usage.serialize_json(
            value["identity_usage"]
        )
    return out


def deserialize_json(data: dict) -> DescribeIdentityUsageResponse:
    out: DescribeIdentityUsageResponse = {}  # type: ignore[typeddict-item]
    if "IdentityUsage" in data:
        import aws_sdk_cognito_sync.types.identity_usage

        out["identity_usage"] = (
            aws_sdk_cognito_sync.types.identity_usage.deserialize_json(
                data["IdentityUsage"]
            )
        )
    return out

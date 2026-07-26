"""Generated from Smithy shape ``com.amazonaws.cognitosync#DescribeIdentityUsageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_sync.types.identity_usage


class DescribeIdentityUsageResponse(TypedDict, closed=True):
    identity_usage: NotRequired["capo_cognito_sync.types.identity_usage.IdentityUsage"]
    """Usage information for the identity."""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeIdentityUsageResponse) -> dict:
    out: dict = {}
    if "identity_usage" in value:
        import capo_cognito_sync.types.identity_usage

        out["IdentityUsage"] = capo_cognito_sync.types.identity_usage.serialize_json(
            value["identity_usage"]
        )
    return out


def deserialize_json(data: dict) -> DescribeIdentityUsageResponse:
    out: DescribeIdentityUsageResponse = {}  # type: ignore[typeddict-item]
    if "IdentityUsage" in data:
        import capo_cognito_sync.types.identity_usage

        out["identity_usage"] = capo_cognito_sync.types.identity_usage.deserialize_json(
            data["IdentityUsage"]
        )
    return out

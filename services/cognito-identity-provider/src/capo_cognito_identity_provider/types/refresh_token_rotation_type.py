"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#RefreshTokenRotationType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.feature_type
    import capo_cognito_identity_provider.types.retry_grace_period_seconds_type


class RefreshTokenRotationType(TypedDict, closed=True):
    feature: "capo_cognito_identity_provider.types.feature_type.FeatureType"
    """<p>The state of refresh token rotation for the current app client.</p>"""
    retry_grace_period_seconds: NotRequired[
        "capo_cognito_identity_provider.types.retry_grace_period_seconds_type.RetryGracePeriodSecondsType"
    ]
    """<p>When you request a token refresh with <code>GetTokensFromRefreshToken</code>, the original refresh token that you're rotating out can remain valid for a period of time of up to 60 seconds. This allows for client-side retries. When <code>RetryGracePeriodSeconds</code> is <code>0</code>, the grace period is disabled and a successful request immediately invalidates the submitted refresh token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RefreshTokenRotationType) -> dict:
    out: dict = {}
    import capo_cognito_identity_provider.types.feature_type

    out["Feature"] = (
        capo_cognito_identity_provider.types.feature_type.serialize_aws_json_1_1(
            value["feature"]
        )
    )
    if "retry_grace_period_seconds" in value:
        out["RetryGracePeriodSeconds"] = value["retry_grace_period_seconds"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RefreshTokenRotationType:
    out: RefreshTokenRotationType = {}  # type: ignore[typeddict-item]
    if "Feature" in data:
        import capo_cognito_identity_provider.types.feature_type

        out["feature"] = (
            capo_cognito_identity_provider.types.feature_type.deserialize_aws_json_1_1(
                data["Feature"]
            )
        )
    else:
        raise DeserializationError("RefreshTokenRotationType.feature required")
    if "RetryGracePeriodSeconds" in data:
        out["retry_grace_period_seconds"] = data["RetryGracePeriodSeconds"]
    return out

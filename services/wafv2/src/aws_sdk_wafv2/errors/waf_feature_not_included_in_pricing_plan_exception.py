"""Generated from Smithy shape ``com.amazonaws.wafv2#WAFFeatureNotIncludedInPricingPlanException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_wafv2.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.disallowed_features
    import aws_sdk_wafv2.types.error_message


class WAFFeatureNotIncludedInPricingPlanException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_wafv2.types.error_message.ErrorMessage"]
    disallowed_features: NotRequired[
        "aws_sdk_wafv2.types.disallowed_features.DisallowedFeatures"
    ]
    """<p>The names of the disallowed WAF features.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WAFFeatureNotIncludedInPricingPlanException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "disallowed_features" in value:
        import aws_sdk_wafv2.types.disallowed_features

        out["DisallowedFeatures"] = (
            aws_sdk_wafv2.types.disallowed_features.serialize_aws_json_1_1(
                value["disallowed_features"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> WAFFeatureNotIncludedInPricingPlanException_:
    out: WAFFeatureNotIncludedInPricingPlanException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "DisallowedFeatures" in data:
        import aws_sdk_wafv2.types.disallowed_features

        out["disallowed_features"] = (
            aws_sdk_wafv2.types.disallowed_features.deserialize_aws_json_1_1(
                data["DisallowedFeatures"]
            )
        )
    return out


class WAFFeatureNotIncludedInPricingPlanException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.wafv2#WAFFeatureNotIncludedInPricingPlanException``."""

    code: str | None = "WAFFeatureNotIncludedInPricingPlanException"

    def __init__(self, data: WAFFeatureNotIncludedInPricingPlanException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="WAFFeatureNotIncludedInPricingPlanException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict
    ) -> "WAFFeatureNotIncludedInPricingPlanException":
        return cls(deserialize_aws_json_1_1(data))

"""Generated from Smithy shape ``com.amazonaws.securityhub#BatchDisableStandardsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.standards_subscription_arns


class BatchDisableStandardsRequest(TypedDict, closed=True):
    standards_subscription_arns: NotRequired[
        "aws_sdk_securityhub.types.standards_subscription_arns.StandardsSubscriptionArns"
    ]
    """<p>The ARNs of the standards subscriptions to disable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDisableStandardsRequest) -> dict:
    out: dict = {}
    if "standards_subscription_arns" in value:
        import aws_sdk_securityhub.types.standards_subscription_arns

        out["StandardsSubscriptionArns"] = (
            aws_sdk_securityhub.types.standards_subscription_arns.serialize_json(
                value["standards_subscription_arns"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchDisableStandardsRequest:
    out: BatchDisableStandardsRequest = {}  # type: ignore[typeddict-item]
    if "StandardsSubscriptionArns" in data:
        import aws_sdk_securityhub.types.standards_subscription_arns

        out["standards_subscription_arns"] = (
            aws_sdk_securityhub.types.standards_subscription_arns.deserialize_json(
                data["StandardsSubscriptionArns"]
            )
        )
    return out

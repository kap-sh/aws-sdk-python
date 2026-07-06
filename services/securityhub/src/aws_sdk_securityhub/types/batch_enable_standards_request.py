"""Generated from Smithy shape ``com.amazonaws.securityhub#BatchEnableStandardsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.standards_subscription_requests


class BatchEnableStandardsRequest(TypedDict, closed=True):
    standards_subscription_requests: NotRequired[
        "aws_sdk_securityhub.types.standards_subscription_requests.StandardsSubscriptionRequests"
    ]
    """<p>The list of standards checks to enable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchEnableStandardsRequest) -> dict:
    out: dict = {}
    if "standards_subscription_requests" in value:
        import aws_sdk_securityhub.types.standards_subscription_requests

        out["StandardsSubscriptionRequests"] = (
            aws_sdk_securityhub.types.standards_subscription_requests.serialize_json(
                value["standards_subscription_requests"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchEnableStandardsRequest:
    out: BatchEnableStandardsRequest = {}  # type: ignore[typeddict-item]
    if "StandardsSubscriptionRequests" in data:
        import aws_sdk_securityhub.types.standards_subscription_requests

        out["standards_subscription_requests"] = (
            aws_sdk_securityhub.types.standards_subscription_requests.deserialize_json(
                data["StandardsSubscriptionRequests"]
            )
        )
    return out

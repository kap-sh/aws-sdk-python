"""Generated from Smithy shape ``com.amazonaws.vpclattice#GetAccessLogSubscriptionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.access_log_subscription_identifier


class GetAccessLogSubscriptionRequest(TypedDict):
    access_log_subscription_identifier: "aws_sdk_vpc_lattice.types.access_log_subscription_identifier.AccessLogSubscriptionIdentifier"
    """<p>The ID or ARN of the access log subscription.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAccessLogSubscriptionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAccessLogSubscriptionRequest:
    out: GetAccessLogSubscriptionRequest = {}  # type: ignore[typeddict-item]
    return out

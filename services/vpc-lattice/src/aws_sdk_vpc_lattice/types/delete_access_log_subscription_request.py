"""Generated from Smithy shape ``com.amazonaws.vpclattice#DeleteAccessLogSubscriptionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.access_log_subscription_identifier


class DeleteAccessLogSubscriptionRequest(TypedDict):
    access_log_subscription_identifier: "aws_sdk_vpc_lattice.types.access_log_subscription_identifier.AccessLogSubscriptionIdentifier"
    """<p>The ID or ARN of the access log subscription.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAccessLogSubscriptionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAccessLogSubscriptionRequest:
    out: DeleteAccessLogSubscriptionRequest = {}  # type: ignore[typeddict-item]
    return out

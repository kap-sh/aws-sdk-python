"""Generated from Smithy shape ``com.amazonaws.vpclattice#UpdateAccessLogSubscriptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_vpc_lattice.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.access_log_destination_arn
    import aws_sdk_vpc_lattice.types.access_log_subscription_identifier


class UpdateAccessLogSubscriptionRequest(TypedDict, closed=True):
    access_log_subscription_identifier: "aws_sdk_vpc_lattice.types.access_log_subscription_identifier.AccessLogSubscriptionIdentifier"
    """<p>The ID or ARN of the access log subscription.</p>"""
    destination_arn: (
        "aws_sdk_vpc_lattice.types.access_log_destination_arn.AccessLogDestinationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the access log destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAccessLogSubscriptionRequest) -> dict:
    out: dict = {}
    out["destinationArn"] = value["destination_arn"]
    return out


def deserialize_json(data: dict) -> UpdateAccessLogSubscriptionRequest:
    out: UpdateAccessLogSubscriptionRequest = {}  # type: ignore[typeddict-item]
    if "destinationArn" in data:
        out["destination_arn"] = data["destinationArn"]
    else:
        raise DeserializationError(
            "UpdateAccessLogSubscriptionRequest.destination_arn required"
        )
    return out

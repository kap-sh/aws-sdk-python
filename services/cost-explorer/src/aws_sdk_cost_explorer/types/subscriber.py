"""Generated from Smithy shape ``com.amazonaws.costexplorer#Subscriber``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.subscriber_address
    import aws_sdk_cost_explorer.types.subscriber_status
    import aws_sdk_cost_explorer.types.subscriber_type


class Subscriber(TypedDict, closed=True):
    address: NotRequired[
        "aws_sdk_cost_explorer.types.subscriber_address.SubscriberAddress"
    ]
    """<p>The email address or SNS Amazon Resource Name (ARN). This depends on the <code>Type</code>. </p>"""
    type: NotRequired["aws_sdk_cost_explorer.types.subscriber_type.SubscriberType"]
    """<p>The notification delivery channel. </p>"""
    status: NotRequired[
        "aws_sdk_cost_explorer.types.subscriber_status.SubscriberStatus"
    ]
    """<p>Indicates if the subscriber accepts the notifications. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Subscriber) -> dict:
    out: dict = {}
    if "address" in value:
        out["Address"] = value["address"]
    if "type" in value:
        import aws_sdk_cost_explorer.types.subscriber_type

        out["Type"] = (
            aws_sdk_cost_explorer.types.subscriber_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "status" in value:
        import aws_sdk_cost_explorer.types.subscriber_status

        out["Status"] = (
            aws_sdk_cost_explorer.types.subscriber_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Subscriber:
    out: Subscriber = {}  # type: ignore[typeddict-item]
    if "Address" in data:
        out["address"] = data["Address"]
    if "Type" in data:
        import aws_sdk_cost_explorer.types.subscriber_type

        out["type"] = (
            aws_sdk_cost_explorer.types.subscriber_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "Status" in data:
        import aws_sdk_cost_explorer.types.subscriber_status

        out["status"] = (
            aws_sdk_cost_explorer.types.subscriber_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    return out

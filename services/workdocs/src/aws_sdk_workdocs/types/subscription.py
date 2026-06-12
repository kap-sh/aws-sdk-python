"""Generated from Smithy shape ``com.amazonaws.workdocs#Subscription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.id_type
    import aws_sdk_workdocs.types.subscription_end_point_type
    import aws_sdk_workdocs.types.subscription_protocol_type


class Subscription(TypedDict):
    subscription_id: NotRequired["aws_sdk_workdocs.types.id_type.IdType"]
    """<p>The ID of the subscription.</p>"""
    end_point: NotRequired[
        "aws_sdk_workdocs.types.subscription_end_point_type.SubscriptionEndPointType"
    ]
    """<p>The endpoint of the subscription.</p>"""
    protocol: NotRequired[
        "aws_sdk_workdocs.types.subscription_protocol_type.SubscriptionProtocolType"
    ]
    """<p>The protocol of the subscription.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Subscription) -> dict:
    out: dict = {}
    if "subscription_id" in value:
        out["SubscriptionId"] = value["subscription_id"]
    if "end_point" in value:
        out["EndPoint"] = value["end_point"]
    if "protocol" in value:
        import aws_sdk_workdocs.types.subscription_protocol_type

        out["Protocol"] = (
            aws_sdk_workdocs.types.subscription_protocol_type.serialize_json(
                value["protocol"]
            )
        )
    return out


def deserialize_json(data: dict) -> Subscription:
    out: Subscription = {}  # type: ignore[typeddict-item]
    if "SubscriptionId" in data:
        out["subscription_id"] = data["SubscriptionId"]
    if "EndPoint" in data:
        out["end_point"] = data["EndPoint"]
    if "Protocol" in data:
        import aws_sdk_workdocs.types.subscription_protocol_type

        out["protocol"] = (
            aws_sdk_workdocs.types.subscription_protocol_type.deserialize_json(
                data["Protocol"]
            )
        )
    return out

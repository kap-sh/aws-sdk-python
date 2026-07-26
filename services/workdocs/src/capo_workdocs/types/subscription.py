"""Generated from Smithy shape ``com.amazonaws.workdocs#Subscription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.id_type
    import capo_workdocs.types.subscription_end_point_type
    import capo_workdocs.types.subscription_protocol_type


class Subscription(TypedDict, closed=True):
    subscription_id: NotRequired["capo_workdocs.types.id_type.IdType"]
    """<p>The ID of the subscription.</p>"""
    end_point: NotRequired[
        "capo_workdocs.types.subscription_end_point_type.SubscriptionEndPointType"
    ]
    """<p>The endpoint of the subscription.</p>"""
    protocol: NotRequired[
        "capo_workdocs.types.subscription_protocol_type.SubscriptionProtocolType"
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
        import capo_workdocs.types.subscription_protocol_type

        out["Protocol"] = capo_workdocs.types.subscription_protocol_type.serialize_json(
            value["protocol"]
        )
    return out


def deserialize_json(data: dict) -> Subscription:
    out: Subscription = {}  # type: ignore[typeddict-item]
    if "SubscriptionId" in data:
        out["subscription_id"] = data["SubscriptionId"]
    if "EndPoint" in data:
        out["end_point"] = data["EndPoint"]
    if "Protocol" in data:
        import capo_workdocs.types.subscription_protocol_type

        out["protocol"] = (
            capo_workdocs.types.subscription_protocol_type.deserialize_json(
                data["Protocol"]
            )
        )
    return out

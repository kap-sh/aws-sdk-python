"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ListedEntitlement``."""

from typing import TypedDict

from typing_extensions import NotRequired


class ListedEntitlement(TypedDict):
    data_transfer_subscriber_fee_percent: NotRequired["int"]
    """<p> Percentage from 0-100 of the data transfer cost to be billed to the subscriber.</p>"""
    entitlement_arn: NotRequired["str"]
    """<p> The ARN of the entitlement.</p>"""
    entitlement_name: NotRequired["str"]
    """<p> The name of the entitlement.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListedEntitlement) -> dict:
    out: dict = {}
    if "data_transfer_subscriber_fee_percent" in value:
        out["dataTransferSubscriberFeePercent"] = value[
            "data_transfer_subscriber_fee_percent"
        ]
    if "entitlement_arn" in value:
        out["entitlementArn"] = value["entitlement_arn"]
    if "entitlement_name" in value:
        out["entitlementName"] = value["entitlement_name"]
    return out


def deserialize_json(data: dict) -> ListedEntitlement:
    out: ListedEntitlement = {}  # type: ignore[typeddict-item]
    if "dataTransferSubscriberFeePercent" in data:
        out["data_transfer_subscriber_fee_percent"] = data[
            "dataTransferSubscriberFeePercent"
        ]
    if "entitlementArn" in data:
        out["entitlement_arn"] = data["entitlementArn"]
    if "entitlementName" in data:
        out["entitlement_name"] = data["entitlementName"]
    return out

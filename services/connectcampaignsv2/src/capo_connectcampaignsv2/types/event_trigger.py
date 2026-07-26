"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#EventTrigger``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.arn


class EventTrigger(TypedDict, closed=True):
    customer_profiles_domain_arn: NotRequired["capo_connectcampaignsv2.types.arn.Arn"]


# --- restJson1 ser/de ---
def serialize_json(value: EventTrigger) -> dict:
    out: dict = {}
    if "customer_profiles_domain_arn" in value:
        out["customerProfilesDomainArn"] = value["customer_profiles_domain_arn"]
    return out


def deserialize_json(data: dict) -> EventTrigger:
    out: EventTrigger = {}  # type: ignore[typeddict-item]
    if "customerProfilesDomainArn" in data:
        out["customer_profiles_domain_arn"] = data["customerProfilesDomainArn"]
    return out

"""Generated from Smithy shape ``com.amazonaws.medialive#MultiplexMediaConnectOutputDestinationSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string_min1


class MultiplexMediaConnectOutputDestinationSettings(TypedDict, closed=True):
    entitlement_arn: NotRequired["capo_medialive.types.__string_min1.__stringMin1"]
    """The MediaConnect entitlement ARN available as a Flow source."""


# --- restJson1 ser/de ---
def serialize_json(value: MultiplexMediaConnectOutputDestinationSettings) -> dict:
    out: dict = {}
    if "entitlement_arn" in value:
        out["entitlementArn"] = value["entitlement_arn"]
    return out


def deserialize_json(data: dict) -> MultiplexMediaConnectOutputDestinationSettings:
    out: MultiplexMediaConnectOutputDestinationSettings = {}  # type: ignore[typeddict-item]
    if "entitlementArn" in data:
        out["entitlement_arn"] = data["entitlementArn"]
    return out

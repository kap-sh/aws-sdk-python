"""Generated from Smithy shape ``com.amazonaws.iot#DescribeBillingGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.billing_group_name


class DescribeBillingGroupRequest(TypedDict, closed=True):
    billing_group_name: "capo_iot.types.billing_group_name.BillingGroupName"
    """<p>The name of the billing group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeBillingGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeBillingGroupRequest:
    out: DescribeBillingGroupRequest = {}  # type: ignore[typeddict-item]
    return out

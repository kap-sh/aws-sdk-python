"""Generated from Smithy shape ``com.amazonaws.workmail#BookingOptions``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workmail.types.boolean


class BookingOptions(TypedDict):
    auto_accept_requests: "aws_sdk_workmail.types.boolean.Boolean"
    """<p>The resource's ability to automatically reply to requests. If disabled, delegates must be associated to the resource.</p>"""
    auto_decline_recurring_requests: "aws_sdk_workmail.types.boolean.Boolean"
    """<p>The resource's ability to automatically decline any recurring requests.</p>"""
    auto_decline_conflicting_requests: "aws_sdk_workmail.types.boolean.Boolean"
    """<p>The resource's ability to automatically decline any conflicting requests.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BookingOptions) -> dict:
    out: dict = {}
    out["AutoAcceptRequests"] = value.get("auto_accept_requests", False)
    out["AutoDeclineRecurringRequests"] = value.get(
        "auto_decline_recurring_requests", False
    )
    out["AutoDeclineConflictingRequests"] = value.get(
        "auto_decline_conflicting_requests", False
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BookingOptions:
    out: BookingOptions = {}  # type: ignore[typeddict-item]
    if "AutoAcceptRequests" in data:
        out["auto_accept_requests"] = data["AutoAcceptRequests"]
    else:
        out["auto_accept_requests"] = False
    if "AutoDeclineRecurringRequests" in data:
        out["auto_decline_recurring_requests"] = data["AutoDeclineRecurringRequests"]
    else:
        out["auto_decline_recurring_requests"] = False
    if "AutoDeclineConflictingRequests" in data:
        out["auto_decline_conflicting_requests"] = data[
            "AutoDeclineConflictingRequests"
        ]
    else:
        out["auto_decline_conflicting_requests"] = False
    return out

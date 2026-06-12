"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ResaleAuthorizationAvailabilityEndDateFilterDateRange``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.date_time_iso8601


class ResaleAuthorizationAvailabilityEndDateFilterDateRange(TypedDict):
    after_value: NotRequired[
        "aws_sdk_marketplace_catalog.types.date_time_iso8601.DateTimeISO8601"
    ]
    """<p>Allows filtering on <code>AvailabilityEndDate</code> of a ResaleAuthorization after a date.</p>"""
    before_value: NotRequired[
        "aws_sdk_marketplace_catalog.types.date_time_iso8601.DateTimeISO8601"
    ]
    """<p>Allows filtering on <code>AvailabilityEndDate</code> of a ResaleAuthorization before a date.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: ResaleAuthorizationAvailabilityEndDateFilterDateRange,
) -> dict:
    out: dict = {}
    if "after_value" in value:
        out["AfterValue"] = value["after_value"]
    if "before_value" in value:
        out["BeforeValue"] = value["before_value"]
    return out


def deserialize_json(
    data: dict,
) -> ResaleAuthorizationAvailabilityEndDateFilterDateRange:
    out: ResaleAuthorizationAvailabilityEndDateFilterDateRange = {}  # type: ignore[typeddict-item]
    if "AfterValue" in data:
        out["after_value"] = data["AfterValue"]
    if "BeforeValue" in data:
        out["before_value"] = data["BeforeValue"]
    return out

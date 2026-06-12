"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ResaleAuthorizationAvailabilityEndDateFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.resale_authorization_availability_end_date_filter_date_range
    import aws_sdk_marketplace_catalog.types.resale_authorization_availability_end_date_filter_value_list


class ResaleAuthorizationAvailabilityEndDateFilter(TypedDict):
    date_range: NotRequired[
        "aws_sdk_marketplace_catalog.types.resale_authorization_availability_end_date_filter_date_range.ResaleAuthorizationAvailabilityEndDateFilterDateRange"
    ]
    """<p>Allows filtering on <code>AvailabilityEndDate</code> of a ResaleAuthorization with date range as input</p>"""
    value_list: NotRequired[
        "aws_sdk_marketplace_catalog.types.resale_authorization_availability_end_date_filter_value_list.ResaleAuthorizationAvailabilityEndDateFilterValueList"
    ]
    """<p>Allows filtering on <code>AvailabilityEndDate</code> of a ResaleAuthorization with date value as input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResaleAuthorizationAvailabilityEndDateFilter) -> dict:
    out: dict = {}
    if "date_range" in value:
        import aws_sdk_marketplace_catalog.types.resale_authorization_availability_end_date_filter_date_range

        out["DateRange"] = (
            aws_sdk_marketplace_catalog.types.resale_authorization_availability_end_date_filter_date_range.serialize_json(
                value["date_range"]
            )
        )
    if "value_list" in value:
        import aws_sdk_marketplace_catalog.types.resale_authorization_availability_end_date_filter_value_list

        out["ValueList"] = (
            aws_sdk_marketplace_catalog.types.resale_authorization_availability_end_date_filter_value_list.serialize_json(
                value["value_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResaleAuthorizationAvailabilityEndDateFilter:
    out: ResaleAuthorizationAvailabilityEndDateFilter = {}  # type: ignore[typeddict-item]
    if "DateRange" in data:
        import aws_sdk_marketplace_catalog.types.resale_authorization_availability_end_date_filter_date_range

        out["date_range"] = (
            aws_sdk_marketplace_catalog.types.resale_authorization_availability_end_date_filter_date_range.deserialize_json(
                data["DateRange"]
            )
        )
    if "ValueList" in data:
        import aws_sdk_marketplace_catalog.types.resale_authorization_availability_end_date_filter_value_list

        out["value_list"] = (
            aws_sdk_marketplace_catalog.types.resale_authorization_availability_end_date_filter_value_list.deserialize_json(
                data["ValueList"]
            )
        )
    return out

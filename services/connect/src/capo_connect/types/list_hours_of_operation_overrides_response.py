"""Generated from Smithy shape ``com.amazonaws.connect#ListHoursOfOperationOverridesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.hours_of_operation_override_list
    import capo_connect.types.next_token
    import capo_connect.types.region_name
    import capo_connect.types.timestamp


class ListHoursOfOperationOverridesResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    hours_of_operation_override_list: NotRequired[
        "capo_connect.types.hours_of_operation_override_list.HoursOfOperationOverrideList"
    ]
    """<p>Information about the hours of operation override.</p>"""
    last_modified_region: NotRequired["capo_connect.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region where this resource was last modified.</p>"""
    last_modified_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when this resource was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListHoursOfOperationOverridesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "hours_of_operation_override_list" in value:
        import capo_connect.types.hours_of_operation_override_list

        out["HoursOfOperationOverrideList"] = (
            capo_connect.types.hours_of_operation_override_list.serialize_json(
                value["hours_of_operation_override_list"]
            )
        )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    if "last_modified_time" in value:
        import capo_connect.types.timestamp

        out["LastModifiedTime"] = capo_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    return out


def deserialize_json(data: dict) -> ListHoursOfOperationOverridesResponse:
    out: ListHoursOfOperationOverridesResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "HoursOfOperationOverrideList" in data:
        import capo_connect.types.hours_of_operation_override_list

        out["hours_of_operation_override_list"] = (
            capo_connect.types.hours_of_operation_override_list.deserialize_json(
                data["HoursOfOperationOverrideList"]
            )
        )
    if "LastModifiedRegion" in data:
        out["last_modified_region"] = data["LastModifiedRegion"]
    if "LastModifiedTime" in data:
        import capo_connect.types.timestamp

        out["last_modified_time"] = capo_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    return out

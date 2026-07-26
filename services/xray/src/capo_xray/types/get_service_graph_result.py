"""Generated from Smithy shape ``com.amazonaws.xray#GetServiceGraphResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.boolean
    import capo_xray.types.service_list
    import capo_xray.types.string
    import capo_xray.types.timestamp


class GetServiceGraphResult(TypedDict, closed=True):
    start_time: NotRequired["capo_xray.types.timestamp.Timestamp"]
    """<p>The start of the time frame for which the graph was generated.</p>"""
    end_time: NotRequired["capo_xray.types.timestamp.Timestamp"]
    """<p>The end of the time frame for which the graph was generated.</p>"""
    services: NotRequired["capo_xray.types.service_list.ServiceList"]
    """<p>The services that have processed a traced request during the specified time frame.</p>"""
    contains_old_group_versions: "capo_xray.types.boolean.Boolean"
    """<p>A flag indicating whether the group's filter expression has been consistent, or if the returned service graph may show traces from an older version of the group's filter expression.</p>"""
    next_token: NotRequired["capo_xray.types.string.String"]
    """<p>Pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetServiceGraphResult) -> dict:
    out: dict = {}
    if "start_time" in value:
        import capo_xray.types.timestamp

        out["StartTime"] = capo_xray.types.timestamp.serialize_json(value["start_time"])
    if "end_time" in value:
        import capo_xray.types.timestamp

        out["EndTime"] = capo_xray.types.timestamp.serialize_json(value["end_time"])
    if "services" in value:
        import capo_xray.types.service_list

        out["Services"] = capo_xray.types.service_list.serialize_json(value["services"])
    out["ContainsOldGroupVersions"] = value.get("contains_old_group_versions", False)
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetServiceGraphResult:
    out: GetServiceGraphResult = {}  # type: ignore[typeddict-item]
    if "StartTime" in data:
        import capo_xray.types.timestamp

        out["start_time"] = capo_xray.types.timestamp.deserialize_json(
            data["StartTime"]
        )
    if "EndTime" in data:
        import capo_xray.types.timestamp

        out["end_time"] = capo_xray.types.timestamp.deserialize_json(data["EndTime"])
    if "Services" in data:
        import capo_xray.types.service_list

        out["services"] = capo_xray.types.service_list.deserialize_json(
            data["Services"]
        )
    if "ContainsOldGroupVersions" in data:
        out["contains_old_group_versions"] = data["ContainsOldGroupVersions"]
    else:
        out["contains_old_group_versions"] = False
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

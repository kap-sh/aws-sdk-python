"""Generated from Smithy shape ``com.amazonaws.connect#ListSecurityProfileFlowModulesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.allowed_flow_modules
    import capo_connect.types.next_token
    import capo_connect.types.region_name
    import capo_connect.types.timestamp


class ListSecurityProfileFlowModulesResponse(TypedDict, closed=True):
    allowed_flow_modules: NotRequired[
        "capo_connect.types.allowed_flow_modules.AllowedFlowModules"
    ]
    """<p> A list of Flow Modules an AI Agent can invoke as a tool. </p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p> The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>"""
    last_modified_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p> The time the flow module was last modified. </p>"""
    last_modified_region: NotRequired["capo_connect.types.region_name.RegionName"]
    """<p> The Region that flow module was last modified in. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSecurityProfileFlowModulesResponse) -> dict:
    out: dict = {}
    if "allowed_flow_modules" in value:
        import capo_connect.types.allowed_flow_modules

        out["AllowedFlowModules"] = (
            capo_connect.types.allowed_flow_modules.serialize_json(
                value["allowed_flow_modules"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "last_modified_time" in value:
        import capo_connect.types.timestamp

        out["LastModifiedTime"] = capo_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    return out


def deserialize_json(data: dict) -> ListSecurityProfileFlowModulesResponse:
    out: ListSecurityProfileFlowModulesResponse = {}  # type: ignore[typeddict-item]
    if "AllowedFlowModules" in data:
        import capo_connect.types.allowed_flow_modules

        out["allowed_flow_modules"] = (
            capo_connect.types.allowed_flow_modules.deserialize_json(
                data["AllowedFlowModules"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "LastModifiedTime" in data:
        import capo_connect.types.timestamp

        out["last_modified_time"] = capo_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if "LastModifiedRegion" in data:
        out["last_modified_region"] = data["LastModifiedRegion"]
    return out

"""Generated from Smithy shape ``com.amazonaws.evs#ListEnvironmentVlansResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_evs.types.pagination_token
    import capo_evs.types.vlan_list


class ListEnvironmentVlansResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_evs.types.pagination_token.PaginationToken"]
    """<p>A unique pagination token for next page results. Make the call again using this token to retrieve the next page.</p>"""
    environment_vlans: NotRequired["capo_evs.types.vlan_list.VlanList"]
    """<p>A list of VLANs that are associated with the specified environment.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListEnvironmentVlansResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "environment_vlans" in value:
        import capo_evs.types.vlan_list

        out["environmentVlans"] = capo_evs.types.vlan_list.serialize_aws_json_1_0(
            value["environment_vlans"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListEnvironmentVlansResponse:
    out: ListEnvironmentVlansResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "environmentVlans" in data:
        import capo_evs.types.vlan_list

        out["environment_vlans"] = capo_evs.types.vlan_list.deserialize_aws_json_1_0(
            data["environmentVlans"]
        )
    return out

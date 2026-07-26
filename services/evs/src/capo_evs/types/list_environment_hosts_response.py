"""Generated from Smithy shape ``com.amazonaws.evs#ListEnvironmentHostsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_evs.types.host_list
    import capo_evs.types.pagination_token


class ListEnvironmentHostsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_evs.types.pagination_token.PaginationToken"]
    """<p>A unique pagination token for next page results. Make the call again using this token to retrieve the next page.</p>"""
    environment_hosts: NotRequired["capo_evs.types.host_list.HostList"]
    """<p>A list of hosts in the environment.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListEnvironmentHostsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "environment_hosts" in value:
        import capo_evs.types.host_list

        out["environmentHosts"] = capo_evs.types.host_list.serialize_aws_json_1_0(
            value["environment_hosts"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListEnvironmentHostsResponse:
    out: ListEnvironmentHostsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "environmentHosts" in data:
        import capo_evs.types.host_list

        out["environment_hosts"] = capo_evs.types.host_list.deserialize_aws_json_1_0(
            data["environmentHosts"]
        )
    return out

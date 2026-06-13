"""Generated from Smithy shape ``com.amazonaws.evs#ListEnvironmentHostsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_evs.types.host_list
    import aws_sdk_evs.types.pagination_token


class ListEnvironmentHostsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_evs.types.pagination_token.PaginationToken"]
    """<p>A unique pagination token for next page results. Make the call again using this token to retrieve the next page.</p>"""
    environment_hosts: NotRequired["aws_sdk_evs.types.host_list.HostList"]
    """<p>A list of hosts in the environment.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListEnvironmentHostsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "environment_hosts" in value:
        import aws_sdk_evs.types.host_list

        out["environmentHosts"] = aws_sdk_evs.types.host_list.serialize_aws_json_1_0(
            value["environment_hosts"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListEnvironmentHostsResponse:
    out: ListEnvironmentHostsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "environmentHosts" in data:
        import aws_sdk_evs.types.host_list

        out["environment_hosts"] = aws_sdk_evs.types.host_list.deserialize_aws_json_1_0(
            data["environmentHosts"]
        )
    return out

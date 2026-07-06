"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#ListServerNeighborsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_application_discovery_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.long
    import aws_sdk_application_discovery_service.types.neighbor_details_list
    import aws_sdk_application_discovery_service.types.string


class ListServerNeighborsResponse(TypedDict, closed=True):
    neighbors: "aws_sdk_application_discovery_service.types.neighbor_details_list.NeighborDetailsList"
    """<p>List of distinct servers that are one hop away from the given server.</p>"""
    next_token: NotRequired["aws_sdk_application_discovery_service.types.string.String"]
    """<p>Token to retrieve the next set of results. For example, if you specified 100 IDs for <code>ListServerNeighborsRequest$neighborConfigurationIds</code> but set <code>ListServerNeighborsRequest$maxResults</code> to 10, you received a set of 10 results along with this token. Use this token in the next query to retrieve the next set of 10.</p>"""
    known_dependency_count: "aws_sdk_application_discovery_service.types.long.Long"
    """<p>Count of distinct servers that are one hop away from the given server.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListServerNeighborsResponse) -> dict:
    out: dict = {}
    import aws_sdk_application_discovery_service.types.neighbor_details_list

    out["neighbors"] = (
        aws_sdk_application_discovery_service.types.neighbor_details_list.serialize_aws_json_1_1(
            value["neighbors"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    out["knownDependencyCount"] = value.get("known_dependency_count", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> ListServerNeighborsResponse:
    out: ListServerNeighborsResponse = {}  # type: ignore[typeddict-item]
    if "neighbors" in data:
        import aws_sdk_application_discovery_service.types.neighbor_details_list

        out["neighbors"] = (
            aws_sdk_application_discovery_service.types.neighbor_details_list.deserialize_aws_json_1_1(
                data["neighbors"]
            )
        )
    else:
        raise DeserializationError("ListServerNeighborsResponse.neighbors required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "knownDependencyCount" in data:
        out["known_dependency_count"] = data["knownDependencyCount"]
    else:
        out["known_dependency_count"] = 0
    return out

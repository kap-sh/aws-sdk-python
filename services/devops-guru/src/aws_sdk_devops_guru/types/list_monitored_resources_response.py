"""Generated from Smithy shape ``com.amazonaws.devopsguru#ListMonitoredResourcesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_devops_guru.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.monitored_resource_identifiers
    import aws_sdk_devops_guru.types.uuid_next_token


class ListMonitoredResourcesResponse(TypedDict):
    monitored_resource_identifiers: "aws_sdk_devops_guru.types.monitored_resource_identifiers.MonitoredResourceIdentifiers"
    """<p> Information about the resource that is being monitored, including the name of the resource, the type of resource, and whether or not permission is given to DevOps Guru to access that resource. </p>"""
    next_token: NotRequired["aws_sdk_devops_guru.types.uuid_next_token.UuidNextToken"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMonitoredResourcesResponse) -> dict:
    out: dict = {}
    import aws_sdk_devops_guru.types.monitored_resource_identifiers

    out["MonitoredResourceIdentifiers"] = (
        aws_sdk_devops_guru.types.monitored_resource_identifiers.serialize_json(
            value["monitored_resource_identifiers"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMonitoredResourcesResponse:
    out: ListMonitoredResourcesResponse = {}  # type: ignore[typeddict-item]
    if "MonitoredResourceIdentifiers" in data:
        import aws_sdk_devops_guru.types.monitored_resource_identifiers

        out["monitored_resource_identifiers"] = (
            aws_sdk_devops_guru.types.monitored_resource_identifiers.deserialize_json(
                data["MonitoredResourceIdentifiers"]
            )
        )
    else:
        raise DeserializationError(
            "ListMonitoredResourcesResponse.monitored_resource_identifiers required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

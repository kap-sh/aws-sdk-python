"""Generated from Smithy shape ``com.amazonaws.configservice#ListDiscoveredResourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.next_token
    import capo_config_service.types.resource_identifier_list


class ListDiscoveredResourcesResponse(TypedDict, closed=True):
    resource_identifiers: NotRequired[
        "capo_config_service.types.resource_identifier_list.ResourceIdentifierList"
    ]
    """<p>The details that identify a resource that is discovered by Config, including the resource type, ID, and (if available) the custom resource name.</p>"""
    next_token: NotRequired["capo_config_service.types.next_token.NextToken"]
    """<p>The string that you use in a subsequent request to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDiscoveredResourcesResponse) -> dict:
    out: dict = {}
    if "resource_identifiers" in value:
        import capo_config_service.types.resource_identifier_list

        out["resourceIdentifiers"] = (
            capo_config_service.types.resource_identifier_list.serialize_aws_json_1_1(
                value["resource_identifiers"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDiscoveredResourcesResponse:
    out: ListDiscoveredResourcesResponse = {}  # type: ignore[typeddict-item]
    if "resourceIdentifiers" in data:
        import capo_config_service.types.resource_identifier_list

        out["resource_identifiers"] = (
            capo_config_service.types.resource_identifier_list.deserialize_aws_json_1_1(
                data["resourceIdentifiers"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out

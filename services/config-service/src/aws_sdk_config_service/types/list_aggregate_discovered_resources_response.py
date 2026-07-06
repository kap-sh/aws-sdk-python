"""Generated from Smithy shape ``com.amazonaws.configservice#ListAggregateDiscoveredResourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.discovered_resource_identifier_list
    import aws_sdk_config_service.types.next_token


class ListAggregateDiscoveredResourcesResponse(TypedDict, closed=True):
    resource_identifiers: NotRequired[
        "aws_sdk_config_service.types.discovered_resource_identifier_list.DiscoveredResourceIdentifierList"
    ]
    """<p>Returns a list of <code>ResourceIdentifiers</code> objects.</p>"""
    next_token: NotRequired["aws_sdk_config_service.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAggregateDiscoveredResourcesResponse) -> dict:
    out: dict = {}
    if "resource_identifiers" in value:
        import aws_sdk_config_service.types.discovered_resource_identifier_list

        out["ResourceIdentifiers"] = (
            aws_sdk_config_service.types.discovered_resource_identifier_list.serialize_aws_json_1_1(
                value["resource_identifiers"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAggregateDiscoveredResourcesResponse:
    out: ListAggregateDiscoveredResourcesResponse = {}  # type: ignore[typeddict-item]
    if "ResourceIdentifiers" in data:
        import aws_sdk_config_service.types.discovered_resource_identifier_list

        out["resource_identifiers"] = (
            aws_sdk_config_service.types.discovered_resource_identifier_list.deserialize_aws_json_1_1(
                data["ResourceIdentifiers"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

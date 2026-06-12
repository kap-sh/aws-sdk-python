"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#SearchEntitiesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotthingsgraph.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.entity_filters
    import aws_sdk_iotthingsgraph.types.entity_types
    import aws_sdk_iotthingsgraph.types.max_results
    import aws_sdk_iotthingsgraph.types.next_token
    import aws_sdk_iotthingsgraph.types.version


class SearchEntitiesRequest(TypedDict):
    entity_types: "aws_sdk_iotthingsgraph.types.entity_types.EntityTypes"
    """<p>The entity types for which to search.</p>"""
    filters: NotRequired["aws_sdk_iotthingsgraph.types.entity_filters.EntityFilters"]
    """<p>Optional filter to apply to the search. Valid filters are <code>NAME</code> <code>NAMESPACE</code>, <code>SEMANTIC_TYPE_PATH</code> and <code>REFERENCED_ENTITY_ID</code>. <code>REFERENCED_ENTITY_ID</code> filters on entities that are used by the entity in the result set. For example, you can filter on the ID of a property that is used in a state.</p> <p>Multiple filters function as OR criteria in the query. Multiple values passed inside the filter function as AND criteria.</p>"""
    next_token: NotRequired["aws_sdk_iotthingsgraph.types.next_token.NextToken"]
    """<p>The string that specifies the next page of results. Use this when you're paginating results.</p>"""
    max_results: NotRequired["aws_sdk_iotthingsgraph.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response.</p>"""
    namespace_version: NotRequired["aws_sdk_iotthingsgraph.types.version.Version"]
    """<p>The version of the user's namespace. Defaults to the latest version of the user's namespace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchEntitiesRequest) -> dict:
    out: dict = {}
    import aws_sdk_iotthingsgraph.types.entity_types

    out["entityTypes"] = (
        aws_sdk_iotthingsgraph.types.entity_types.serialize_aws_json_1_1(
            value["entity_types"]
        )
    )
    if "filters" in value:
        import aws_sdk_iotthingsgraph.types.entity_filters

        out["filters"] = (
            aws_sdk_iotthingsgraph.types.entity_filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "namespace_version" in value:
        out["namespaceVersion"] = value["namespace_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchEntitiesRequest:
    out: SearchEntitiesRequest = {}  # type: ignore[typeddict-item]
    if "entityTypes" in data:
        import aws_sdk_iotthingsgraph.types.entity_types

        out["entity_types"] = (
            aws_sdk_iotthingsgraph.types.entity_types.deserialize_aws_json_1_1(
                data["entityTypes"]
            )
        )
    else:
        raise DeserializationError("SearchEntitiesRequest.entity_types required")
    if "filters" in data:
        import aws_sdk_iotthingsgraph.types.entity_filters

        out["filters"] = (
            aws_sdk_iotthingsgraph.types.entity_filters.deserialize_aws_json_1_1(
                data["filters"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "namespaceVersion" in data:
        out["namespace_version"] = data["namespaceVersion"]
    return out

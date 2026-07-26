"""Generated from Smithy shape ``com.amazonaws.glue#ListEntitiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.api_version
    import capo_glue.types.catalog_id_string
    import capo_glue.types.entity_name
    import capo_glue.types.name_string
    import capo_glue.types.next_token


class ListEntitiesRequest(TypedDict, closed=True):
    connection_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>A name for the connection that has required credentials to query any connection type.</p>"""
    catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The catalog ID of the catalog that contains the connection. This can be null, By default, the Amazon Web Services Account ID is the catalog ID.</p>"""
    parent_entity_name: NotRequired["capo_glue.types.entity_name.EntityName"]
    """<p>Name of the parent entity for which you want to list the children. This parameter takes a fully-qualified path of the entity in order to list the child entities.</p>"""
    next_token: NotRequired["capo_glue.types.next_token.NextToken"]
    """<p>A continuation token, included if this is a continuation call.</p>"""
    data_store_api_version: NotRequired["capo_glue.types.api_version.ApiVersion"]
    """<p>The API version of the SaaS connector.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEntitiesRequest) -> dict:
    out: dict = {}
    if "connection_name" in value:
        out["ConnectionName"] = value["connection_name"]
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    if "parent_entity_name" in value:
        out["ParentEntityName"] = value["parent_entity_name"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "data_store_api_version" in value:
        out["DataStoreApiVersion"] = value["data_store_api_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEntitiesRequest:
    out: ListEntitiesRequest = {}  # type: ignore[typeddict-item]
    if "ConnectionName" in data:
        out["connection_name"] = data["ConnectionName"]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "ParentEntityName" in data:
        out["parent_entity_name"] = data["ParentEntityName"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "DataStoreApiVersion" in data:
        out["data_store_api_version"] = data["DataStoreApiVersion"]
    return out

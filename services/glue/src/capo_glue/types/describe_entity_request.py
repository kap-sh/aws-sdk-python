"""Generated from Smithy shape ``com.amazonaws.glue#DescribeEntityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.api_version
    import capo_glue.types.catalog_id_string
    import capo_glue.types.entity_name
    import capo_glue.types.name_string
    import capo_glue.types.next_token


class DescribeEntityRequest(TypedDict, closed=True):
    connection_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the connection that contains the connection type credentials.</p>"""
    catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The catalog ID of the catalog that contains the connection. This can be null, By default, the Amazon Web Services Account ID is the catalog ID.</p>"""
    entity_name: "capo_glue.types.entity_name.EntityName"
    """<p>The name of the entity that you want to describe from the connection type.</p>"""
    next_token: NotRequired["capo_glue.types.next_token.NextToken"]
    """<p>A continuation token, included if this is a continuation call.</p>"""
    data_store_api_version: NotRequired["capo_glue.types.api_version.ApiVersion"]
    """<p>The version of the API used for the data store.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEntityRequest) -> dict:
    out: dict = {}
    out["ConnectionName"] = value["connection_name"]
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["EntityName"] = value["entity_name"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "data_store_api_version" in value:
        out["DataStoreApiVersion"] = value["data_store_api_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEntityRequest:
    out: DescribeEntityRequest = {}  # type: ignore[typeddict-item]
    if "ConnectionName" in data:
        out["connection_name"] = data["ConnectionName"]
    else:
        raise DeserializationError("DescribeEntityRequest.connection_name required")
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "EntityName" in data:
        out["entity_name"] = data["EntityName"]
    else:
        raise DeserializationError("DescribeEntityRequest.entity_name required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "DataStoreApiVersion" in data:
        out["data_store_api_version"] = data["DataStoreApiVersion"]
    return out

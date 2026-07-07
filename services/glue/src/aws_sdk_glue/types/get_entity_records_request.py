"""Generated from Smithy shape ``com.amazonaws.glue#GetEntityRecordsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.api_version
    import aws_sdk_glue.types.catalog_id_string
    import aws_sdk_glue.types.connection_options
    import aws_sdk_glue.types.entity_name
    import aws_sdk_glue.types.filter_predicate
    import aws_sdk_glue.types.limit
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.next_token
    import aws_sdk_glue.types.selected_fields


class GetEntityRecordsRequest(TypedDict, closed=True):
    connection_name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The name of the connection that contains the connection type credentials.</p>"""
    catalog_id: NotRequired["aws_sdk_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The catalog ID of the catalog that contains the connection. This can be null, By default, the Amazon Web Services Account ID is the catalog ID.</p>"""
    entity_name: "aws_sdk_glue.types.entity_name.EntityName"
    """<p>Name of the entity that we want to query the preview data from the given connection type.</p>"""
    next_token: NotRequired["aws_sdk_glue.types.next_token.NextToken"]
    """<p>A continuation token, included if this is a continuation call.</p>"""
    data_store_api_version: NotRequired["aws_sdk_glue.types.api_version.ApiVersion"]
    """<p>The API version of the SaaS connector.</p>"""
    connection_options: NotRequired[
        "aws_sdk_glue.types.connection_options.ConnectionOptions"
    ]
    """<p>Connector options that are required to query the data.</p>"""
    filter_predicate: NotRequired["aws_sdk_glue.types.filter_predicate.FilterPredicate"]
    """<p>A filter predicate that you can apply in the query request.</p>"""
    limit: "aws_sdk_glue.types.limit.Limit"
    """<p>Limits the number of records fetched with the request.</p>"""
    order_by: NotRequired["str"]
    """<p>A parameter that orders the response preview data.</p>"""
    selected_fields: NotRequired["aws_sdk_glue.types.selected_fields.SelectedFields"]
    """<p> List of fields that we want to fetch as part of preview data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetEntityRecordsRequest) -> dict:
    out: dict = {}
    if "connection_name" in value:
        out["ConnectionName"] = value["connection_name"]
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["EntityName"] = value["entity_name"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "data_store_api_version" in value:
        out["DataStoreApiVersion"] = value["data_store_api_version"]
    if "connection_options" in value:
        import aws_sdk_glue.types.connection_options

        out["ConnectionOptions"] = (
            aws_sdk_glue.types.connection_options.serialize_aws_json_1_1(
                value["connection_options"]
            )
        )
    if "filter_predicate" in value:
        out["FilterPredicate"] = value["filter_predicate"]
    out["Limit"] = value["limit"]
    if "order_by" in value:
        out["OrderBy"] = value["order_by"]
    if "selected_fields" in value:
        import aws_sdk_glue.types.selected_fields

        out["SelectedFields"] = (
            aws_sdk_glue.types.selected_fields.serialize_aws_json_1_1(
                value["selected_fields"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetEntityRecordsRequest:
    out: GetEntityRecordsRequest = {}  # type: ignore[typeddict-item]
    if "ConnectionName" in data:
        out["connection_name"] = data["ConnectionName"]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "EntityName" in data:
        out["entity_name"] = data["EntityName"]
    else:
        raise DeserializationError("GetEntityRecordsRequest.entity_name required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "DataStoreApiVersion" in data:
        out["data_store_api_version"] = data["DataStoreApiVersion"]
    if "ConnectionOptions" in data:
        import aws_sdk_glue.types.connection_options

        out["connection_options"] = (
            aws_sdk_glue.types.connection_options.deserialize_aws_json_1_1(
                data["ConnectionOptions"]
            )
        )
    if "FilterPredicate" in data:
        out["filter_predicate"] = data["FilterPredicate"]
    if "Limit" in data:
        out["limit"] = data["Limit"]
    else:
        raise DeserializationError("GetEntityRecordsRequest.limit required")
    if "OrderBy" in data:
        out["order_by"] = data["OrderBy"]
    if "SelectedFields" in data:
        import aws_sdk_glue.types.selected_fields

        out["selected_fields"] = (
            aws_sdk_glue.types.selected_fields.deserialize_aws_json_1_1(
                data["SelectedFields"]
            )
        )
    return out

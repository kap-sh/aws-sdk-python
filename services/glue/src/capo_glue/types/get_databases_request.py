"""Generated from Smithy shape ``com.amazonaws.glue#GetDatabasesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.catalog_getter_page_size
    import capo_glue.types.catalog_id_string
    import capo_glue.types.database_attributes_list
    import capo_glue.types.resource_share_type
    import capo_glue.types.token


class GetDatabasesRequest(TypedDict, closed=True):
    catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog from which to retrieve <code>Databases</code>. If none is provided, the Amazon Web Services account ID is used by default.</p>"""
    next_token: NotRequired["capo_glue.types.token.Token"]
    """<p>A continuation token, if this is a continuation call.</p>"""
    max_results: NotRequired[
        "capo_glue.types.catalog_getter_page_size.CatalogGetterPageSize"
    ]
    """<p>The maximum number of databases to return in one response.</p>"""
    resource_share_type: NotRequired[
        "capo_glue.types.resource_share_type.ResourceShareType"
    ]
    """<p>Allows you to specify that you want to list the databases shared with your account. The allowable values are <code>FEDERATED</code>, <code>FOREIGN</code> or <code>ALL</code>. </p> <ul> <li> <p>If set to <code>FEDERATED</code>, will list the federated databases (referencing an external entity) shared with your account.</p> </li> <li> <p>If set to <code>FOREIGN</code>, will list the databases shared with your account. </p> </li> <li> <p>If set to <code>ALL</code>, will list the databases shared with your account, as well as the databases in yor local account. </p> </li> </ul>"""
    attributes_to_get: NotRequired[
        "capo_glue.types.database_attributes_list.DatabaseAttributesList"
    ]
    """<p>Specifies the database fields returned by the <code>GetDatabases</code> call. This parameter doesn’t accept an empty list. The request must include the <code>NAME</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDatabasesRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "resource_share_type" in value:
        import capo_glue.types.resource_share_type

        out["ResourceShareType"] = (
            capo_glue.types.resource_share_type.serialize_aws_json_1_1(
                value["resource_share_type"]
            )
        )
    if "attributes_to_get" in value:
        import capo_glue.types.database_attributes_list

        out["AttributesToGet"] = (
            capo_glue.types.database_attributes_list.serialize_aws_json_1_1(
                value["attributes_to_get"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDatabasesRequest:
    out: GetDatabasesRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "ResourceShareType" in data:
        import capo_glue.types.resource_share_type

        out["resource_share_type"] = (
            capo_glue.types.resource_share_type.deserialize_aws_json_1_1(
                data["ResourceShareType"]
            )
        )
    if "AttributesToGet" in data:
        import capo_glue.types.database_attributes_list

        out["attributes_to_get"] = (
            capo_glue.types.database_attributes_list.deserialize_aws_json_1_1(
                data["AttributesToGet"]
            )
        )
    return out

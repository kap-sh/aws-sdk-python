"""Generated from Smithy shape ``com.amazonaws.lakeformation#ListPermissionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.catalog_id_string
    import capo_lakeformation.types.data_lake_principal
    import capo_lakeformation.types.data_lake_resource_type
    import capo_lakeformation.types.page_size
    import capo_lakeformation.types.resource
    import capo_lakeformation.types.token
    import capo_lakeformation.types.true_false_string


class ListPermissionsRequest(TypedDict, closed=True):
    catalog_id: NotRequired[
        "capo_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment. </p>"""
    principal: NotRequired[
        "capo_lakeformation.types.data_lake_principal.DataLakePrincipal"
    ]
    """<p>Specifies a principal to filter the permissions returned.</p>"""
    resource_type: NotRequired[
        "capo_lakeformation.types.data_lake_resource_type.DataLakeResourceType"
    ]
    """<p>Specifies a resource type to filter the permissions returned.</p>"""
    resource: NotRequired["capo_lakeformation.types.resource.Resource"]
    """<p>A resource where you will get a list of the principal permissions.</p> <p>This operation does not support getting privileges on a table with columns. Instead, call this operation on the table, and the operation returns the table and the table w columns.</p>"""
    next_token: NotRequired["capo_lakeformation.types.token.Token"]
    """<p>A continuation token, if this is not the first call to retrieve this list.</p>"""
    max_results: NotRequired["capo_lakeformation.types.page_size.PageSize"]
    """<p>The maximum number of results to return.</p>"""
    include_related: NotRequired[
        "capo_lakeformation.types.true_false_string.TrueFalseString"
    ]
    """<p>Indicates that related permissions should be included in the results when listing permissions on a table resource.</p> <p>Set the field to <code>TRUE</code> to show the cell filters on a table resource. Default is <code>FALSE</code>. The Principal parameter must not be specified when requesting cell filter information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPermissionsRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    if "principal" in value:
        import capo_lakeformation.types.data_lake_principal

        out["Principal"] = capo_lakeformation.types.data_lake_principal.serialize_json(
            value["principal"]
        )
    if "resource_type" in value:
        import capo_lakeformation.types.data_lake_resource_type

        out["ResourceType"] = (
            capo_lakeformation.types.data_lake_resource_type.serialize_json(
                value["resource_type"]
            )
        )
    if "resource" in value:
        import capo_lakeformation.types.resource

        out["Resource"] = capo_lakeformation.types.resource.serialize_json(
            value["resource"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "include_related" in value:
        out["IncludeRelated"] = value["include_related"]
    return out


def deserialize_json(data: dict) -> ListPermissionsRequest:
    out: ListPermissionsRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "Principal" in data:
        import capo_lakeformation.types.data_lake_principal

        out["principal"] = (
            capo_lakeformation.types.data_lake_principal.deserialize_json(
                data["Principal"]
            )
        )
    if "ResourceType" in data:
        import capo_lakeformation.types.data_lake_resource_type

        out["resource_type"] = (
            capo_lakeformation.types.data_lake_resource_type.deserialize_json(
                data["ResourceType"]
            )
        )
    if "Resource" in data:
        import capo_lakeformation.types.resource

        out["resource"] = capo_lakeformation.types.resource.deserialize_json(
            data["Resource"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "IncludeRelated" in data:
        out["include_related"] = data["IncludeRelated"]
    return out

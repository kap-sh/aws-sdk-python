"""Generated from Smithy shape ``com.amazonaws.lakeformation#GetResourceLFTagsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lakeformation.types.boolean_nullable
    import capo_lakeformation.types.catalog_id_string
    import capo_lakeformation.types.resource


class GetResourceLFTagsRequest(TypedDict, closed=True):
    catalog_id: NotRequired[
        "capo_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment. </p>"""
    resource: "capo_lakeformation.types.resource.Resource"
    """<p>The database, table, or column resource for which you want to return LF-tags.</p>"""
    show_assigned_lf_tags: NotRequired[
        "capo_lakeformation.types.boolean_nullable.BooleanNullable"
    ]
    """<p>Indicates whether to show the assigned LF-tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourceLFTagsRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    import capo_lakeformation.types.resource

    out["Resource"] = capo_lakeformation.types.resource.serialize_json(
        value["resource"]
    )
    if "show_assigned_lf_tags" in value:
        out["ShowAssignedLFTags"] = value["show_assigned_lf_tags"]
    return out


def deserialize_json(data: dict) -> GetResourceLFTagsRequest:
    out: GetResourceLFTagsRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "Resource" in data:
        import capo_lakeformation.types.resource

        out["resource"] = capo_lakeformation.types.resource.deserialize_json(
            data["Resource"]
        )
    else:
        raise DeserializationError("GetResourceLFTagsRequest.resource required")
    if "ShowAssignedLFTags" in data:
        out["show_assigned_lf_tags"] = data["ShowAssignedLFTags"]
    return out

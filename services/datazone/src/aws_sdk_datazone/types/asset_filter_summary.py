"""Generated from Smithy shape ``com.amazonaws.datazone#AssetFilterSummary``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_datazone.types.asset_id
    import aws_sdk_datazone.types.column_name_list
    import aws_sdk_datazone.types.created_at
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.filter_id
    import aws_sdk_datazone.types.filter_name
    import aws_sdk_datazone.types.filter_status

class AssetFilterSummary(TypedDict):
    id: "aws_sdk_datazone.types.filter_id.FilterId"
    """<p>The ID of the asset filter.</p>"""
    domain_id: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where the asset filter lives.</p>"""
    asset_id: "aws_sdk_datazone.types.asset_id.AssetId"
    """<p>The ID of the data asset.</p>"""
    name: "aws_sdk_datazone.types.filter_name.FilterName"
    """<p>The name of the asset filter.</p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>The description of the asset filter.</p>"""
    status: NotRequired["aws_sdk_datazone.types.filter_status.FilterStatus"]
    """<p>The status of the asset filter.</p>"""
    effective_column_names: NotRequired["aws_sdk_datazone.types.column_name_list.ColumnNameList"]
    """<p>The effective column names of the asset filter.</p>"""
    effective_row_filter: NotRequired["str"]
    """<p>The effective row filter of the asset filter.</p>"""
    created_at: NotRequired["aws_sdk_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp at which the asset filter was created.</p>"""
    error_message: NotRequired["str"]
    """<p>The error message that is displayed if the action does not succeed.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AssetFilterSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["domainId"] = value["domain_id"]
    out["assetId"] = value["asset_id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        import aws_sdk_datazone.types.filter_status
        out["status"] = aws_sdk_datazone.types.filter_status.serialize_json(value["status"])
    if "effective_column_names" in value:
        import aws_sdk_datazone.types.column_name_list
        out["effectiveColumnNames"] = aws_sdk_datazone.types.column_name_list.serialize_json(value["effective_column_names"])
    if "effective_row_filter" in value:
        out["effectiveRowFilter"] = value["effective_row_filter"]
    if "created_at" in value:
        import aws_sdk_datazone.types.created_at
        out["createdAt"] = aws_sdk_datazone.types.created_at.serialize_json(value["created_at"])
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> AssetFilterSummary:
    out: AssetFilterSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("AssetFilterSummary.id required")
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("AssetFilterSummary.domain_id required")
    if "assetId" in data:
        out["asset_id"] = data["assetId"]
    else:
        raise DeserializationError("AssetFilterSummary.asset_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AssetFilterSummary.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "status" in data:
        import aws_sdk_datazone.types.filter_status
        out["status"] = aws_sdk_datazone.types.filter_status.deserialize_json(data["status"])
    if "effectiveColumnNames" in data:
        import aws_sdk_datazone.types.column_name_list
        out["effective_column_names"] = aws_sdk_datazone.types.column_name_list.deserialize_json(data["effectiveColumnNames"])
    if "effectiveRowFilter" in data:
        out["effective_row_filter"] = data["effectiveRowFilter"]
    if "createdAt" in data:
        import aws_sdk_datazone.types.created_at
        out["created_at"] = aws_sdk_datazone.types.created_at.deserialize_json(data["createdAt"])
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
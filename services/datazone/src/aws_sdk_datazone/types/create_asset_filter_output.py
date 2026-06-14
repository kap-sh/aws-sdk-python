"""Generated from Smithy shape ``com.amazonaws.datazone#CreateAssetFilterOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.asset_filter_configuration
    import aws_sdk_datazone.types.asset_id
    import aws_sdk_datazone.types.column_name_list
    import aws_sdk_datazone.types.created_at
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.filter_id
    import aws_sdk_datazone.types.filter_name
    import aws_sdk_datazone.types.filter_status


class CreateAssetFilterOutput(TypedDict):
    id: "aws_sdk_datazone.types.filter_id.FilterId"
    """<p>The ID of the asset filter.</p>"""
    domain_id: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where the asset filter is created.</p>"""
    asset_id: "aws_sdk_datazone.types.asset_id.AssetId"
    """<p>The ID of the asset.</p>"""
    name: "aws_sdk_datazone.types.filter_name.FilterName"
    """<p>The name of the asset filter.</p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>The description of the asset filter.</p>"""
    status: NotRequired["aws_sdk_datazone.types.filter_status.FilterStatus"]
    """<p>The status of the asset filter.</p>"""
    configuration: (
        "aws_sdk_datazone.types.asset_filter_configuration.AssetFilterConfiguration"
    )
    """<p>The configuration of the asset filter.</p>"""
    created_at: NotRequired["aws_sdk_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp at which the asset filter was created.</p>"""
    error_message: NotRequired["str"]
    """<p>The error message that is displayed if the asset filter is not created successfully.</p>"""
    effective_column_names: NotRequired[
        "aws_sdk_datazone.types.column_name_list.ColumnNameList"
    ]
    """<p>The column names in the asset filter.</p>"""
    effective_row_filter: NotRequired["str"]
    """<p>The row filter in the asset filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssetFilterOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["domainId"] = value["domain_id"]
    out["assetId"] = value["asset_id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        import aws_sdk_datazone.types.filter_status

        out["status"] = aws_sdk_datazone.types.filter_status.serialize_json(
            value["status"]
        )
    import aws_sdk_datazone.types.asset_filter_configuration

    out["configuration"] = (
        aws_sdk_datazone.types.asset_filter_configuration.serialize_json(
            value["configuration"]
        )
    )
    if "created_at" in value:
        import aws_sdk_datazone.types.created_at

        out["createdAt"] = aws_sdk_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "effective_column_names" in value:
        import aws_sdk_datazone.types.column_name_list

        out["effectiveColumnNames"] = (
            aws_sdk_datazone.types.column_name_list.serialize_json(
                value["effective_column_names"]
            )
        )
    if "effective_row_filter" in value:
        out["effectiveRowFilter"] = value["effective_row_filter"]
    return out


def deserialize_json(data: dict) -> CreateAssetFilterOutput:
    out: CreateAssetFilterOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CreateAssetFilterOutput.id required")
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("CreateAssetFilterOutput.domain_id required")
    if "assetId" in data:
        out["asset_id"] = data["assetId"]
    else:
        raise DeserializationError("CreateAssetFilterOutput.asset_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateAssetFilterOutput.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "status" in data:
        import aws_sdk_datazone.types.filter_status

        out["status"] = aws_sdk_datazone.types.filter_status.deserialize_json(
            data["status"]
        )
    if "configuration" in data:
        import aws_sdk_datazone.types.asset_filter_configuration

        out["configuration"] = (
            aws_sdk_datazone.types.asset_filter_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError("CreateAssetFilterOutput.configuration required")
    if "createdAt" in data:
        import aws_sdk_datazone.types.created_at

        out["created_at"] = aws_sdk_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    if "effectiveColumnNames" in data:
        import aws_sdk_datazone.types.column_name_list

        out["effective_column_names"] = (
            aws_sdk_datazone.types.column_name_list.deserialize_json(
                data["effectiveColumnNames"]
            )
        )
    if "effectiveRowFilter" in data:
        out["effective_row_filter"] = data["effectiveRowFilter"]
    return out

"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#GetExportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.export_status
    import capo_lex_model_building_service.types.export_type
    import capo_lex_model_building_service.types.name
    import capo_lex_model_building_service.types.numerical_version
    import capo_lex_model_building_service.types.resource_type
    import capo_lex_model_building_service.types.string


class GetExportResponse(TypedDict, closed=True):
    name: NotRequired["capo_lex_model_building_service.types.name.Name"]
    """<p>The name of the bot being exported.</p>"""
    version: NotRequired[
        "capo_lex_model_building_service.types.numerical_version.NumericalVersion"
    ]
    """<p>The version of the bot being exported.</p>"""
    resource_type: NotRequired[
        "capo_lex_model_building_service.types.resource_type.ResourceType"
    ]
    """<p>The type of the exported resource.</p>"""
    export_type: NotRequired[
        "capo_lex_model_building_service.types.export_type.ExportType"
    ]
    """<p>The format of the exported data.</p>"""
    export_status: NotRequired[
        "capo_lex_model_building_service.types.export_status.ExportStatus"
    ]
    """<p>The status of the export. </p> <ul> <li> <p> <code>IN_PROGRESS</code> - The export is in progress.</p> </li> <li> <p> <code>READY</code> - The export is complete.</p> </li> <li> <p> <code>FAILED</code> - The export could not be completed.</p> </li> </ul>"""
    failure_reason: NotRequired["capo_lex_model_building_service.types.string.String"]
    """<p>If <code>status</code> is <code>FAILED</code>, Amazon Lex provides the reason that it failed to export the resource.</p>"""
    url: NotRequired["capo_lex_model_building_service.types.string.String"]
    """<p>An S3 pre-signed URL that provides the location of the exported resource. The exported resource is a ZIP archive that contains the exported resource in JSON format. The structure of the archive may change. Your code should not rely on the archive structure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetExportResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "version" in value:
        out["version"] = value["version"]
    if "resource_type" in value:
        import capo_lex_model_building_service.types.resource_type

        out["resourceType"] = (
            capo_lex_model_building_service.types.resource_type.serialize_json(
                value["resource_type"]
            )
        )
    if "export_type" in value:
        import capo_lex_model_building_service.types.export_type

        out["exportType"] = (
            capo_lex_model_building_service.types.export_type.serialize_json(
                value["export_type"]
            )
        )
    if "export_status" in value:
        import capo_lex_model_building_service.types.export_status

        out["exportStatus"] = (
            capo_lex_model_building_service.types.export_status.serialize_json(
                value["export_status"]
            )
        )
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    if "url" in value:
        out["url"] = value["url"]
    return out


def deserialize_json(data: dict) -> GetExportResponse:
    out: GetExportResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "version" in data:
        out["version"] = data["version"]
    if "resourceType" in data:
        import capo_lex_model_building_service.types.resource_type

        out["resource_type"] = (
            capo_lex_model_building_service.types.resource_type.deserialize_json(
                data["resourceType"]
            )
        )
    if "exportType" in data:
        import capo_lex_model_building_service.types.export_type

        out["export_type"] = (
            capo_lex_model_building_service.types.export_type.deserialize_json(
                data["exportType"]
            )
        )
    if "exportStatus" in data:
        import capo_lex_model_building_service.types.export_status

        out["export_status"] = (
            capo_lex_model_building_service.types.export_status.deserialize_json(
                data["exportStatus"]
            )
        )
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    if "url" in data:
        out["url"] = data["url"]
    return out

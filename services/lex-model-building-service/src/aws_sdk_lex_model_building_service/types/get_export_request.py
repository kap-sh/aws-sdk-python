"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#GetExportRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.export_type
    import aws_sdk_lex_model_building_service.types.name
    import aws_sdk_lex_model_building_service.types.numerical_version
    import aws_sdk_lex_model_building_service.types.resource_type


class GetExportRequest(TypedDict):
    name: "aws_sdk_lex_model_building_service.types.name.Name"
    """<p>The name of the bot to export.</p>"""
    version: (
        "aws_sdk_lex_model_building_service.types.numerical_version.NumericalVersion"
    )
    """<p>The version of the bot to export.</p>"""
    resource_type: "aws_sdk_lex_model_building_service.types.resource_type.ResourceType"
    """<p>The type of resource to export. </p>"""
    export_type: "aws_sdk_lex_model_building_service.types.export_type.ExportType"
    """<p>The format of the exported data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetExportRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetExportRequest:
    out: GetExportRequest = {}  # type: ignore[typeddict-item]
    return out

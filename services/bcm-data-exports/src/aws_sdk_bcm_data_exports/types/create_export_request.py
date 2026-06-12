"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#CreateExportRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bcm_data_exports.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bcm_data_exports.types.export
    import aws_sdk_bcm_data_exports.types.resource_tag_list

class CreateExportRequest(TypedDict):
    export: "aws_sdk_bcm_data_exports.types.export.Export"
    """<p>The details of the export, including data query, name, description, and destination configuration.</p>"""
    resource_tags: NotRequired["aws_sdk_bcm_data_exports.types.resource_tag_list.ResourceTagList"]
    """<p>An optional list of tags to associate with the specified export. Each tag consists of a key and a value, and each key must be unique for the resource.</p>"""

# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateExportRequest) -> dict:
    out: dict = {}
    import aws_sdk_bcm_data_exports.types.export
    out["Export"] = aws_sdk_bcm_data_exports.types.export.serialize_aws_json_1_1(value["export"])
    if "resource_tags" in value:
        import aws_sdk_bcm_data_exports.types.resource_tag_list
        out["ResourceTags"] = aws_sdk_bcm_data_exports.types.resource_tag_list.serialize_aws_json_1_1(value["resource_tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateExportRequest:
    out: CreateExportRequest = {}  # type: ignore[typeddict-item]
    if "Export" in data:
        import aws_sdk_bcm_data_exports.types.export
        out["export"] = aws_sdk_bcm_data_exports.types.export.deserialize_aws_json_1_1(data["Export"])
    else:
        raise DeserializationError("CreateExportRequest.export required")
    if "ResourceTags" in data:
        import aws_sdk_bcm_data_exports.types.resource_tag_list
        out["resource_tags"] = aws_sdk_bcm_data_exports.types.resource_tag_list.deserialize_aws_json_1_1(data["ResourceTags"])
    return out
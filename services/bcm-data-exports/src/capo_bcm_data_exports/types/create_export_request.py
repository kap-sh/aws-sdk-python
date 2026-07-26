"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#CreateExportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bcm_data_exports.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bcm_data_exports.types.export
    import capo_bcm_data_exports.types.resource_tag_list


class CreateExportRequest(TypedDict, closed=True):
    export: "capo_bcm_data_exports.types.export.Export"
    """<p>The details of the export, including data query, name, description, and destination configuration.</p>"""
    resource_tags: NotRequired[
        "capo_bcm_data_exports.types.resource_tag_list.ResourceTagList"
    ]
    """<p>An optional list of tags to associate with the specified export. Each tag consists of a key and a value, and each key must be unique for the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateExportRequest) -> dict:
    out: dict = {}
    import capo_bcm_data_exports.types.export

    out["Export"] = capo_bcm_data_exports.types.export.serialize_aws_json_1_1(
        value["export"]
    )
    if "resource_tags" in value:
        import capo_bcm_data_exports.types.resource_tag_list

        out["ResourceTags"] = (
            capo_bcm_data_exports.types.resource_tag_list.serialize_aws_json_1_1(
                value["resource_tags"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateExportRequest:
    out: CreateExportRequest = {}  # type: ignore[typeddict-item]
    if "Export" in data:
        import capo_bcm_data_exports.types.export

        out["export"] = capo_bcm_data_exports.types.export.deserialize_aws_json_1_1(
            data["Export"]
        )
    else:
        raise DeserializationError("CreateExportRequest.export required")
    if "ResourceTags" in data:
        import capo_bcm_data_exports.types.resource_tag_list

        out["resource_tags"] = (
            capo_bcm_data_exports.types.resource_tag_list.deserialize_aws_json_1_1(
                data["ResourceTags"]
            )
        )
    return out

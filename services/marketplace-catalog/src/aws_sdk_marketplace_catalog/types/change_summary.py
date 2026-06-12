"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ChangeSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.change_name
    import aws_sdk_marketplace_catalog.types.change_type
    import aws_sdk_marketplace_catalog.types.entity
    import aws_sdk_marketplace_catalog.types.error_detail_list
    import aws_sdk_marketplace_catalog.types.json
    import aws_sdk_marketplace_catalog.types.json_document_type


class ChangeSummary(TypedDict):
    change_type: NotRequired["aws_sdk_marketplace_catalog.types.change_type.ChangeType"]
    """<p>The type of the change.</p>"""
    entity: NotRequired["aws_sdk_marketplace_catalog.types.entity.Entity"]
    """<p>The entity to be changed.</p>"""
    details: NotRequired["aws_sdk_marketplace_catalog.types.json.Json"]
    """<p>This object contains details specific to the change type of the requested change.</p>"""
    details_document: NotRequired[
        "aws_sdk_marketplace_catalog.types.json_document_type.JsonDocumentType"
    ]
    """<p>The JSON value of the details specific to the change type of the requested change.</p> <p>To download the \"DetailsDocument\" shapes, see the <a href=\"https://github.com/awslabs/aws-marketplace-catalog-api-shapes-for-python\">Python</a> and <a href=\"https://github.com/awslabs/aws-marketplace-catalog-api-shapes-for-java/tree/main\">Java</a> shapes on GitHub.</p>"""
    error_detail_list: NotRequired[
        "aws_sdk_marketplace_catalog.types.error_detail_list.ErrorDetailList"
    ]
    """<p>An array of <code>ErrorDetail</code> objects associated with the change.</p>"""
    change_name: NotRequired["aws_sdk_marketplace_catalog.types.change_name.ChangeName"]
    """<p>Optional name for the change.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChangeSummary) -> dict:
    out: dict = {}
    if "change_type" in value:
        out["ChangeType"] = value["change_type"]
    if "entity" in value:
        import aws_sdk_marketplace_catalog.types.entity

        out["Entity"] = aws_sdk_marketplace_catalog.types.entity.serialize_json(
            value["entity"]
        )
    if "details" in value:
        out["Details"] = value["details"]
    if "details_document" in value:
        out["DetailsDocument"] = value["details_document"]
    if "error_detail_list" in value:
        import aws_sdk_marketplace_catalog.types.error_detail_list

        out["ErrorDetailList"] = (
            aws_sdk_marketplace_catalog.types.error_detail_list.serialize_json(
                value["error_detail_list"]
            )
        )
    if "change_name" in value:
        out["ChangeName"] = value["change_name"]
    return out


def deserialize_json(data: dict) -> ChangeSummary:
    out: ChangeSummary = {}  # type: ignore[typeddict-item]
    if "ChangeType" in data:
        out["change_type"] = data["ChangeType"]
    if "Entity" in data:
        import aws_sdk_marketplace_catalog.types.entity

        out["entity"] = aws_sdk_marketplace_catalog.types.entity.deserialize_json(
            data["Entity"]
        )
    if "Details" in data:
        out["details"] = data["Details"]
    if "DetailsDocument" in data:
        out["details_document"] = data["DetailsDocument"]
    if "ErrorDetailList" in data:
        import aws_sdk_marketplace_catalog.types.error_detail_list

        out["error_detail_list"] = (
            aws_sdk_marketplace_catalog.types.error_detail_list.deserialize_json(
                data["ErrorDetailList"]
            )
        )
    if "ChangeName" in data:
        out["change_name"] = data["ChangeName"]
    return out

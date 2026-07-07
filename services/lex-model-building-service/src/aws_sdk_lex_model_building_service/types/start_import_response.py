"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#StartImportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.import_status
    import aws_sdk_lex_model_building_service.types.merge_strategy
    import aws_sdk_lex_model_building_service.types.name
    import aws_sdk_lex_model_building_service.types.resource_type
    import aws_sdk_lex_model_building_service.types.string
    import aws_sdk_lex_model_building_service.types.tag_list
    import aws_sdk_lex_model_building_service.types.timestamp


class StartImportResponse(TypedDict, closed=True):
    name: NotRequired["aws_sdk_lex_model_building_service.types.name.Name"]
    """<p>The name given to the import job.</p>"""
    resource_type: NotRequired[
        "aws_sdk_lex_model_building_service.types.resource_type.ResourceType"
    ]
    """<p>The type of resource to import.</p>"""
    merge_strategy: NotRequired[
        "aws_sdk_lex_model_building_service.types.merge_strategy.MergeStrategy"
    ]
    """<p>The action to take when there is a merge conflict.</p>"""
    import_id: NotRequired["aws_sdk_lex_model_building_service.types.string.String"]
    """<p>The identifier for the specific import job.</p>"""
    import_status: NotRequired[
        "aws_sdk_lex_model_building_service.types.import_status.ImportStatus"
    ]
    """<p>The status of the import job. If the status is <code>FAILED</code>, you can get the reason for the failure using the <code>GetImport</code> operation.</p>"""
    tags: NotRequired["aws_sdk_lex_model_building_service.types.tag_list.TagList"]
    """<p>A list of tags added to the imported bot.</p>"""
    created_date: NotRequired[
        "aws_sdk_lex_model_building_service.types.timestamp.Timestamp"
    ]
    """<p>A timestamp for the date and time that the import job was requested.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartImportResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "resource_type" in value:
        import aws_sdk_lex_model_building_service.types.resource_type

        out["resourceType"] = (
            aws_sdk_lex_model_building_service.types.resource_type.serialize_json(
                value["resource_type"]
            )
        )
    if "merge_strategy" in value:
        import aws_sdk_lex_model_building_service.types.merge_strategy

        out["mergeStrategy"] = (
            aws_sdk_lex_model_building_service.types.merge_strategy.serialize_json(
                value["merge_strategy"]
            )
        )
    if "import_id" in value:
        out["importId"] = value["import_id"]
    if "import_status" in value:
        import aws_sdk_lex_model_building_service.types.import_status

        out["importStatus"] = (
            aws_sdk_lex_model_building_service.types.import_status.serialize_json(
                value["import_status"]
            )
        )
    if "tags" in value:
        import aws_sdk_lex_model_building_service.types.tag_list

        out["tags"] = aws_sdk_lex_model_building_service.types.tag_list.serialize_json(
            value["tags"]
        )
    if "created_date" in value:
        import aws_sdk_lex_model_building_service.types.timestamp

        out["createdDate"] = (
            aws_sdk_lex_model_building_service.types.timestamp.serialize_json(
                value["created_date"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartImportResponse:
    out: StartImportResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "resourceType" in data:
        import aws_sdk_lex_model_building_service.types.resource_type

        out["resource_type"] = (
            aws_sdk_lex_model_building_service.types.resource_type.deserialize_json(
                data["resourceType"]
            )
        )
    if "mergeStrategy" in data:
        import aws_sdk_lex_model_building_service.types.merge_strategy

        out["merge_strategy"] = (
            aws_sdk_lex_model_building_service.types.merge_strategy.deserialize_json(
                data["mergeStrategy"]
            )
        )
    if "importId" in data:
        out["import_id"] = data["importId"]
    if "importStatus" in data:
        import aws_sdk_lex_model_building_service.types.import_status

        out["import_status"] = (
            aws_sdk_lex_model_building_service.types.import_status.deserialize_json(
                data["importStatus"]
            )
        )
    if "tags" in data:
        import aws_sdk_lex_model_building_service.types.tag_list

        out["tags"] = (
            aws_sdk_lex_model_building_service.types.tag_list.deserialize_json(
                data["tags"]
            )
        )
    if "createdDate" in data:
        import aws_sdk_lex_model_building_service.types.timestamp

        out["created_date"] = (
            aws_sdk_lex_model_building_service.types.timestamp.deserialize_json(
                data["createdDate"]
            )
        )
    return out

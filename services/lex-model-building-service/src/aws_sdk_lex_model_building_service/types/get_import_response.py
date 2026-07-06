"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#GetImportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.import_status
    import aws_sdk_lex_model_building_service.types.merge_strategy
    import aws_sdk_lex_model_building_service.types.name
    import aws_sdk_lex_model_building_service.types.resource_type
    import aws_sdk_lex_model_building_service.types.string
    import aws_sdk_lex_model_building_service.types.string_list
    import aws_sdk_lex_model_building_service.types.timestamp


class GetImportResponse(TypedDict, closed=True):
    name: NotRequired["aws_sdk_lex_model_building_service.types.name.Name"]
    """<p>The name given to the import job.</p>"""
    resource_type: NotRequired[
        "aws_sdk_lex_model_building_service.types.resource_type.ResourceType"
    ]
    """<p>The type of resource imported.</p>"""
    merge_strategy: NotRequired[
        "aws_sdk_lex_model_building_service.types.merge_strategy.MergeStrategy"
    ]
    """<p>The action taken when there was a conflict between an existing resource and a resource in the import file.</p>"""
    import_id: NotRequired["aws_sdk_lex_model_building_service.types.string.String"]
    """<p>The identifier for the specific import job.</p>"""
    import_status: NotRequired[
        "aws_sdk_lex_model_building_service.types.import_status.ImportStatus"
    ]
    """<p>The status of the import job. If the status is <code>FAILED</code>, you can get the reason for the failure from the <code>failureReason</code> field.</p>"""
    failure_reason: NotRequired[
        "aws_sdk_lex_model_building_service.types.string_list.StringList"
    ]
    """<p>A string that describes why an import job failed to complete.</p>"""
    created_date: NotRequired[
        "aws_sdk_lex_model_building_service.types.timestamp.Timestamp"
    ]
    """<p>A timestamp for the date and time that the import job was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetImportResponse) -> dict:
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
    if "failure_reason" in value:
        import aws_sdk_lex_model_building_service.types.string_list

        out["failureReason"] = (
            aws_sdk_lex_model_building_service.types.string_list.serialize_json(
                value["failure_reason"]
            )
        )
    if "created_date" in value:
        import aws_sdk_lex_model_building_service.types.timestamp

        out["createdDate"] = (
            aws_sdk_lex_model_building_service.types.timestamp.serialize_json(
                value["created_date"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetImportResponse:
    out: GetImportResponse = {}  # type: ignore[typeddict-item]
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
    if "failureReason" in data:
        import aws_sdk_lex_model_building_service.types.string_list

        out["failure_reason"] = (
            aws_sdk_lex_model_building_service.types.string_list.deserialize_json(
                data["failureReason"]
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

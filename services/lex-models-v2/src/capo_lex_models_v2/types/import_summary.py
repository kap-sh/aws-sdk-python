"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ImportSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.import_resource_type
    import capo_lex_models_v2.types.import_status
    import capo_lex_models_v2.types.imported_resource_id
    import capo_lex_models_v2.types.merge_strategy
    import capo_lex_models_v2.types.name
    import capo_lex_models_v2.types.timestamp


class ImportSummary(TypedDict, closed=True):
    import_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The unique identifier that Amazon Lex assigned to the import.</p>"""
    imported_resource_id: NotRequired[
        "capo_lex_models_v2.types.imported_resource_id.ImportedResourceId"
    ]
    """<p>The unique identifier that Amazon Lex assigned to the imported resource.</p>"""
    imported_resource_name: NotRequired["capo_lex_models_v2.types.name.Name"]
    """<p>The name that you gave the imported resource.</p>"""
    import_status: NotRequired["capo_lex_models_v2.types.import_status.ImportStatus"]
    """<p>The status of the resource. When the status is <code>Completed</code> the resource is ready to build.</p>"""
    merge_strategy: NotRequired["capo_lex_models_v2.types.merge_strategy.MergeStrategy"]
    """<p>The strategy used to merge existing bot or bot locale definitions with the imported definition.</p>"""
    creation_date_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The date and time that the import was created.</p>"""
    last_updated_date_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The date and time that the import was last updated.</p>"""
    imported_resource_type: NotRequired[
        "capo_lex_models_v2.types.import_resource_type.ImportResourceType"
    ]
    """<p>The type of resource that was imported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportSummary) -> dict:
    out: dict = {}
    if "import_id" in value:
        out["importId"] = value["import_id"]
    if "imported_resource_id" in value:
        out["importedResourceId"] = value["imported_resource_id"]
    if "imported_resource_name" in value:
        out["importedResourceName"] = value["imported_resource_name"]
    if "import_status" in value:
        import capo_lex_models_v2.types.import_status

        out["importStatus"] = capo_lex_models_v2.types.import_status.serialize_json(
            value["import_status"]
        )
    if "merge_strategy" in value:
        import capo_lex_models_v2.types.merge_strategy

        out["mergeStrategy"] = capo_lex_models_v2.types.merge_strategy.serialize_json(
            value["merge_strategy"]
        )
    if "creation_date_time" in value:
        import capo_lex_models_v2.types.timestamp

        out["creationDateTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
            value["creation_date_time"]
        )
    if "last_updated_date_time" in value:
        import capo_lex_models_v2.types.timestamp

        out["lastUpdatedDateTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
            value["last_updated_date_time"]
        )
    if "imported_resource_type" in value:
        import capo_lex_models_v2.types.import_resource_type

        out["importedResourceType"] = (
            capo_lex_models_v2.types.import_resource_type.serialize_json(
                value["imported_resource_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> ImportSummary:
    out: ImportSummary = {}  # type: ignore[typeddict-item]
    if "importId" in data:
        out["import_id"] = data["importId"]
    if "importedResourceId" in data:
        out["imported_resource_id"] = data["importedResourceId"]
    if "importedResourceName" in data:
        out["imported_resource_name"] = data["importedResourceName"]
    if "importStatus" in data:
        import capo_lex_models_v2.types.import_status

        out["import_status"] = capo_lex_models_v2.types.import_status.deserialize_json(
            data["importStatus"]
        )
    if "mergeStrategy" in data:
        import capo_lex_models_v2.types.merge_strategy

        out["merge_strategy"] = (
            capo_lex_models_v2.types.merge_strategy.deserialize_json(
                data["mergeStrategy"]
            )
        )
    if "creationDateTime" in data:
        import capo_lex_models_v2.types.timestamp

        out["creation_date_time"] = capo_lex_models_v2.types.timestamp.deserialize_json(
            data["creationDateTime"]
        )
    if "lastUpdatedDateTime" in data:
        import capo_lex_models_v2.types.timestamp

        out["last_updated_date_time"] = (
            capo_lex_models_v2.types.timestamp.deserialize_json(
                data["lastUpdatedDateTime"]
            )
        )
    if "importedResourceType" in data:
        import capo_lex_models_v2.types.import_resource_type

        out["imported_resource_type"] = (
            capo_lex_models_v2.types.import_resource_type.deserialize_json(
                data["importedResourceType"]
            )
        )
    return out

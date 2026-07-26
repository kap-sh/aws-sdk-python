"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DescribeImportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.failure_reasons
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.import_resource_specification
    import capo_lex_models_v2.types.import_status
    import capo_lex_models_v2.types.imported_resource_id
    import capo_lex_models_v2.types.merge_strategy
    import capo_lex_models_v2.types.name
    import capo_lex_models_v2.types.timestamp


class DescribeImportResponse(TypedDict, closed=True):
    import_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The unique identifier of the described import.</p>"""
    resource_specification: NotRequired[
        "capo_lex_models_v2.types.import_resource_specification.ImportResourceSpecification"
    ]
    """<p>The specifications of the imported bot, bot locale, or custom vocabulary.</p>"""
    imported_resource_id: NotRequired[
        "capo_lex_models_v2.types.imported_resource_id.ImportedResourceId"
    ]
    """<p>The unique identifier that Amazon Lex assigned to the resource created by the import.</p>"""
    imported_resource_name: NotRequired["capo_lex_models_v2.types.name.Name"]
    """<p>The name of the imported resource.</p>"""
    merge_strategy: NotRequired["capo_lex_models_v2.types.merge_strategy.MergeStrategy"]
    """<p>The strategy used when there was a name conflict between the imported resource and an existing resource. When the merge strategy is <code>FailOnConflict</code> existing resources are not overwritten and the import fails.</p>"""
    import_status: NotRequired["capo_lex_models_v2.types.import_status.ImportStatus"]
    """<p>The status of the import process. When the status is <code>Completed</code> the resource is imported and ready for use.</p>"""
    failure_reasons: NotRequired[
        "capo_lex_models_v2.types.failure_reasons.FailureReasons"
    ]
    """<p>If the <code>importStatus</code> field is <code>Failed</code>, this provides one or more reasons for the failure.</p>"""
    creation_date_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The date and time that the import was created.</p>"""
    last_updated_date_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The date and time that the import was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeImportResponse) -> dict:
    out: dict = {}
    if "import_id" in value:
        out["importId"] = value["import_id"]
    if "resource_specification" in value:
        import capo_lex_models_v2.types.import_resource_specification

        out["resourceSpecification"] = (
            capo_lex_models_v2.types.import_resource_specification.serialize_json(
                value["resource_specification"]
            )
        )
    if "imported_resource_id" in value:
        out["importedResourceId"] = value["imported_resource_id"]
    if "imported_resource_name" in value:
        out["importedResourceName"] = value["imported_resource_name"]
    if "merge_strategy" in value:
        import capo_lex_models_v2.types.merge_strategy

        out["mergeStrategy"] = capo_lex_models_v2.types.merge_strategy.serialize_json(
            value["merge_strategy"]
        )
    if "import_status" in value:
        import capo_lex_models_v2.types.import_status

        out["importStatus"] = capo_lex_models_v2.types.import_status.serialize_json(
            value["import_status"]
        )
    if "failure_reasons" in value:
        import capo_lex_models_v2.types.failure_reasons

        out["failureReasons"] = capo_lex_models_v2.types.failure_reasons.serialize_json(
            value["failure_reasons"]
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
    return out


def deserialize_json(data: dict) -> DescribeImportResponse:
    out: DescribeImportResponse = {}  # type: ignore[typeddict-item]
    if "importId" in data:
        out["import_id"] = data["importId"]
    if "resourceSpecification" in data:
        import capo_lex_models_v2.types.import_resource_specification

        out["resource_specification"] = (
            capo_lex_models_v2.types.import_resource_specification.deserialize_json(
                data["resourceSpecification"]
            )
        )
    if "importedResourceId" in data:
        out["imported_resource_id"] = data["importedResourceId"]
    if "importedResourceName" in data:
        out["imported_resource_name"] = data["importedResourceName"]
    if "mergeStrategy" in data:
        import capo_lex_models_v2.types.merge_strategy

        out["merge_strategy"] = (
            capo_lex_models_v2.types.merge_strategy.deserialize_json(
                data["mergeStrategy"]
            )
        )
    if "importStatus" in data:
        import capo_lex_models_v2.types.import_status

        out["import_status"] = capo_lex_models_v2.types.import_status.deserialize_json(
            data["importStatus"]
        )
    if "failureReasons" in data:
        import capo_lex_models_v2.types.failure_reasons

        out["failure_reasons"] = (
            capo_lex_models_v2.types.failure_reasons.deserialize_json(
                data["failureReasons"]
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
    return out

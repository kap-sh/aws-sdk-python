"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#StartImportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.import_resource_specification
    import capo_lex_models_v2.types.import_status
    import capo_lex_models_v2.types.merge_strategy
    import capo_lex_models_v2.types.timestamp


class StartImportResponse(TypedDict, closed=True):
    import_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>A unique identifier for the import.</p>"""
    resource_specification: NotRequired[
        "capo_lex_models_v2.types.import_resource_specification.ImportResourceSpecification"
    ]
    """<p>The parameters used when importing the resource.</p>"""
    merge_strategy: NotRequired["capo_lex_models_v2.types.merge_strategy.MergeStrategy"]
    """<p>The strategy used when there was a name conflict between the imported resource and an existing resource. When the merge strategy is <code>FailOnConflict</code> existing resources are not overwritten and the import fails.</p>"""
    import_status: NotRequired["capo_lex_models_v2.types.import_status.ImportStatus"]
    """<p>The current status of the import. When the status is <code>Complete</code> the bot, bot alias, or custom vocabulary is ready to use.</p>"""
    creation_date_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The date and time that the import request was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartImportResponse) -> dict:
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
    if "creation_date_time" in value:
        import capo_lex_models_v2.types.timestamp

        out["creationDateTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
            value["creation_date_time"]
        )
    return out


def deserialize_json(data: dict) -> StartImportResponse:
    out: StartImportResponse = {}  # type: ignore[typeddict-item]
    if "importId" in data:
        out["import_id"] = data["importId"]
    if "resourceSpecification" in data:
        import capo_lex_models_v2.types.import_resource_specification

        out["resource_specification"] = (
            capo_lex_models_v2.types.import_resource_specification.deserialize_json(
                data["resourceSpecification"]
            )
        )
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
    if "creationDateTime" in data:
        import capo_lex_models_v2.types.timestamp

        out["creation_date_time"] = capo_lex_models_v2.types.timestamp.deserialize_json(
            data["creationDateTime"]
        )
    return out

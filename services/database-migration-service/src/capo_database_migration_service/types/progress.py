"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#Progress``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.double_optional
    import capo_database_migration_service.types.long
    import capo_database_migration_service.types.processed_object
    import capo_database_migration_service.types.string


class Progress(TypedDict, closed=True):
    progress_percent: NotRequired[
        "capo_database_migration_service.types.double_optional.DoubleOptional"
    ]
    """<p>The percent complete for the current step of the schema conversion operation.</p>"""
    total_objects: "capo_database_migration_service.types.long.Long"
    """<p>The number of objects in this schema conversion operation.</p>"""
    progress_step: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The step of the schema conversion operation. This parameter can store one of the following values:</p> <ul> <li> <p> <code>IN_PROGRESS</code> – The operation is running.</p> </li> <li> <p> <code>LOADING_METADATA</code> – Loads metadata from the source database.</p> </li> <li> <p> <code>COUNTING_OBJECTS</code> – Determines the number of objects involved in the operation.</p> </li> <li> <p> <code>ANALYZING</code> – Analyzes the source database objects.</p> </li> <li> <p> <code>CONVERTING</code> – Converts the source database objects to a format compatible with the target database.</p> </li> <li> <p> <code>APPLYING</code> – Applies the converted code to the target database.</p> </li> <li> <p> <code>FINISHED</code> – The operation completed successfully.</p> </li> </ul>"""
    processed_object: NotRequired[
        "capo_database_migration_service.types.processed_object.ProcessedObject"
    ]
    """<p>The name of the database object that the schema conversion operation currently uses.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Progress) -> dict:
    out: dict = {}
    if "progress_percent" in value:
        out["ProgressPercent"] = value["progress_percent"]
    out["TotalObjects"] = value.get("total_objects", 0)
    if "progress_step" in value:
        out["ProgressStep"] = value["progress_step"]
    if "processed_object" in value:
        import capo_database_migration_service.types.processed_object

        out["ProcessedObject"] = (
            capo_database_migration_service.types.processed_object.serialize_aws_json_1_1(
                value["processed_object"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Progress:
    out: Progress = {}  # type: ignore[typeddict-item]
    if "ProgressPercent" in data:
        out["progress_percent"] = data["ProgressPercent"]
    if "TotalObjects" in data:
        out["total_objects"] = data["TotalObjects"]
    else:
        out["total_objects"] = 0
    if "ProgressStep" in data:
        out["progress_step"] = data["ProgressStep"]
    if "ProcessedObject" in data:
        import capo_database_migration_service.types.processed_object

        out["processed_object"] = (
            capo_database_migration_service.types.processed_object.deserialize_aws_json_1_1(
                data["ProcessedObject"]
            )
        )
    return out

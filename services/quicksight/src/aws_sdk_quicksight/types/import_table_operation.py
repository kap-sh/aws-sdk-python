"""Generated from Smithy shape ``com.amazonaws.quicksight#ImportTableOperation``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.import_table_operation_source
    import aws_sdk_quicksight.types.transform_operation_alias


class ImportTableOperation(TypedDict):
    alias: "aws_sdk_quicksight.types.transform_operation_alias.TransformOperationAlias"
    """<p>Alias for this operation.</p>"""
    source: "aws_sdk_quicksight.types.import_table_operation_source.ImportTableOperationSource"
    """<p>The source configuration that specifies which source table to import and any column mappings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportTableOperation) -> dict:
    out: dict = {}
    out["Alias"] = value["alias"]
    import aws_sdk_quicksight.types.import_table_operation_source

    out["Source"] = (
        aws_sdk_quicksight.types.import_table_operation_source.serialize_json(
            value["source"]
        )
    )
    return out


def deserialize_json(data: dict) -> ImportTableOperation:
    out: ImportTableOperation = {}  # type: ignore[typeddict-item]
    if "Alias" in data:
        out["alias"] = data["Alias"]
    else:
        raise DeserializationError("ImportTableOperation.alias required")
    if "Source" in data:
        import aws_sdk_quicksight.types.import_table_operation_source

        out["source"] = (
            aws_sdk_quicksight.types.import_table_operation_source.deserialize_json(
                data["Source"]
            )
        )
    else:
        raise DeserializationError("ImportTableOperation.source required")
    return out

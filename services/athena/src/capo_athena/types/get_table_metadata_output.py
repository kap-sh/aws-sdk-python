"""Generated from Smithy shape ``com.amazonaws.athena#GetTableMetadataOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.table_metadata


class GetTableMetadataOutput(TypedDict, closed=True):
    table_metadata: NotRequired["capo_athena.types.table_metadata.TableMetadata"]
    """<p>An object that contains table metadata.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTableMetadataOutput) -> dict:
    out: dict = {}
    if "table_metadata" in value:
        import capo_athena.types.table_metadata

        out["TableMetadata"] = capo_athena.types.table_metadata.serialize_aws_json_1_1(
            value["table_metadata"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTableMetadataOutput:
    out: GetTableMetadataOutput = {}  # type: ignore[typeddict-item]
    if "TableMetadata" in data:
        import capo_athena.types.table_metadata

        out["table_metadata"] = (
            capo_athena.types.table_metadata.deserialize_aws_json_1_1(
                data["TableMetadata"]
            )
        )
    return out

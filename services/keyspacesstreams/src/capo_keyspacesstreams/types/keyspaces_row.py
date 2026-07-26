"""Generated from Smithy shape ``com.amazonaws.keyspacesstreams#KeyspacesRow``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_keyspacesstreams.types.keyspaces_cells
    import capo_keyspacesstreams.types.keyspaces_metadata


class KeyspacesRow(TypedDict, closed=True):
    value_cells: NotRequired[
        "capo_keyspacesstreams.types.keyspaces_cells.KeyspacesCells"
    ]
    """<p>A map of regular (non-static) column cells in the row, where keys are column names and values are the corresponding cells.</p>"""
    static_cells: NotRequired[
        "capo_keyspacesstreams.types.keyspaces_cells.KeyspacesCells"
    ]
    """<p>A map of static column cells shared by all rows with the same partition key, where keys are column names and values are the corresponding cells.</p>"""
    row_metadata: NotRequired[
        "capo_keyspacesstreams.types.keyspaces_metadata.KeyspacesMetadata"
    ]
    """<p>Metadata that applies to the entire row, such as timestamps and TTL information.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KeyspacesRow) -> dict:
    out: dict = {}
    if "value_cells" in value:
        import capo_keyspacesstreams.types.keyspaces_cells

        out["valueCells"] = (
            capo_keyspacesstreams.types.keyspaces_cells.serialize_aws_json_1_0(
                value["value_cells"]
            )
        )
    if "static_cells" in value:
        import capo_keyspacesstreams.types.keyspaces_cells

        out["staticCells"] = (
            capo_keyspacesstreams.types.keyspaces_cells.serialize_aws_json_1_0(
                value["static_cells"]
            )
        )
    if "row_metadata" in value:
        import capo_keyspacesstreams.types.keyspaces_metadata

        out["rowMetadata"] = (
            capo_keyspacesstreams.types.keyspaces_metadata.serialize_aws_json_1_0(
                value["row_metadata"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> KeyspacesRow:
    out: KeyspacesRow = {}  # type: ignore[typeddict-item]
    if "valueCells" in data:
        import capo_keyspacesstreams.types.keyspaces_cells

        out["value_cells"] = (
            capo_keyspacesstreams.types.keyspaces_cells.deserialize_aws_json_1_0(
                data["valueCells"]
            )
        )
    if "staticCells" in data:
        import capo_keyspacesstreams.types.keyspaces_cells

        out["static_cells"] = (
            capo_keyspacesstreams.types.keyspaces_cells.deserialize_aws_json_1_0(
                data["staticCells"]
            )
        )
    if "rowMetadata" in data:
        import capo_keyspacesstreams.types.keyspaces_metadata

        out["row_metadata"] = (
            capo_keyspacesstreams.types.keyspaces_metadata.deserialize_aws_json_1_0(
                data["rowMetadata"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.redshift#BatchDeleteClusterSnapshotsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.batch_snapshot_operation_error_list
    import capo_redshift.types.snapshot_identifier_list


class BatchDeleteClusterSnapshotsResult(TypedDict, closed=True):
    resources: NotRequired[
        "capo_redshift.types.snapshot_identifier_list.SnapshotIdentifierList"
    ]
    """<p>A list of the snapshot identifiers that were deleted. </p>"""
    errors: NotRequired[
        "capo_redshift.types.batch_snapshot_operation_error_list.BatchSnapshotOperationErrorList"
    ]
    """<p>A list of any errors returned.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: BatchDeleteClusterSnapshotsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "resources" in value:
        import capo_redshift.types.snapshot_identifier_list

        capo_redshift.types.snapshot_identifier_list.serialize_query(
            value["resources"], pairs, f"{key_prefix}Resources"
        )
    if "errors" in value:
        import capo_redshift.types.batch_snapshot_operation_error_list

        capo_redshift.types.batch_snapshot_operation_error_list.serialize_query(
            value["errors"], pairs, f"{key_prefix}Errors"
        )


def deserialize_query(el: Element) -> BatchDeleteClusterSnapshotsResult:
    out: BatchDeleteClusterSnapshotsResult = {}  # type: ignore[typeddict-item]
    child_resources = el.find("Resources")
    if child_resources is not None:
        import capo_redshift.types.snapshot_identifier_list

        out["resources"] = (
            capo_redshift.types.snapshot_identifier_list.deserialize_query(
                child_resources
            )
        )
    child_errors = el.find("Errors")
    if child_errors is not None:
        import capo_redshift.types.batch_snapshot_operation_error_list

        out["errors"] = (
            capo_redshift.types.batch_snapshot_operation_error_list.deserialize_query(
                child_errors
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.redshift#BatchModifyClusterSnapshotsOutputMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.batch_snapshot_operation_errors
    import aws_sdk_redshift.types.snapshot_identifier_list


class BatchModifyClusterSnapshotsOutputMessage(TypedDict, closed=True):
    resources: NotRequired[
        "aws_sdk_redshift.types.snapshot_identifier_list.SnapshotIdentifierList"
    ]
    """<p>A list of the snapshots that were modified.</p>"""
    errors: NotRequired[
        "aws_sdk_redshift.types.batch_snapshot_operation_errors.BatchSnapshotOperationErrors"
    ]
    """<p>A list of any errors returned.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: BatchModifyClusterSnapshotsOutputMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "resources" in value:
        import aws_sdk_redshift.types.snapshot_identifier_list

        aws_sdk_redshift.types.snapshot_identifier_list.serialize_query(
            value["resources"], pairs, f"{prefix}.Resources"
        )
    if "errors" in value:
        import aws_sdk_redshift.types.batch_snapshot_operation_errors

        aws_sdk_redshift.types.batch_snapshot_operation_errors.serialize_query(
            value["errors"], pairs, f"{prefix}.Errors"
        )


def deserialize_query(el: Element) -> BatchModifyClusterSnapshotsOutputMessage:
    out: BatchModifyClusterSnapshotsOutputMessage = {}  # type: ignore[typeddict-item]
    child_resources = el.find("Resources")
    if child_resources is not None:
        import aws_sdk_redshift.types.snapshot_identifier_list

        out["resources"] = (
            aws_sdk_redshift.types.snapshot_identifier_list.deserialize_query(
                child_resources
            )
        )
    child_errors = el.find("Errors")
    if child_errors is not None:
        import aws_sdk_redshift.types.batch_snapshot_operation_errors

        out["errors"] = (
            aws_sdk_redshift.types.batch_snapshot_operation_errors.deserialize_query(
                child_errors
            )
        )
    return out

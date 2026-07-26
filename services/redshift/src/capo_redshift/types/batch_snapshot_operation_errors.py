"""Generated from Smithy shape ``com.amazonaws.redshift#BatchSnapshotOperationErrors``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.snapshot_error_message

BatchSnapshotOperationErrors: TypeAlias = list[
    "capo_redshift.types.snapshot_error_message.SnapshotErrorMessage"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: BatchSnapshotOperationErrors, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.snapshot_error_message

    for n, item in enumerate(value, 1):
        capo_redshift.types.snapshot_error_message.serialize_query(
            item, pairs, f"{prefix}.SnapshotErrorMessage.{n}"
        )


def deserialize_query(el: Element) -> BatchSnapshotOperationErrors:
    import capo_redshift.types.snapshot_error_message

    out: BatchSnapshotOperationErrors = []
    for child in el.findall("SnapshotErrorMessage"):
        out.append(capo_redshift.types.snapshot_error_message.deserialize_query(child))
    return out


def serialize_query_flat(
    value: BatchSnapshotOperationErrors, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.snapshot_error_message

    for n, item in enumerate(value, 1):
        capo_redshift.types.snapshot_error_message.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> BatchSnapshotOperationErrors:
    import capo_redshift.types.snapshot_error_message

    out: BatchSnapshotOperationErrors = []
    for child in parent.findall(tag):
        out.append(capo_redshift.types.snapshot_error_message.deserialize_query(child))
    return out

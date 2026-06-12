"""Generated from Smithy shape ``com.amazonaws.redshift#BatchSnapshotOperationErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.snapshot_error_message

BatchSnapshotOperationErrorList: TypeAlias = list[
    "aws_sdk_redshift.types.snapshot_error_message.SnapshotErrorMessage"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: BatchSnapshotOperationErrorList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.snapshot_error_message

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.snapshot_error_message.serialize_query(
            item, pairs, f"{prefix}.SnapshotErrorMessage.{n}"
        )


def deserialize_query(el: Element) -> BatchSnapshotOperationErrorList:
    import aws_sdk_redshift.types.snapshot_error_message

    out: BatchSnapshotOperationErrorList = []
    for child in el.findall("SnapshotErrorMessage"):
        out.append(
            aws_sdk_redshift.types.snapshot_error_message.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: BatchSnapshotOperationErrorList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.snapshot_error_message

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.snapshot_error_message.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> BatchSnapshotOperationErrorList:
    import aws_sdk_redshift.types.snapshot_error_message

    out: BatchSnapshotOperationErrorList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_redshift.types.snapshot_error_message.deserialize_query(child)
        )
    return out

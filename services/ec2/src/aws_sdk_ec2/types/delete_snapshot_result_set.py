"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteSnapshotResultSet``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_snapshot_return_code

DeleteSnapshotResultSet: TypeAlias = list[
    "aws_sdk_ec2.types.delete_snapshot_return_code.DeleteSnapshotReturnCode"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteSnapshotResultSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.delete_snapshot_return_code

        aws_sdk_ec2.types.delete_snapshot_return_code.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> DeleteSnapshotResultSet:
    import aws_sdk_ec2.types.delete_snapshot_return_code

    out: DeleteSnapshotResultSet = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.delete_snapshot_return_code.deserialize_ec2_query(child)
        )
    return out

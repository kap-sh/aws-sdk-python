"""Generated from Smithy shape ``com.amazonaws.redshift#AuthorizeSnapshotAccessResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.snapshot


class AuthorizeSnapshotAccessResult(TypedDict):
    snapshot: NotRequired["aws_sdk_redshift.types.snapshot.Snapshot"]


# --- awsQuery ser/de ---
def serialize_query(
    value: AuthorizeSnapshotAccessResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "snapshot" in value:
        import aws_sdk_redshift.types.snapshot

        aws_sdk_redshift.types.snapshot.serialize_query(
            value["snapshot"], pairs, f"{prefix}.Snapshot"
        )


def deserialize_query(el: Element) -> AuthorizeSnapshotAccessResult:
    out: AuthorizeSnapshotAccessResult = {}  # type: ignore[typeddict-item]
    child_snapshot = el.find("Snapshot")
    if child_snapshot is not None:
        import aws_sdk_redshift.types.snapshot

        out["snapshot"] = aws_sdk_redshift.types.snapshot.deserialize_query(
            child_snapshot
        )
    return out

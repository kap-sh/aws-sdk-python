"""Generated from Smithy shape ``com.amazonaws.redshift#CreateSnapshotCopyGrantResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.snapshot_copy_grant


class CreateSnapshotCopyGrantResult(TypedDict, closed=True):
    snapshot_copy_grant: NotRequired[
        "capo_redshift.types.snapshot_copy_grant.SnapshotCopyGrant"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateSnapshotCopyGrantResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "snapshot_copy_grant" in value:
        import capo_redshift.types.snapshot_copy_grant

        capo_redshift.types.snapshot_copy_grant.serialize_query(
            value["snapshot_copy_grant"], pairs, f"{prefix}.SnapshotCopyGrant"
        )


def deserialize_query(el: Element) -> CreateSnapshotCopyGrantResult:
    out: CreateSnapshotCopyGrantResult = {}  # type: ignore[typeddict-item]
    child_snapshot_copy_grant = el.find("SnapshotCopyGrant")
    if child_snapshot_copy_grant is not None:
        import capo_redshift.types.snapshot_copy_grant

        out["snapshot_copy_grant"] = (
            capo_redshift.types.snapshot_copy_grant.deserialize_query(
                child_snapshot_copy_grant
            )
        )
    return out

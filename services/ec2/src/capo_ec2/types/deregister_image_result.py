"""Generated from Smithy shape ``com.amazonaws.ec2#DeregisterImageResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.delete_snapshot_result_set

DeregisterImageResult = TypedDict(
    "DeregisterImageResult",
    {
        "return": NotRequired["capo_ec2.types.boolean.Boolean"],
        "delete_snapshot_results": NotRequired[
            "capo_ec2.types.delete_snapshot_result_set.DeleteSnapshotResultSet"
        ],
    },
    closed=True,
)


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeregisterImageResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "return" in value:
        pairs.append((f"{key_prefix}Return", "true" if value["return"] else "false"))
    if "delete_snapshot_results" in value:
        import capo_ec2.types.delete_snapshot_result_set

        capo_ec2.types.delete_snapshot_result_set.serialize_ec2_query(
            value["delete_snapshot_results"],
            pairs,
            f"{key_prefix}DeleteSnapshotResultSet",
        )


def deserialize_ec2_query(el: Element) -> DeregisterImageResult:
    out: DeregisterImageResult = {}  # type: ignore[typeddict-item]
    child_return = el.find("return")
    if child_return is not None:
        out["return"] = (child_return.text or "").lower() == "true"
    child_delete_snapshot_results = el.find("deleteSnapshotResultSet")
    if child_delete_snapshot_results is not None:
        import capo_ec2.types.delete_snapshot_result_set

        out["delete_snapshot_results"] = (
            capo_ec2.types.delete_snapshot_result_set.deserialize_ec2_query(
                child_delete_snapshot_results
            )
        )
    return out

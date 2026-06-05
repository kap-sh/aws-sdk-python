"""Generated from Smithy shape ``com.amazonaws.ec2#DeregisterImageResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.delete_snapshot_result_set

DeregisterImageResult = TypedDict(
    "DeregisterImageResult",
    {
        "return": NotRequired["aws_sdk_ec2.types.boolean.Boolean"],
        "delete_snapshot_results": NotRequired[
            "aws_sdk_ec2.types.delete_snapshot_result_set.DeleteSnapshotResultSet"
        ],
    },
)


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeregisterImageResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "return" in value:
        pairs.append((f"{prefix}.Return", "true" if value["return"] else "false"))
    if "delete_snapshot_results" in value:
        import aws_sdk_ec2.types.delete_snapshot_result_set

        aws_sdk_ec2.types.delete_snapshot_result_set.serialize_ec2_query(
            value["delete_snapshot_results"], pairs, f"{prefix}.DeleteSnapshotResultSet"
        )


def deserialize_ec2_query(el: Element) -> DeregisterImageResult:
    out: DeregisterImageResult = {}  # type: ignore[typeddict-item]
    child_return = el.find("Return")
    if child_return is not None:
        out["return"] = (child_return.text or "").lower() == "true"
    if el.find("DeleteSnapshotResultSet") is not None:
        import aws_sdk_ec2.types.delete_snapshot_result_set

        out["delete_snapshot_results"] = (
            aws_sdk_ec2.types.delete_snapshot_result_set.deserialize_ec2_query(
                el, "DeleteSnapshotResultSet"
            )
        )
    return out

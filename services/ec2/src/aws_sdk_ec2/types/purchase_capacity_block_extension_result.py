"""Generated from Smithy shape ``com.amazonaws.ec2#PurchaseCapacityBlockExtensionResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_block_extension_set


class PurchaseCapacityBlockExtensionResult(TypedDict):
    capacity_block_extensions: NotRequired[
        "aws_sdk_ec2.types.capacity_block_extension_set.CapacityBlockExtensionSet"
    ]
    """<p>The purchased Capacity Block extensions. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PurchaseCapacityBlockExtensionResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "capacity_block_extensions" in value:
        import aws_sdk_ec2.types.capacity_block_extension_set

        aws_sdk_ec2.types.capacity_block_extension_set.serialize_ec2_query(
            value["capacity_block_extensions"],
            pairs,
            f"{prefix}.CapacityBlockExtensionSet",
        )


def deserialize_ec2_query(el: Element) -> PurchaseCapacityBlockExtensionResult:
    out: PurchaseCapacityBlockExtensionResult = {}  # type: ignore[typeddict-item]
    if el.find("CapacityBlockExtensionSet") is not None:
        import aws_sdk_ec2.types.capacity_block_extension_set

        out["capacity_block_extensions"] = (
            aws_sdk_ec2.types.capacity_block_extension_set.deserialize_ec2_query(
                el, "CapacityBlockExtensionSet"
            )
        )
    return out

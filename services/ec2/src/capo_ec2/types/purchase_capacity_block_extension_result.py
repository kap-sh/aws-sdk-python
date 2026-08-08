"""Generated from Smithy shape ``com.amazonaws.ec2#PurchaseCapacityBlockExtensionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.capacity_block_extension_set


class PurchaseCapacityBlockExtensionResult(TypedDict, closed=True):
    capacity_block_extensions: NotRequired[
        "capo_ec2.types.capacity_block_extension_set.CapacityBlockExtensionSet"
    ]
    """<p>The purchased Capacity Block extensions. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PurchaseCapacityBlockExtensionResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "capacity_block_extensions" in value:
        import capo_ec2.types.capacity_block_extension_set

        capo_ec2.types.capacity_block_extension_set.serialize_ec2_query(
            value["capacity_block_extensions"],
            pairs,
            f"{key_prefix}CapacityBlockExtensionSet",
        )


def deserialize_ec2_query(el: Element) -> PurchaseCapacityBlockExtensionResult:
    out: PurchaseCapacityBlockExtensionResult = {}  # type: ignore[typeddict-item]
    if el.find("capacityBlockExtensionSet") is not None:
        import capo_ec2.types.capacity_block_extension_set

        out["capacity_block_extensions"] = (
            capo_ec2.types.capacity_block_extension_set.deserialize_ec2_query(
                el, "capacityBlockExtensionSet"
            )
        )
    return out

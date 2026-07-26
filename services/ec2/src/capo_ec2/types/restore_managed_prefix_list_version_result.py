"""Generated from Smithy shape ``com.amazonaws.ec2#RestoreManagedPrefixListVersionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.managed_prefix_list


class RestoreManagedPrefixListVersionResult(TypedDict, closed=True):
    prefix_list: NotRequired["capo_ec2.types.managed_prefix_list.ManagedPrefixList"]
    """<p>Information about the prefix list.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RestoreManagedPrefixListVersionResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "prefix_list" in value:
        import capo_ec2.types.managed_prefix_list

        capo_ec2.types.managed_prefix_list.serialize_ec2_query(
            value["prefix_list"], pairs, f"{prefix}.PrefixList"
        )


def deserialize_ec2_query(el: Element) -> RestoreManagedPrefixListVersionResult:
    out: RestoreManagedPrefixListVersionResult = {}  # type: ignore[typeddict-item]
    child_prefix_list = el.find("PrefixList")
    if child_prefix_list is not None:
        import capo_ec2.types.managed_prefix_list

        out["prefix_list"] = capo_ec2.types.managed_prefix_list.deserialize_ec2_query(
            child_prefix_list
        )
    return out

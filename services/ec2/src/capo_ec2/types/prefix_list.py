"""Generated from Smithy shape ``com.amazonaws.ec2#PrefixList``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.value_string_list


class PrefixList(TypedDict, closed=True):
    cidrs: NotRequired["capo_ec2.types.value_string_list.ValueStringList"]
    """<p>The IP address range of the Amazon Web Services service.</p>"""
    prefix_list_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the prefix.</p>"""
    prefix_list_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the prefix.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PrefixList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cidrs" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["cidrs"], pairs, f"{key_prefix}CidrSet"
        )
    if "prefix_list_id" in value:
        pairs.append((f"{key_prefix}PrefixListId", str(value["prefix_list_id"])))
    if "prefix_list_name" in value:
        pairs.append((f"{key_prefix}PrefixListName", str(value["prefix_list_name"])))


def deserialize_ec2_query(el: Element) -> PrefixList:
    out: PrefixList = {}  # type: ignore[typeddict-item]
    if el.find("cidrSet") is not None:
        import capo_ec2.types.value_string_list

        out["cidrs"] = capo_ec2.types.value_string_list.deserialize_ec2_query(
            el, "cidrSet"
        )
    child_prefix_list_id = el.find("prefixListId")
    if child_prefix_list_id is not None:
        out["prefix_list_id"] = str(child_prefix_list_id.text or "")
    child_prefix_list_name = el.find("prefixListName")
    if child_prefix_list_name is not None:
        out["prefix_list_name"] = str(child_prefix_list_name.text or "")
    return out

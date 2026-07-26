"""Generated from Smithy shape ``com.amazonaws.ec2#PrefixListId``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class PrefixListId(TypedDict, closed=True):
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A description for the security group rule that references this prefix list ID.</p> <p>Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*</p>"""
    prefix_list_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the prefix.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PrefixListId, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "prefix_list_id" in value:
        pairs.append((f"{prefix}.PrefixListId", str(value["prefix_list_id"])))


def deserialize_ec2_query(el: Element) -> PrefixListId:
    out: PrefixListId = {}  # type: ignore[typeddict-item]
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_prefix_list_id = el.find("PrefixListId")
    if child_prefix_list_id is not None:
        out["prefix_list_id"] = str(child_prefix_list_id.text or "")
    return out

"""Generated from Smithy shape ``com.amazonaws.ec2#AddPrefixListEntry``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class AddPrefixListEntry(TypedDict):
    cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The CIDR block.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description for the entry.</p> <p>Constraints: Up to 255 characters in length.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AddPrefixListEntry, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cidr" in value:
        pairs.append((f"{prefix}.Cidr", str(value["cidr"])))
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))


def deserialize_ec2_query(el: Element) -> AddPrefixListEntry:
    out: AddPrefixListEntry = {}  # type: ignore[typeddict-item]
    child_cidr = el.find("Cidr")
    if child_cidr is not None:
        out["cidr"] = str(child_cidr.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    return out

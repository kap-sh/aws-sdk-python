"""Generated from Smithy shape ``com.amazonaws.ec2#PortRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.integer

PortRange = TypedDict(
    "PortRange",
    {
        "from": NotRequired["capo_ec2.types.integer.Integer"],
        "to": NotRequired["capo_ec2.types.integer.Integer"],
    },
    closed=True,
)


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PortRange, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "from" in value:
        pairs.append((f"{key_prefix}From", str(value["from"])))
    if "to" in value:
        pairs.append((f"{key_prefix}To", str(value["to"])))


def deserialize_ec2_query(el: Element) -> PortRange:
    out: PortRange = {}  # type: ignore[typeddict-item]
    child_from = el.find("from")
    if child_from is not None:
        out["from"] = int(child_from.text or "")
    child_to = el.find("to")
    if child_to is not None:
        out["to"] = int(child_to.text or "")
    return out

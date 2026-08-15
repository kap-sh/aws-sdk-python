"""Generated from Smithy shape ``com.amazonaws.ec2#ChronologicalOrder``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

"""<p>The chronological order for returning results.</p>"""
ChronologicalOrder: TypeAlias = Literal[
    "forward",
    "reverse",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: ChronologicalOrder) -> str:
    return value


def from_ec2_query_text(text: str) -> ChronologicalOrder:
    return cast(ChronologicalOrder, text)


def serialize_ec2_query(
    value: ChronologicalOrder, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ChronologicalOrder:
    return from_ec2_query_text(el.text or "")

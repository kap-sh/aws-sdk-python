"""Generated from Smithy shape ``com.amazonaws.cloudformation#Changes``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.change

Changes: TypeAlias = list["capo_cloudformation.types.change.Change"]


# --- awsQuery ser/de ---
def serialize_query(value: Changes, pairs: list[tuple[str, str]], prefix: str) -> None:
    import capo_cloudformation.types.change

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.change.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> Changes:
    import capo_cloudformation.types.change

    out: Changes = []
    for child in el.findall("member"):
        out.append(capo_cloudformation.types.change.deserialize_query(child))
    return out


def serialize_query_flat(
    value: Changes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudformation.types.change

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.change.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> Changes:
    import capo_cloudformation.types.change

    out: Changes = []
    for child in parent.findall(tag):
        out.append(capo_cloudformation.types.change.deserialize_query(child))
    return out

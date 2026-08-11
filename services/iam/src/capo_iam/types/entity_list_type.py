"""Generated from Smithy shape ``com.amazonaws.iam#entityListType``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.entity_type

entityListType: TypeAlias = list["capo_iam.types.entity_type.EntityType"]


# --- awsQuery ser/de ---
def serialize_query(
    value: entityListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.entity_type

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_iam.types.entity_type.serialize_query(item, pairs, f"{prefix}.member.{n}")


def deserialize_query(el: Element) -> entityListType:
    import capo_iam.types.entity_type

    out: entityListType = []
    for child in el.findall("member"):
        out.append(capo_iam.types.entity_type.deserialize_query(child))
    return out


def serialize_query_flat(
    value: entityListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.entity_type

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_iam.types.entity_type.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> entityListType:
    import capo_iam.types.entity_type

    out: entityListType = []
    for child in parent.findall(tag):
        out.append(capo_iam.types.entity_type.deserialize_query(child))
    return out

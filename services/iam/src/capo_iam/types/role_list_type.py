"""Generated from Smithy shape ``com.amazonaws.iam#roleListType``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.role

roleListType: TypeAlias = list["capo_iam.types.role.Role"]


# --- awsQuery ser/de ---
def serialize_query(
    value: roleListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.role

    for n, item in enumerate(value, 1):
        capo_iam.types.role.serialize_query(item, pairs, f"{prefix}.member.{n}")


def deserialize_query(el: Element) -> roleListType:
    import capo_iam.types.role

    out: roleListType = []
    for child in el.findall("member"):
        out.append(capo_iam.types.role.deserialize_query(child))
    return out


def serialize_query_flat(
    value: roleListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.role

    for n, item in enumerate(value, 1):
        capo_iam.types.role.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> roleListType:
    import capo_iam.types.role

    out: roleListType = []
    for child in parent.findall(tag):
        out.append(capo_iam.types.role.deserialize_query(child))
    return out

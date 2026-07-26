"""Generated from Smithy shape ``com.amazonaws.iam#userListType``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.user

userListType: TypeAlias = list["capo_iam.types.user.User"]


# --- awsQuery ser/de ---
def serialize_query(
    value: userListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.user

    for n, item in enumerate(value, 1):
        capo_iam.types.user.serialize_query(item, pairs, f"{prefix}.member.{n}")


def deserialize_query(el: Element) -> userListType:
    import capo_iam.types.user

    out: userListType = []
    for child in el.findall("member"):
        out.append(capo_iam.types.user.deserialize_query(child))
    return out


def serialize_query_flat(
    value: userListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.user

    for n, item in enumerate(value, 1):
        capo_iam.types.user.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> userListType:
    import capo_iam.types.user

    out: userListType = []
    for child in parent.findall(tag):
        out.append(capo_iam.types.user.deserialize_query(child))
    return out

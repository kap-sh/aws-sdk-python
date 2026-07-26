"""Generated from Smithy shape ``com.amazonaws.iam#RoleUsageListType``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.role_usage_type

RoleUsageListType: TypeAlias = list["capo_iam.types.role_usage_type.RoleUsageType"]


# --- awsQuery ser/de ---
def serialize_query(
    value: RoleUsageListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.role_usage_type

    for n, item in enumerate(value, 1):
        capo_iam.types.role_usage_type.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> RoleUsageListType:
    import capo_iam.types.role_usage_type

    out: RoleUsageListType = []
    for child in el.findall("member"):
        out.append(capo_iam.types.role_usage_type.deserialize_query(child))
    return out


def serialize_query_flat(
    value: RoleUsageListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.role_usage_type

    for n, item in enumerate(value, 1):
        capo_iam.types.role_usage_type.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> RoleUsageListType:
    import capo_iam.types.role_usage_type

    out: RoleUsageListType = []
    for child in parent.findall(tag):
        out.append(capo_iam.types.role_usage_type.deserialize_query(child))
    return out

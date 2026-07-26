"""Generated from Smithy shape ``com.amazonaws.iam#instanceProfileListType``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.instance_profile

instanceProfileListType: TypeAlias = list[
    "capo_iam.types.instance_profile.InstanceProfile"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: instanceProfileListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.instance_profile

    for n, item in enumerate(value, 1):
        capo_iam.types.instance_profile.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> instanceProfileListType:
    import capo_iam.types.instance_profile

    out: instanceProfileListType = []
    for child in el.findall("member"):
        out.append(capo_iam.types.instance_profile.deserialize_query(child))
    return out


def serialize_query_flat(
    value: instanceProfileListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.instance_profile

    for n, item in enumerate(value, 1):
        capo_iam.types.instance_profile.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> instanceProfileListType:
    import capo_iam.types.instance_profile

    out: instanceProfileListType = []
    for child in parent.findall(tag):
        out.append(capo_iam.types.instance_profile.deserialize_query(child))
    return out

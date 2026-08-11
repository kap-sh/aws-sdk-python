"""Generated from Smithy shape ``com.amazonaws.sts#policyDescriptorListType``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_sts._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sts.types.policy_descriptor_type

policyDescriptorListType: TypeAlias = list[
    "capo_sts.types.policy_descriptor_type.PolicyDescriptorType"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: policyDescriptorListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_sts.types.policy_descriptor_type

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_sts.types.policy_descriptor_type.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> policyDescriptorListType:
    import capo_sts.types.policy_descriptor_type

    out: policyDescriptorListType = []
    for child in el.findall("member"):
        out.append(capo_sts.types.policy_descriptor_type.deserialize_query(child))
    return out


def serialize_query_flat(
    value: policyDescriptorListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_sts.types.policy_descriptor_type

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_sts.types.policy_descriptor_type.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> policyDescriptorListType:
    import capo_sts.types.policy_descriptor_type

    out: policyDescriptorListType = []
    for child in parent.findall(tag):
        out.append(capo_sts.types.policy_descriptor_type.deserialize_query(child))
    return out

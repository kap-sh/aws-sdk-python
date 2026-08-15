"""Generated from Smithy shape ``com.amazonaws.iam#inlinePolicyTemplateListType``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.inline_policy

inlinePolicyTemplateListType: TypeAlias = list[
    "capo_iam.types.inline_policy.InlinePolicy"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: inlinePolicyTemplateListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.inline_policy

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_iam.types.inline_policy.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> inlinePolicyTemplateListType:
    import capo_iam.types.inline_policy

    out: inlinePolicyTemplateListType = []
    for child in el.findall("member"):
        out.append(capo_iam.types.inline_policy.deserialize_query(child))
    return out


def serialize_query_flat(
    value: inlinePolicyTemplateListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.inline_policy

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_iam.types.inline_policy.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> inlinePolicyTemplateListType:
    import capo_iam.types.inline_policy

    out: inlinePolicyTemplateListType = []
    for child in parent.findall(tag):
        out.append(capo_iam.types.inline_policy.deserialize_query(child))
    return out

"""Generated from Smithy shape ``com.amazonaws.redshift#UsageLimits``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.usage_limit

UsageLimits: TypeAlias = list["capo_redshift.types.usage_limit.UsageLimit"]


# --- awsQuery ser/de ---
def serialize_query(
    value: UsageLimits, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.usage_limit

    for n, item in enumerate(value, 1):
        capo_redshift.types.usage_limit.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> UsageLimits:
    import capo_redshift.types.usage_limit

    out: UsageLimits = []
    for child in el.findall("member"):
        out.append(capo_redshift.types.usage_limit.deserialize_query(child))
    return out


def serialize_query_flat(
    value: UsageLimits, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.usage_limit

    for n, item in enumerate(value, 1):
        capo_redshift.types.usage_limit.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> UsageLimits:
    import capo_redshift.types.usage_limit

    out: UsageLimits = []
    for child in parent.findall(tag):
        out.append(capo_redshift.types.usage_limit.deserialize_query(child))
    return out

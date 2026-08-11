"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#TagKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.tag_key_only

TagKeyList: TypeAlias = list[
    "capo_elastic_load_balancing.types.tag_key_only.TagKeyOnly"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: TagKeyList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing.types.tag_key_only

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing.types.tag_key_only.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> TagKeyList:
    import capo_elastic_load_balancing.types.tag_key_only

    out: TagKeyList = []
    for child in el.findall("member"):
        out.append(
            capo_elastic_load_balancing.types.tag_key_only.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: TagKeyList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing.types.tag_key_only

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing.types.tag_key_only.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> TagKeyList:
    import capo_elastic_load_balancing.types.tag_key_only

    out: TagKeyList = []
    for child in parent.findall(tag):
        out.append(
            capo_elastic_load_balancing.types.tag_key_only.deserialize_query(child)
        )
    return out

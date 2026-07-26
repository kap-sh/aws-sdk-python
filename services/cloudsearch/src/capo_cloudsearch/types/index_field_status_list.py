"""Generated from Smithy shape ``com.amazonaws.cloudsearch#IndexFieldStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudsearch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudsearch.types.index_field_status

IndexFieldStatusList: TypeAlias = list[
    "capo_cloudsearch.types.index_field_status.IndexFieldStatus"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: IndexFieldStatusList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudsearch.types.index_field_status

    for n, item in enumerate(value, 1):
        capo_cloudsearch.types.index_field_status.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> IndexFieldStatusList:
    import capo_cloudsearch.types.index_field_status

    out: IndexFieldStatusList = []
    for child in el.findall("member"):
        out.append(capo_cloudsearch.types.index_field_status.deserialize_query(child))
    return out


def serialize_query_flat(
    value: IndexFieldStatusList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudsearch.types.index_field_status

    for n, item in enumerate(value, 1):
        capo_cloudsearch.types.index_field_status.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> IndexFieldStatusList:
    import capo_cloudsearch.types.index_field_status

    out: IndexFieldStatusList = []
    for child in parent.findall(tag):
        out.append(capo_cloudsearch.types.index_field_status.deserialize_query(child))
    return out

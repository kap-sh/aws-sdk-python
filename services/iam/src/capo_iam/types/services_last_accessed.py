"""Generated from Smithy shape ``com.amazonaws.iam#ServicesLastAccessed``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.service_last_accessed

ServicesLastAccessed: TypeAlias = list[
    "capo_iam.types.service_last_accessed.ServiceLastAccessed"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ServicesLastAccessed, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.service_last_accessed

    for n, item in enumerate(value, 1):
        capo_iam.types.service_last_accessed.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ServicesLastAccessed:
    import capo_iam.types.service_last_accessed

    out: ServicesLastAccessed = []
    for child in el.findall("member"):
        out.append(capo_iam.types.service_last_accessed.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ServicesLastAccessed, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.service_last_accessed

    for n, item in enumerate(value, 1):
        capo_iam.types.service_last_accessed.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ServicesLastAccessed:
    import capo_iam.types.service_last_accessed

    out: ServicesLastAccessed = []
    for child in parent.findall(tag):
        out.append(capo_iam.types.service_last_accessed.deserialize_query(child))
    return out

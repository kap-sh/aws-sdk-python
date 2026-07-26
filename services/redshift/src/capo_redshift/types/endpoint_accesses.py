"""Generated from Smithy shape ``com.amazonaws.redshift#EndpointAccesses``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.endpoint_access

EndpointAccesses: TypeAlias = list["capo_redshift.types.endpoint_access.EndpointAccess"]


# --- awsQuery ser/de ---
def serialize_query(
    value: EndpointAccesses, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.endpoint_access

    for n, item in enumerate(value, 1):
        capo_redshift.types.endpoint_access.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> EndpointAccesses:
    import capo_redshift.types.endpoint_access

    out: EndpointAccesses = []
    for child in el.findall("member"):
        out.append(capo_redshift.types.endpoint_access.deserialize_query(child))
    return out


def serialize_query_flat(
    value: EndpointAccesses, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.endpoint_access

    for n, item in enumerate(value, 1):
        capo_redshift.types.endpoint_access.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> EndpointAccesses:
    import capo_redshift.types.endpoint_access

    out: EndpointAccesses = []
    for child in parent.findall(tag):
        out.append(capo_redshift.types.endpoint_access.deserialize_query(child))
    return out

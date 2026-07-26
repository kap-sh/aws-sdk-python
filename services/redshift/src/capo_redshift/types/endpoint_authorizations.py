"""Generated from Smithy shape ``com.amazonaws.redshift#EndpointAuthorizations``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.endpoint_authorization

EndpointAuthorizations: TypeAlias = list[
    "capo_redshift.types.endpoint_authorization.EndpointAuthorization"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: EndpointAuthorizations, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.endpoint_authorization

    for n, item in enumerate(value, 1):
        capo_redshift.types.endpoint_authorization.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> EndpointAuthorizations:
    import capo_redshift.types.endpoint_authorization

    out: EndpointAuthorizations = []
    for child in el.findall("member"):
        out.append(capo_redshift.types.endpoint_authorization.deserialize_query(child))
    return out


def serialize_query_flat(
    value: EndpointAuthorizations, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.endpoint_authorization

    for n, item in enumerate(value, 1):
        capo_redshift.types.endpoint_authorization.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> EndpointAuthorizations:
    import capo_redshift.types.endpoint_authorization

    out: EndpointAuthorizations = []
    for child in parent.findall(tag):
        out.append(capo_redshift.types.endpoint_authorization.deserialize_query(child))
    return out

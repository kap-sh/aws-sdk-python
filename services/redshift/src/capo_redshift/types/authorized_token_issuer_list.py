"""Generated from Smithy shape ``com.amazonaws.redshift#AuthorizedTokenIssuerList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.authorized_token_issuer

AuthorizedTokenIssuerList: TypeAlias = list[
    "capo_redshift.types.authorized_token_issuer.AuthorizedTokenIssuer"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: AuthorizedTokenIssuerList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.authorized_token_issuer

    for n, item in enumerate(value, 1):
        capo_redshift.types.authorized_token_issuer.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> AuthorizedTokenIssuerList:
    import capo_redshift.types.authorized_token_issuer

    out: AuthorizedTokenIssuerList = []
    for child in el.findall("member"):
        out.append(capo_redshift.types.authorized_token_issuer.deserialize_query(child))
    return out


def serialize_query_flat(
    value: AuthorizedTokenIssuerList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.authorized_token_issuer

    for n, item in enumerate(value, 1):
        capo_redshift.types.authorized_token_issuer.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> AuthorizedTokenIssuerList:
    import capo_redshift.types.authorized_token_issuer

    out: AuthorizedTokenIssuerList = []
    for child in parent.findall(tag):
        out.append(capo_redshift.types.authorized_token_issuer.deserialize_query(child))
    return out

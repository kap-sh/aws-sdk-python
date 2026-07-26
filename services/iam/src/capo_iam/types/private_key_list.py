"""Generated from Smithy shape ``com.amazonaws.iam#privateKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.saml_private_key

privateKeyList: TypeAlias = list["capo_iam.types.saml_private_key.SAMLPrivateKey"]


# --- awsQuery ser/de ---
def serialize_query(
    value: privateKeyList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.saml_private_key

    for n, item in enumerate(value, 1):
        capo_iam.types.saml_private_key.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> privateKeyList:
    import capo_iam.types.saml_private_key

    out: privateKeyList = []
    for child in el.findall("member"):
        out.append(capo_iam.types.saml_private_key.deserialize_query(child))
    return out


def serialize_query_flat(
    value: privateKeyList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.saml_private_key

    for n, item in enumerate(value, 1):
        capo_iam.types.saml_private_key.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> privateKeyList:
    import capo_iam.types.saml_private_key

    out: privateKeyList = []
    for child in parent.findall(tag):
        out.append(capo_iam.types.saml_private_key.deserialize_query(child))
    return out

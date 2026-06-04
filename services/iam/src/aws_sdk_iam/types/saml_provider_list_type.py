"""Generated from Smithy shape ``com.amazonaws.iam#SAMLProviderListType``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.saml_provider_list_entry

SAMLProviderListType: TypeAlias = list[
    "aws_sdk_iam.types.saml_provider_list_entry.SAMLProviderListEntry"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: SAMLProviderListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.saml_provider_list_entry

    for n, item in enumerate(value, 1):
        aws_sdk_iam.types.saml_provider_list_entry.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> SAMLProviderListType:
    import aws_sdk_iam.types.saml_provider_list_entry

    out: SAMLProviderListType = []
    for child in el.findall("member"):
        out.append(aws_sdk_iam.types.saml_provider_list_entry.deserialize_query(child))
    return out


def serialize_query_flat(
    value: SAMLProviderListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.saml_provider_list_entry

    for n, item in enumerate(value, 1):
        aws_sdk_iam.types.saml_provider_list_entry.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> SAMLProviderListType:
    import aws_sdk_iam.types.saml_provider_list_entry

    out: SAMLProviderListType = []
    for child in parent.findall(tag):
        out.append(aws_sdk_iam.types.saml_provider_list_entry.deserialize_query(child))
    return out

"""Generated from Smithy shape ``com.amazonaws.iam#ServiceSpecificCredentialsListType``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.service_specific_credential_metadata

ServiceSpecificCredentialsListType: TypeAlias = list[
    "aws_sdk_iam.types.service_specific_credential_metadata.ServiceSpecificCredentialMetadata"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ServiceSpecificCredentialsListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.service_specific_credential_metadata

    for n, item in enumerate(value, 1):
        aws_sdk_iam.types.service_specific_credential_metadata.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ServiceSpecificCredentialsListType:
    import aws_sdk_iam.types.service_specific_credential_metadata

    out: ServiceSpecificCredentialsListType = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_iam.types.service_specific_credential_metadata.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: ServiceSpecificCredentialsListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.service_specific_credential_metadata

    for n, item in enumerate(value, 1):
        aws_sdk_iam.types.service_specific_credential_metadata.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> ServiceSpecificCredentialsListType:
    import aws_sdk_iam.types.service_specific_credential_metadata

    out: ServiceSpecificCredentialsListType = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_iam.types.service_specific_credential_metadata.deserialize_query(
                child
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.transfer#ListedCertificates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transfer.types.listed_certificate

ListedCertificates: TypeAlias = list[
    "capo_transfer.types.listed_certificate.ListedCertificate"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListedCertificates) -> list:
    import capo_transfer.types.listed_certificate

    out: list = []
    for item in value:
        out.append(capo_transfer.types.listed_certificate.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ListedCertificates:
    import capo_transfer.types.listed_certificate

    out: ListedCertificates = []
    for item in data:
        out.append(
            capo_transfer.types.listed_certificate.deserialize_aws_json_1_1(item)
        )
    return out

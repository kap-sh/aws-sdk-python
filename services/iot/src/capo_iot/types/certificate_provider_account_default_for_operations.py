"""Generated from Smithy shape ``com.amazonaws.iot#CertificateProviderAccountDefaultForOperations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.certificate_provider_operation

CertificateProviderAccountDefaultForOperations: TypeAlias = list[
    "capo_iot.types.certificate_provider_operation.CertificateProviderOperation"
]


# --- restJson1 ser/de ---
def serialize_json(value: CertificateProviderAccountDefaultForOperations) -> list:
    import capo_iot.types.certificate_provider_operation

    out: list = []
    for item in value:
        out.append(capo_iot.types.certificate_provider_operation.serialize_json(item))
    return out


def deserialize_json(data: list) -> CertificateProviderAccountDefaultForOperations:
    import capo_iot.types.certificate_provider_operation

    out: CertificateProviderAccountDefaultForOperations = []
    for item in data:
        out.append(capo_iot.types.certificate_provider_operation.deserialize_json(item))
    return out

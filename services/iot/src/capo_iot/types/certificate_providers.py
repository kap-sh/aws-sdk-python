"""Generated from Smithy shape ``com.amazonaws.iot#CertificateProviders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.certificate_provider_summary

CertificateProviders: TypeAlias = list[
    "capo_iot.types.certificate_provider_summary.CertificateProviderSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CertificateProviders) -> list:
    import capo_iot.types.certificate_provider_summary

    out: list = []
    for item in value:
        out.append(capo_iot.types.certificate_provider_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> CertificateProviders:
    import capo_iot.types.certificate_provider_summary

    out: CertificateProviders = []
    for item in data:
        out.append(capo_iot.types.certificate_provider_summary.deserialize_json(item))
    return out

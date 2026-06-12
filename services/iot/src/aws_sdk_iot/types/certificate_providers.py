"""Generated from Smithy shape ``com.amazonaws.iot#CertificateProviders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.certificate_provider_summary

CertificateProviders: TypeAlias = list[
    "aws_sdk_iot.types.certificate_provider_summary.CertificateProviderSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CertificateProviders) -> list:
    import aws_sdk_iot.types.certificate_provider_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_iot.types.certificate_provider_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> CertificateProviders:
    import aws_sdk_iot.types.certificate_provider_summary

    out: CertificateProviders = []
    for item in data:
        out.append(
            aws_sdk_iot.types.certificate_provider_summary.deserialize_json(item)
        )
    return out

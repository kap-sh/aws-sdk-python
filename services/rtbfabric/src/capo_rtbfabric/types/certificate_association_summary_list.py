"""Generated from Smithy shape ``com.amazonaws.rtbfabric#CertificateAssociationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rtbfabric.types.certificate_association_summary

CertificateAssociationSummaryList: TypeAlias = list[
    "capo_rtbfabric.types.certificate_association_summary.CertificateAssociationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CertificateAssociationSummaryList) -> list:
    import capo_rtbfabric.types.certificate_association_summary

    out: list = []
    for item in value:
        out.append(
            capo_rtbfabric.types.certificate_association_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CertificateAssociationSummaryList:
    import capo_rtbfabric.types.certificate_association_summary

    out: CertificateAssociationSummaryList = []
    for item in data:
        out.append(
            capo_rtbfabric.types.certificate_association_summary.deserialize_json(item)
        )
    return out

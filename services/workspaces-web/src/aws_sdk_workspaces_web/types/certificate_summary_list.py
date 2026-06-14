"""Generated from Smithy shape ``com.amazonaws.workspacesweb#CertificateSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.certificate_summary

CertificateSummaryList: TypeAlias = list[
    "aws_sdk_workspaces_web.types.certificate_summary.CertificateSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CertificateSummaryList) -> list:
    import aws_sdk_workspaces_web.types.certificate_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workspaces_web.types.certificate_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CertificateSummaryList:
    import aws_sdk_workspaces_web.types.certificate_summary

    out: CertificateSummaryList = []
    for item in data:
        out.append(
            aws_sdk_workspaces_web.types.certificate_summary.deserialize_json(item)
        )
    return out

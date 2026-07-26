"""Generated from Smithy shape ``com.amazonaws.networkfirewall#AnalysisReportResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.analysis_type_report_result

AnalysisReportResults: TypeAlias = list[
    "capo_network_firewall.types.analysis_type_report_result.AnalysisTypeReportResult"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AnalysisReportResults) -> list:
    import capo_network_firewall.types.analysis_type_report_result

    out: list = []
    for item in value:
        out.append(
            capo_network_firewall.types.analysis_type_report_result.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AnalysisReportResults:
    import capo_network_firewall.types.analysis_type_report_result

    out: AnalysisReportResults = []
    for item in data:
        out.append(
            capo_network_firewall.types.analysis_type_report_result.deserialize_aws_json_1_0(
                item
            )
        )
    return out

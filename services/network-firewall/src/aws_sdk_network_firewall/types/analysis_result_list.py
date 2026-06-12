"""Generated from Smithy shape ``com.amazonaws.networkfirewall#AnalysisResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.analysis_result

AnalysisResultList: TypeAlias = list[
    "aws_sdk_network_firewall.types.analysis_result.AnalysisResult"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AnalysisResultList) -> list:
    import aws_sdk_network_firewall.types.analysis_result

    out: list = []
    for item in value:
        out.append(
            aws_sdk_network_firewall.types.analysis_result.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AnalysisResultList:
    import aws_sdk_network_firewall.types.analysis_result

    out: AnalysisResultList = []
    for item in data:
        out.append(
            aws_sdk_network_firewall.types.analysis_result.deserialize_aws_json_1_0(
                item
            )
        )
    return out

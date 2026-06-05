"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInsightsAnalysisList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_insights_analysis

NetworkInsightsAnalysisList: TypeAlias = list[
    "aws_sdk_ec2.types.network_insights_analysis.NetworkInsightsAnalysis"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NetworkInsightsAnalysisList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.network_insights_analysis

        aws_sdk_ec2.types.network_insights_analysis.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> NetworkInsightsAnalysisList:
    import aws_sdk_ec2.types.network_insights_analysis

    out: NetworkInsightsAnalysisList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.network_insights_analysis.deserialize_ec2_query(child)
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInsightsAnalysisList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.network_insights_analysis

NetworkInsightsAnalysisList: TypeAlias = list[
    "capo_ec2.types.network_insights_analysis.NetworkInsightsAnalysis"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NetworkInsightsAnalysisList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.network_insights_analysis

        capo_ec2.types.network_insights_analysis.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> NetworkInsightsAnalysisList:
    import capo_ec2.types.network_insights_analysis

    out: NetworkInsightsAnalysisList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.network_insights_analysis.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> NetworkInsightsAnalysisList:
    import capo_ec2.types.network_insights_analysis

    out: NetworkInsightsAnalysisList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.network_insights_analysis.deserialize_ec2_query(child)
        )
    return out

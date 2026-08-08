"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeNetworkInsightsAnalysesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.network_insights_analysis_list
    import capo_ec2.types.string


class DescribeNetworkInsightsAnalysesResult(TypedDict, closed=True):
    network_insights_analyses: NotRequired[
        "capo_ec2.types.network_insights_analysis_list.NetworkInsightsAnalysisList"
    ]
    """<p>Information about the network insights analyses.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeNetworkInsightsAnalysesResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "network_insights_analyses" in value:
        import capo_ec2.types.network_insights_analysis_list

        capo_ec2.types.network_insights_analysis_list.serialize_ec2_query(
            value["network_insights_analyses"],
            pairs,
            f"{key_prefix}NetworkInsightsAnalysisSet",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeNetworkInsightsAnalysesResult:
    out: DescribeNetworkInsightsAnalysesResult = {}  # type: ignore[typeddict-item]
    if el.find("networkInsightsAnalysisSet") is not None:
        import capo_ec2.types.network_insights_analysis_list

        out["network_insights_analyses"] = (
            capo_ec2.types.network_insights_analysis_list.deserialize_ec2_query(
                el, "networkInsightsAnalysisSet"
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out

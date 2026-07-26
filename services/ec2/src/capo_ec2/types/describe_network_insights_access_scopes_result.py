"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeNetworkInsightsAccessScopesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.network_insights_access_scope_list
    import capo_ec2.types.string


class DescribeNetworkInsightsAccessScopesResult(TypedDict, closed=True):
    network_insights_access_scopes: NotRequired[
        "capo_ec2.types.network_insights_access_scope_list.NetworkInsightsAccessScopeList"
    ]
    """<p>The Network Access Scopes.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeNetworkInsightsAccessScopesResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "network_insights_access_scopes" in value:
        import capo_ec2.types.network_insights_access_scope_list

        capo_ec2.types.network_insights_access_scope_list.serialize_ec2_query(
            value["network_insights_access_scopes"],
            pairs,
            f"{prefix}.NetworkInsightsAccessScopeSet",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeNetworkInsightsAccessScopesResult:
    out: DescribeNetworkInsightsAccessScopesResult = {}  # type: ignore[typeddict-item]
    if el.find("NetworkInsightsAccessScopeSet") is not None:
        import capo_ec2.types.network_insights_access_scope_list

        out["network_insights_access_scopes"] = (
            capo_ec2.types.network_insights_access_scope_list.deserialize_ec2_query(
                el, "NetworkInsightsAccessScopeSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out

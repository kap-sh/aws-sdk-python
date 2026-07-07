"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeNetworkInsightsPathsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_insights_path_list
    import aws_sdk_ec2.types.string


class DescribeNetworkInsightsPathsResult(TypedDict, closed=True):
    network_insights_paths: NotRequired[
        "aws_sdk_ec2.types.network_insights_path_list.NetworkInsightsPathList"
    ]
    """<p>Information about the paths.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeNetworkInsightsPathsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "network_insights_paths" in value:
        import aws_sdk_ec2.types.network_insights_path_list

        aws_sdk_ec2.types.network_insights_path_list.serialize_ec2_query(
            value["network_insights_paths"], pairs, f"{prefix}.NetworkInsightsPathSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeNetworkInsightsPathsResult:
    out: DescribeNetworkInsightsPathsResult = {}  # type: ignore[typeddict-item]
    if el.find("NetworkInsightsPathSet") is not None:
        import aws_sdk_ec2.types.network_insights_path_list

        out["network_insights_paths"] = (
            aws_sdk_ec2.types.network_insights_path_list.deserialize_ec2_query(
                el, "NetworkInsightsPathSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out

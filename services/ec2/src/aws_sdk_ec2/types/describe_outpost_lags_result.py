"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeOutpostLagsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.outpost_lag_set
    import aws_sdk_ec2.types.string


class DescribeOutpostLagsResult(TypedDict):
    outpost_lags: NotRequired["aws_sdk_ec2.types.outpost_lag_set.OutpostLagSet"]
    """<p>The Outpost LAGs.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeOutpostLagsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "outpost_lags" in value:
        import aws_sdk_ec2.types.outpost_lag_set

        aws_sdk_ec2.types.outpost_lag_set.serialize_ec2_query(
            value["outpost_lags"], pairs, f"{prefix}.OutpostLagSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeOutpostLagsResult:
    out: DescribeOutpostLagsResult = {}  # type: ignore[typeddict-item]
    if el.find("OutpostLagSet") is not None:
        import aws_sdk_ec2.types.outpost_lag_set

        out["outpost_lags"] = aws_sdk_ec2.types.outpost_lag_set.deserialize_ec2_query(
            el, "OutpostLagSet"
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out

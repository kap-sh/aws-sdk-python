"""Generated from Smithy shape ``com.amazonaws.ec2#GetAwsNetworkPerformanceDataResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.data_responses
    import aws_sdk_ec2.types.string


class GetAwsNetworkPerformanceDataResult(TypedDict):
    data_responses: NotRequired["aws_sdk_ec2.types.data_responses.DataResponses"]
    """<p>The list of data responses.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetAwsNetworkPerformanceDataResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "data_responses" in value:
        import aws_sdk_ec2.types.data_responses

        aws_sdk_ec2.types.data_responses.serialize_ec2_query(
            value["data_responses"], pairs, f"{prefix}.DataResponseSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetAwsNetworkPerformanceDataResult:
    out: GetAwsNetworkPerformanceDataResult = {}  # type: ignore[typeddict-item]
    if el.find("DataResponseSet") is not None:
        import aws_sdk_ec2.types.data_responses

        out["data_responses"] = aws_sdk_ec2.types.data_responses.deserialize_ec2_query(
            el, "DataResponseSet"
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out

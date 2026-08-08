"""Generated from Smithy shape ``com.amazonaws.ec2#GetAwsNetworkPerformanceDataResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.data_responses
    import capo_ec2.types.string


class GetAwsNetworkPerformanceDataResult(TypedDict, closed=True):
    data_responses: NotRequired["capo_ec2.types.data_responses.DataResponses"]
    """<p>The list of data responses.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetAwsNetworkPerformanceDataResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "data_responses" in value:
        import capo_ec2.types.data_responses

        capo_ec2.types.data_responses.serialize_ec2_query(
            value["data_responses"], pairs, f"{key_prefix}DataResponseSet"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetAwsNetworkPerformanceDataResult:
    out: GetAwsNetworkPerformanceDataResult = {}  # type: ignore[typeddict-item]
    if el.find("dataResponseSet") is not None:
        import capo_ec2.types.data_responses

        out["data_responses"] = capo_ec2.types.data_responses.deserialize_ec2_query(
            el, "dataResponseSet"
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out

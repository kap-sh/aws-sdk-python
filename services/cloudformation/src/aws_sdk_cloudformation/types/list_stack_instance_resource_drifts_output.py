"""Generated from Smithy shape ``com.amazonaws.cloudformation#ListStackInstanceResourceDriftsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.next_token
    import aws_sdk_cloudformation.types.stack_instance_resource_drifts_summaries


class ListStackInstanceResourceDriftsOutput(TypedDict, closed=True):
    summaries: NotRequired[
        "aws_sdk_cloudformation.types.stack_instance_resource_drifts_summaries.StackInstanceResourceDriftsSummaries"
    ]
    """<p>A list of <code>StackInstanceResourceDriftsSummary</code> structures that contain information about the specified stack instances.</p>"""
    next_token: NotRequired["aws_sdk_cloudformation.types.next_token.NextToken"]
    """<p>If the previous paginated request didn't return all of the remaining results, the response object's <code>NextToken</code> parameter value is set to a token. To retrieve the next set of results, call this action again and assign that token to the request object's <code>NextToken</code> parameter. If there are no remaining results, the previous response object's <code>NextToken</code> parameter is set to <code>null</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListStackInstanceResourceDriftsOutput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "summaries" in value:
        import aws_sdk_cloudformation.types.stack_instance_resource_drifts_summaries

        aws_sdk_cloudformation.types.stack_instance_resource_drifts_summaries.serialize_query(
            value["summaries"], pairs, f"{prefix}.Summaries"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListStackInstanceResourceDriftsOutput:
    out: ListStackInstanceResourceDriftsOutput = {}  # type: ignore[typeddict-item]
    child_summaries = el.find("Summaries")
    if child_summaries is not None:
        import aws_sdk_cloudformation.types.stack_instance_resource_drifts_summaries

        out["summaries"] = (
            aws_sdk_cloudformation.types.stack_instance_resource_drifts_summaries.deserialize_query(
                child_summaries
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out

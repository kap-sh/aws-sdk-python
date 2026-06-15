"""Generated from Smithy shape ``com.amazonaws.cloudformation#ListStackSetAutoDeploymentTargetsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.next_token
    import aws_sdk_cloudformation.types.stack_set_auto_deployment_target_summaries


class ListStackSetAutoDeploymentTargetsOutput(TypedDict):
    summaries: NotRequired[
        "aws_sdk_cloudformation.types.stack_set_auto_deployment_target_summaries.StackSetAutoDeploymentTargetSummaries"
    ]
    """<p>An array of summaries of the deployment targets for the StackSet.</p>"""
    next_token: NotRequired["aws_sdk_cloudformation.types.next_token.NextToken"]
    r"""<p>If the request doesn't return all the remaining results, <code>NextToken</code> is set to a token. To retrieve the next set of results, call <a href=\"https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ListStackSetAutoDeploymentTargets.html\">ListStackSetAutoDeploymentTargets</a> again and use that value for the <code>NextToken</code> parameter. If the request returns all results, <code>NextToken</code> is set to an empty string.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListStackSetAutoDeploymentTargetsOutput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "summaries" in value:
        import aws_sdk_cloudformation.types.stack_set_auto_deployment_target_summaries

        aws_sdk_cloudformation.types.stack_set_auto_deployment_target_summaries.serialize_query(
            value["summaries"], pairs, f"{prefix}.Summaries"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListStackSetAutoDeploymentTargetsOutput:
    out: ListStackSetAutoDeploymentTargetsOutput = {}  # type: ignore[typeddict-item]
    child_summaries = el.find("Summaries")
    if child_summaries is not None:
        import aws_sdk_cloudformation.types.stack_set_auto_deployment_target_summaries

        out["summaries"] = (
            aws_sdk_cloudformation.types.stack_set_auto_deployment_target_summaries.deserialize_query(
                child_summaries
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out

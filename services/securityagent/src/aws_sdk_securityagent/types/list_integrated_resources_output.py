"""Generated from Smithy shape ``com.amazonaws.securityagent#ListIntegratedResourcesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.integrated_resource_summary_list
    import aws_sdk_securityagent.types.next_token


class ListIntegratedResourcesOutput(TypedDict, closed=True):
    integrated_resource_summaries: "aws_sdk_securityagent.types.integrated_resource_summary_list.IntegratedResourceSummaryList"
    """<p>The list of integrated resource summaries.</p>"""
    next_token: NotRequired["aws_sdk_securityagent.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIntegratedResourcesOutput) -> dict:
    out: dict = {}
    import aws_sdk_securityagent.types.integrated_resource_summary_list

    out["integratedResourceSummaries"] = (
        aws_sdk_securityagent.types.integrated_resource_summary_list.serialize_json(
            value["integrated_resource_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListIntegratedResourcesOutput:
    out: ListIntegratedResourcesOutput = {}  # type: ignore[typeddict-item]
    if "integratedResourceSummaries" in data:
        import aws_sdk_securityagent.types.integrated_resource_summary_list

        out["integrated_resource_summaries"] = (
            aws_sdk_securityagent.types.integrated_resource_summary_list.deserialize_json(
                data["integratedResourceSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListIntegratedResourcesOutput.integrated_resource_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out

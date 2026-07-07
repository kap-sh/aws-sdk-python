"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#GetFlowTemplateRevisionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.flow_template_summaries
    import aws_sdk_iotthingsgraph.types.next_token


class GetFlowTemplateRevisionsResponse(TypedDict, closed=True):
    summaries: NotRequired[
        "aws_sdk_iotthingsgraph.types.flow_template_summaries.FlowTemplateSummaries"
    ]
    """<p>An array of objects that provide summary data about each revision.</p>"""
    next_token: NotRequired["aws_sdk_iotthingsgraph.types.next_token.NextToken"]
    """<p>The string to specify as <code>nextToken</code> when you request the next page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetFlowTemplateRevisionsResponse) -> dict:
    out: dict = {}
    if "summaries" in value:
        import aws_sdk_iotthingsgraph.types.flow_template_summaries

        out["summaries"] = (
            aws_sdk_iotthingsgraph.types.flow_template_summaries.serialize_aws_json_1_1(
                value["summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetFlowTemplateRevisionsResponse:
    out: GetFlowTemplateRevisionsResponse = {}  # type: ignore[typeddict-item]
    if "summaries" in data:
        import aws_sdk_iotthingsgraph.types.flow_template_summaries

        out["summaries"] = (
            aws_sdk_iotthingsgraph.types.flow_template_summaries.deserialize_aws_json_1_1(
                data["summaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out

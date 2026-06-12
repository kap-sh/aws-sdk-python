"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#GetSystemTemplateRevisionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.next_token
    import aws_sdk_iotthingsgraph.types.system_template_summaries


class GetSystemTemplateRevisionsResponse(TypedDict):
    summaries: NotRequired[
        "aws_sdk_iotthingsgraph.types.system_template_summaries.SystemTemplateSummaries"
    ]
    """<p>An array of objects that contain summary data about the system template revisions.</p>"""
    next_token: NotRequired["aws_sdk_iotthingsgraph.types.next_token.NextToken"]
    """<p>The string to specify as <code>nextToken</code> when you request the next page of results. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSystemTemplateRevisionsResponse) -> dict:
    out: dict = {}
    if "summaries" in value:
        import aws_sdk_iotthingsgraph.types.system_template_summaries

        out["summaries"] = (
            aws_sdk_iotthingsgraph.types.system_template_summaries.serialize_aws_json_1_1(
                value["summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSystemTemplateRevisionsResponse:
    out: GetSystemTemplateRevisionsResponse = {}  # type: ignore[typeddict-item]
    if "summaries" in data:
        import aws_sdk_iotthingsgraph.types.system_template_summaries

        out["summaries"] = (
            aws_sdk_iotthingsgraph.types.system_template_summaries.deserialize_aws_json_1_1(
                data["summaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out

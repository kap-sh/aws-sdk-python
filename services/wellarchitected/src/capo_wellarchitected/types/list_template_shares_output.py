"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListTemplateSharesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.next_token
    import capo_wellarchitected.types.template_arn
    import capo_wellarchitected.types.template_share_summaries


class ListTemplateSharesOutput(TypedDict, closed=True):
    template_arn: NotRequired["capo_wellarchitected.types.template_arn.TemplateArn"]
    """<p>The review template ARN.</p>"""
    template_share_summaries: NotRequired[
        "capo_wellarchitected.types.template_share_summaries.TemplateShareSummaries"
    ]
    """<p>A review template share summary return object.</p>"""
    next_token: NotRequired["capo_wellarchitected.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListTemplateSharesOutput) -> dict:
    out: dict = {}
    if "template_arn" in value:
        out["TemplateArn"] = value["template_arn"]
    if "template_share_summaries" in value:
        import capo_wellarchitected.types.template_share_summaries

        out["TemplateShareSummaries"] = (
            capo_wellarchitected.types.template_share_summaries.serialize_json(
                value["template_share_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTemplateSharesOutput:
    out: ListTemplateSharesOutput = {}  # type: ignore[typeddict-item]
    if "TemplateArn" in data:
        out["template_arn"] = data["TemplateArn"]
    if "TemplateShareSummaries" in data:
        import capo_wellarchitected.types.template_share_summaries

        out["template_share_summaries"] = (
            capo_wellarchitected.types.template_share_summaries.deserialize_json(
                data["TemplateShareSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

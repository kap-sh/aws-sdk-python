"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ListLabelGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.label_group_summaries
    import capo_lookoutequipment.types.next_token


class ListLabelGroupsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_lookoutequipment.types.next_token.NextToken"]
    """<p> An opaque pagination token indicating where to continue the listing of label groups. </p>"""
    label_group_summaries: NotRequired[
        "capo_lookoutequipment.types.label_group_summaries.LabelGroupSummaries"
    ]
    """<p> A summary of the label groups. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListLabelGroupsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "label_group_summaries" in value:
        import capo_lookoutequipment.types.label_group_summaries

        out["LabelGroupSummaries"] = (
            capo_lookoutequipment.types.label_group_summaries.serialize_aws_json_1_0(
                value["label_group_summaries"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListLabelGroupsResponse:
    out: ListLabelGroupsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "LabelGroupSummaries" in data:
        import capo_lookoutequipment.types.label_group_summaries

        out["label_group_summaries"] = (
            capo_lookoutequipment.types.label_group_summaries.deserialize_aws_json_1_0(
                data["LabelGroupSummaries"]
            )
        )
    return out

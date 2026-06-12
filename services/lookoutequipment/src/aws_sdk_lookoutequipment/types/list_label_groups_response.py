"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ListLabelGroupsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.label_group_summaries
    import aws_sdk_lookoutequipment.types.next_token


class ListLabelGroupsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_lookoutequipment.types.next_token.NextToken"]
    """<p> An opaque pagination token indicating where to continue the listing of label groups. </p>"""
    label_group_summaries: NotRequired[
        "aws_sdk_lookoutequipment.types.label_group_summaries.LabelGroupSummaries"
    ]
    """<p> A summary of the label groups. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListLabelGroupsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "label_group_summaries" in value:
        import aws_sdk_lookoutequipment.types.label_group_summaries

        out["LabelGroupSummaries"] = (
            aws_sdk_lookoutequipment.types.label_group_summaries.serialize_aws_json_1_0(
                value["label_group_summaries"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListLabelGroupsResponse:
    out: ListLabelGroupsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "LabelGroupSummaries" in data:
        import aws_sdk_lookoutequipment.types.label_group_summaries

        out["label_group_summaries"] = (
            aws_sdk_lookoutequipment.types.label_group_summaries.deserialize_aws_json_1_0(
                data["LabelGroupSummaries"]
            )
        )
    return out

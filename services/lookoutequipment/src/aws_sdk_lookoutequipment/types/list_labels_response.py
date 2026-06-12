"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ListLabelsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.label_summaries
    import aws_sdk_lookoutequipment.types.next_token


class ListLabelsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_lookoutequipment.types.next_token.NextToken"]
    """<p> An opaque pagination token indicating where to continue the listing of datasets. </p>"""
    label_summaries: NotRequired[
        "aws_sdk_lookoutequipment.types.label_summaries.LabelSummaries"
    ]
    """<p> A summary of the items in the label group. </p> <note> <p>If you don't supply the <code>LabelGroupName</code> request parameter, or if you supply the name of a label group that doesn't exist, <code>ListLabels</code> returns an empty array in <code>LabelSummaries</code>.</p> </note>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListLabelsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "label_summaries" in value:
        import aws_sdk_lookoutequipment.types.label_summaries

        out["LabelSummaries"] = (
            aws_sdk_lookoutequipment.types.label_summaries.serialize_aws_json_1_0(
                value["label_summaries"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListLabelsResponse:
    out: ListLabelsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "LabelSummaries" in data:
        import aws_sdk_lookoutequipment.types.label_summaries

        out["label_summaries"] = (
            aws_sdk_lookoutequipment.types.label_summaries.deserialize_aws_json_1_0(
                data["LabelSummaries"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ListLabelGroupsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.label_group_name
    import aws_sdk_lookoutequipment.types.max_results
    import aws_sdk_lookoutequipment.types.next_token


class ListLabelGroupsRequest(TypedDict):
    label_group_name_begins_with: NotRequired[
        "aws_sdk_lookoutequipment.types.label_group_name.LabelGroupName"
    ]
    """<p> The beginning of the name of the label groups to be listed. </p>"""
    next_token: NotRequired["aws_sdk_lookoutequipment.types.next_token.NextToken"]
    """<p> An opaque pagination token indicating where to continue the listing of label groups. </p>"""
    max_results: NotRequired["aws_sdk_lookoutequipment.types.max_results.MaxResults"]
    """<p> Specifies the maximum number of label groups to list. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListLabelGroupsRequest) -> dict:
    out: dict = {}
    if "label_group_name_begins_with" in value:
        out["LabelGroupNameBeginsWith"] = value["label_group_name_begins_with"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListLabelGroupsRequest:
    out: ListLabelGroupsRequest = {}  # type: ignore[typeddict-item]
    if "LabelGroupNameBeginsWith" in data:
        out["label_group_name_begins_with"] = data["LabelGroupNameBeginsWith"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out

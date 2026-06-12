"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#DescribeLabelRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lookoutequipment.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.label_group_name
    import aws_sdk_lookoutequipment.types.label_id


class DescribeLabelRequest(TypedDict):
    label_group_name: "aws_sdk_lookoutequipment.types.label_group_name.LabelGroupName"
    """<p> Returns the name of the group containing the label. </p>"""
    label_id: "aws_sdk_lookoutequipment.types.label_id.LabelId"
    """<p> Returns the ID of the label. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeLabelRequest) -> dict:
    out: dict = {}
    out["LabelGroupName"] = value["label_group_name"]
    out["LabelId"] = value["label_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeLabelRequest:
    out: DescribeLabelRequest = {}  # type: ignore[typeddict-item]
    if "LabelGroupName" in data:
        out["label_group_name"] = data["LabelGroupName"]
    else:
        raise DeserializationError("DescribeLabelRequest.label_group_name required")
    if "LabelId" in data:
        out["label_id"] = data["LabelId"]
    else:
        raise DeserializationError("DescribeLabelRequest.label_id required")
    return out

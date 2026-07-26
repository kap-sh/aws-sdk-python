"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#CreateLabelGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.label_group_arn
    import capo_lookoutequipment.types.label_group_name


class CreateLabelGroupResponse(TypedDict, closed=True):
    label_group_name: NotRequired[
        "capo_lookoutequipment.types.label_group_name.LabelGroupName"
    ]
    """<p> The name of the label group that you have created. Data in this field will be retained for service usage. Follow best practices for the security of your data. </p>"""
    label_group_arn: NotRequired[
        "capo_lookoutequipment.types.label_group_arn.LabelGroupArn"
    ]
    """<p> The Amazon Resource Name (ARN) of the label group that you have created. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateLabelGroupResponse) -> dict:
    out: dict = {}
    if "label_group_name" in value:
        out["LabelGroupName"] = value["label_group_name"]
    if "label_group_arn" in value:
        out["LabelGroupArn"] = value["label_group_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateLabelGroupResponse:
    out: CreateLabelGroupResponse = {}  # type: ignore[typeddict-item]
    if "LabelGroupName" in data:
        out["label_group_name"] = data["LabelGroupName"]
    if "LabelGroupArn" in data:
        out["label_group_arn"] = data["LabelGroupArn"]
    return out

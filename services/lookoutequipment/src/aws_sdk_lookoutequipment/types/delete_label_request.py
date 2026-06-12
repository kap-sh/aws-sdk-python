"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#DeleteLabelRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lookoutequipment.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.label_group_name
    import aws_sdk_lookoutequipment.types.label_id


class DeleteLabelRequest(TypedDict):
    label_group_name: "aws_sdk_lookoutequipment.types.label_group_name.LabelGroupName"
    """<p> The name of the label group that contains the label that you want to delete. Data in this field will be retained for service usage. Follow best practices for the security of your data. </p>"""
    label_id: "aws_sdk_lookoutequipment.types.label_id.LabelId"
    """<p> The ID of the label that you want to delete. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteLabelRequest) -> dict:
    out: dict = {}
    out["LabelGroupName"] = value["label_group_name"]
    out["LabelId"] = value["label_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteLabelRequest:
    out: DeleteLabelRequest = {}  # type: ignore[typeddict-item]
    if "LabelGroupName" in data:
        out["label_group_name"] = data["LabelGroupName"]
    else:
        raise DeserializationError("DeleteLabelRequest.label_group_name required")
    if "LabelId" in data:
        out["label_id"] = data["LabelId"]
    else:
        raise DeserializationError("DeleteLabelRequest.label_id required")
    return out

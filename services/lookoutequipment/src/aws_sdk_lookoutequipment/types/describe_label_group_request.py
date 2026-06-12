"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#DescribeLabelGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lookoutequipment.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.label_group_name


class DescribeLabelGroupRequest(TypedDict):
    label_group_name: "aws_sdk_lookoutequipment.types.label_group_name.LabelGroupName"
    """<p> Returns the name of the label group. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeLabelGroupRequest) -> dict:
    out: dict = {}
    out["LabelGroupName"] = value["label_group_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeLabelGroupRequest:
    out: DescribeLabelGroupRequest = {}  # type: ignore[typeddict-item]
    if "LabelGroupName" in data:
        out["label_group_name"] = data["LabelGroupName"]
    else:
        raise DeserializationError(
            "DescribeLabelGroupRequest.label_group_name required"
        )
    return out

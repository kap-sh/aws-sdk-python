"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#CreateLabelResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.label_id


class CreateLabelResponse(TypedDict):
    label_id: NotRequired["aws_sdk_lookoutequipment.types.label_id.LabelId"]
    """<p> The ID of the label that you have created. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateLabelResponse) -> dict:
    out: dict = {}
    if "label_id" in value:
        out["LabelId"] = value["label_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateLabelResponse:
    out: CreateLabelResponse = {}  # type: ignore[typeddict-item]
    if "LabelId" in data:
        out["label_id"] = data["LabelId"]
    return out

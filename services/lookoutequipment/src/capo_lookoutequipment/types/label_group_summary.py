"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#LabelGroupSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.label_group_arn
    import capo_lookoutequipment.types.label_group_name
    import capo_lookoutequipment.types.timestamp


class LabelGroupSummary(TypedDict, closed=True):
    label_group_name: NotRequired[
        "capo_lookoutequipment.types.label_group_name.LabelGroupName"
    ]
    """<p> The name of the label group. </p>"""
    label_group_arn: NotRequired[
        "capo_lookoutequipment.types.label_group_arn.LabelGroupArn"
    ]
    """<p> The Amazon Resource Name (ARN) of the label group. </p>"""
    created_at: NotRequired["capo_lookoutequipment.types.timestamp.Timestamp"]
    """<p> The time at which the label group was created. </p>"""
    updated_at: NotRequired["capo_lookoutequipment.types.timestamp.Timestamp"]
    """<p> The time at which the label group was updated. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LabelGroupSummary) -> dict:
    out: dict = {}
    if "label_group_name" in value:
        out["LabelGroupName"] = value["label_group_name"]
    if "label_group_arn" in value:
        out["LabelGroupArn"] = value["label_group_arn"]
    if "created_at" in value:
        import capo_lookoutequipment.types.timestamp

        out["CreatedAt"] = capo_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_lookoutequipment.types.timestamp

        out["UpdatedAt"] = capo_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
            value["updated_at"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> LabelGroupSummary:
    out: LabelGroupSummary = {}  # type: ignore[typeddict-item]
    if "LabelGroupName" in data:
        out["label_group_name"] = data["LabelGroupName"]
    if "LabelGroupArn" in data:
        out["label_group_arn"] = data["LabelGroupArn"]
    if "CreatedAt" in data:
        import capo_lookoutequipment.types.timestamp

        out["created_at"] = (
            capo_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["CreatedAt"]
            )
        )
    if "UpdatedAt" in data:
        import capo_lookoutequipment.types.timestamp

        out["updated_at"] = (
            capo_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["UpdatedAt"]
            )
        )
    return out

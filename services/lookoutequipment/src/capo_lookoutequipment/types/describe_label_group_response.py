"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#DescribeLabelGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.fault_codes
    import capo_lookoutequipment.types.label_group_arn
    import capo_lookoutequipment.types.label_group_name
    import capo_lookoutequipment.types.timestamp


class DescribeLabelGroupResponse(TypedDict, closed=True):
    label_group_name: NotRequired[
        "capo_lookoutequipment.types.label_group_name.LabelGroupName"
    ]
    """<p> The name of the label group. </p>"""
    label_group_arn: NotRequired[
        "capo_lookoutequipment.types.label_group_arn.LabelGroupArn"
    ]
    """<p> The Amazon Resource Name (ARN) of the label group. </p>"""
    fault_codes: NotRequired["capo_lookoutequipment.types.fault_codes.FaultCodes"]
    """<p> Codes indicating the type of anomaly associated with the labels in the lagbel group. </p>"""
    created_at: NotRequired["capo_lookoutequipment.types.timestamp.Timestamp"]
    """<p> The time at which the label group was created. </p>"""
    updated_at: NotRequired["capo_lookoutequipment.types.timestamp.Timestamp"]
    """<p> The time at which the label group was updated. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeLabelGroupResponse) -> dict:
    out: dict = {}
    if "label_group_name" in value:
        out["LabelGroupName"] = value["label_group_name"]
    if "label_group_arn" in value:
        out["LabelGroupArn"] = value["label_group_arn"]
    if "fault_codes" in value:
        import capo_lookoutequipment.types.fault_codes

        out["FaultCodes"] = (
            capo_lookoutequipment.types.fault_codes.serialize_aws_json_1_0(
                value["fault_codes"]
            )
        )
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


def deserialize_aws_json_1_0(data: dict) -> DescribeLabelGroupResponse:
    out: DescribeLabelGroupResponse = {}  # type: ignore[typeddict-item]
    if "LabelGroupName" in data:
        out["label_group_name"] = data["LabelGroupName"]
    if "LabelGroupArn" in data:
        out["label_group_arn"] = data["LabelGroupArn"]
    if "FaultCodes" in data:
        import capo_lookoutequipment.types.fault_codes

        out["fault_codes"] = (
            capo_lookoutequipment.types.fault_codes.deserialize_aws_json_1_0(
                data["FaultCodes"]
            )
        )
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

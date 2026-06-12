"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#DescribeLabelGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.fault_codes
    import aws_sdk_lookoutequipment.types.label_group_arn
    import aws_sdk_lookoutequipment.types.label_group_name
    import aws_sdk_lookoutequipment.types.timestamp


class DescribeLabelGroupResponse(TypedDict):
    label_group_name: NotRequired[
        "aws_sdk_lookoutequipment.types.label_group_name.LabelGroupName"
    ]
    """<p> The name of the label group. </p>"""
    label_group_arn: NotRequired[
        "aws_sdk_lookoutequipment.types.label_group_arn.LabelGroupArn"
    ]
    """<p> The Amazon Resource Name (ARN) of the label group. </p>"""
    fault_codes: NotRequired["aws_sdk_lookoutequipment.types.fault_codes.FaultCodes"]
    """<p> Codes indicating the type of anomaly associated with the labels in the lagbel group. </p>"""
    created_at: NotRequired["aws_sdk_lookoutequipment.types.timestamp.Timestamp"]
    """<p> The time at which the label group was created. </p>"""
    updated_at: NotRequired["aws_sdk_lookoutequipment.types.timestamp.Timestamp"]
    """<p> The time at which the label group was updated. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeLabelGroupResponse) -> dict:
    out: dict = {}
    if "label_group_name" in value:
        out["LabelGroupName"] = value["label_group_name"]
    if "label_group_arn" in value:
        out["LabelGroupArn"] = value["label_group_arn"]
    if "fault_codes" in value:
        import aws_sdk_lookoutequipment.types.fault_codes

        out["FaultCodes"] = (
            aws_sdk_lookoutequipment.types.fault_codes.serialize_aws_json_1_0(
                value["fault_codes"]
            )
        )
    if "created_at" in value:
        import aws_sdk_lookoutequipment.types.timestamp

        out["CreatedAt"] = (
            aws_sdk_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import aws_sdk_lookoutequipment.types.timestamp

        out["UpdatedAt"] = (
            aws_sdk_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["updated_at"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeLabelGroupResponse:
    out: DescribeLabelGroupResponse = {}  # type: ignore[typeddict-item]
    if "LabelGroupName" in data:
        out["label_group_name"] = data["LabelGroupName"]
    if "LabelGroupArn" in data:
        out["label_group_arn"] = data["LabelGroupArn"]
    if "FaultCodes" in data:
        import aws_sdk_lookoutequipment.types.fault_codes

        out["fault_codes"] = (
            aws_sdk_lookoutequipment.types.fault_codes.deserialize_aws_json_1_0(
                data["FaultCodes"]
            )
        )
    if "CreatedAt" in data:
        import aws_sdk_lookoutequipment.types.timestamp

        out["created_at"] = (
            aws_sdk_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["CreatedAt"]
            )
        )
    if "UpdatedAt" in data:
        import aws_sdk_lookoutequipment.types.timestamp

        out["updated_at"] = (
            aws_sdk_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["UpdatedAt"]
            )
        )
    return out

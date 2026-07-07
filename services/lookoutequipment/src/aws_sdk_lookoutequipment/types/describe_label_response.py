"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#DescribeLabelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.comments
    import aws_sdk_lookoutequipment.types.equipment
    import aws_sdk_lookoutequipment.types.fault_code
    import aws_sdk_lookoutequipment.types.label_group_arn
    import aws_sdk_lookoutequipment.types.label_group_name
    import aws_sdk_lookoutequipment.types.label_id
    import aws_sdk_lookoutequipment.types.label_rating
    import aws_sdk_lookoutequipment.types.timestamp


class DescribeLabelResponse(TypedDict, closed=True):
    label_group_name: NotRequired[
        "aws_sdk_lookoutequipment.types.label_group_name.LabelGroupName"
    ]
    """<p> The name of the requested label group. </p>"""
    label_group_arn: NotRequired[
        "aws_sdk_lookoutequipment.types.label_group_arn.LabelGroupArn"
    ]
    """<p> The Amazon Resource Name (ARN) of the requested label group. </p>"""
    label_id: NotRequired["aws_sdk_lookoutequipment.types.label_id.LabelId"]
    """<p> The ID of the requested label. </p>"""
    start_time: NotRequired["aws_sdk_lookoutequipment.types.timestamp.Timestamp"]
    """<p> The start time of the requested label. </p>"""
    end_time: NotRequired["aws_sdk_lookoutequipment.types.timestamp.Timestamp"]
    """<p> The end time of the requested label. </p>"""
    rating: NotRequired["aws_sdk_lookoutequipment.types.label_rating.LabelRating"]
    """<p> Indicates whether a labeled event represents an anomaly. </p>"""
    fault_code: NotRequired["aws_sdk_lookoutequipment.types.fault_code.FaultCode"]
    """<p> Indicates the type of anomaly associated with the label. </p> <p>Data in this field will be retained for service usage. Follow best practices for the security of your data.</p>"""
    notes: NotRequired["aws_sdk_lookoutequipment.types.comments.Comments"]
    """<p>Metadata providing additional information about the label.</p> <p>Data in this field will be retained for service usage. Follow best practices for the security of your data.</p>"""
    equipment: NotRequired["aws_sdk_lookoutequipment.types.equipment.Equipment"]
    """<p> Indicates that a label pertains to a particular piece of equipment. </p>"""
    created_at: NotRequired["aws_sdk_lookoutequipment.types.timestamp.Timestamp"]
    """<p> The time at which the label was created. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeLabelResponse) -> dict:
    out: dict = {}
    if "label_group_name" in value:
        out["LabelGroupName"] = value["label_group_name"]
    if "label_group_arn" in value:
        out["LabelGroupArn"] = value["label_group_arn"]
    if "label_id" in value:
        out["LabelId"] = value["label_id"]
    if "start_time" in value:
        import aws_sdk_lookoutequipment.types.timestamp

        out["StartTime"] = (
            aws_sdk_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["start_time"]
            )
        )
    if "end_time" in value:
        import aws_sdk_lookoutequipment.types.timestamp

        out["EndTime"] = (
            aws_sdk_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["end_time"]
            )
        )
    if "rating" in value:
        import aws_sdk_lookoutequipment.types.label_rating

        out["Rating"] = (
            aws_sdk_lookoutequipment.types.label_rating.serialize_aws_json_1_0(
                value["rating"]
            )
        )
    if "fault_code" in value:
        out["FaultCode"] = value["fault_code"]
    if "notes" in value:
        out["Notes"] = value["notes"]
    if "equipment" in value:
        out["Equipment"] = value["equipment"]
    if "created_at" in value:
        import aws_sdk_lookoutequipment.types.timestamp

        out["CreatedAt"] = (
            aws_sdk_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["created_at"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeLabelResponse:
    out: DescribeLabelResponse = {}  # type: ignore[typeddict-item]
    if "LabelGroupName" in data:
        out["label_group_name"] = data["LabelGroupName"]
    if "LabelGroupArn" in data:
        out["label_group_arn"] = data["LabelGroupArn"]
    if "LabelId" in data:
        out["label_id"] = data["LabelId"]
    if "StartTime" in data:
        import aws_sdk_lookoutequipment.types.timestamp

        out["start_time"] = (
            aws_sdk_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["StartTime"]
            )
        )
    if "EndTime" in data:
        import aws_sdk_lookoutequipment.types.timestamp

        out["end_time"] = (
            aws_sdk_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["EndTime"]
            )
        )
    if "Rating" in data:
        import aws_sdk_lookoutequipment.types.label_rating

        out["rating"] = (
            aws_sdk_lookoutequipment.types.label_rating.deserialize_aws_json_1_0(
                data["Rating"]
            )
        )
    if "FaultCode" in data:
        out["fault_code"] = data["FaultCode"]
    if "Notes" in data:
        out["notes"] = data["Notes"]
    if "Equipment" in data:
        out["equipment"] = data["Equipment"]
    if "CreatedAt" in data:
        import aws_sdk_lookoutequipment.types.timestamp

        out["created_at"] = (
            aws_sdk_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["CreatedAt"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ListLabelsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lookoutequipment.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.equipment
    import aws_sdk_lookoutequipment.types.fault_code
    import aws_sdk_lookoutequipment.types.label_group_name
    import aws_sdk_lookoutequipment.types.max_results
    import aws_sdk_lookoutequipment.types.next_token
    import aws_sdk_lookoutequipment.types.timestamp


class ListLabelsRequest(TypedDict, closed=True):
    label_group_name: "aws_sdk_lookoutequipment.types.label_group_name.LabelGroupName"
    """<p> Returns the name of the label group. </p>"""
    interval_start_time: NotRequired[
        "aws_sdk_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p> Returns all the labels with a end time equal to or later than the start time given. </p>"""
    interval_end_time: NotRequired["aws_sdk_lookoutequipment.types.timestamp.Timestamp"]
    """<p> Returns all labels with a start time earlier than the end time given. </p>"""
    fault_code: NotRequired["aws_sdk_lookoutequipment.types.fault_code.FaultCode"]
    """<p> Returns labels with a particular fault code. </p>"""
    equipment: NotRequired["aws_sdk_lookoutequipment.types.equipment.Equipment"]
    """<p> Lists the labels that pertain to a particular piece of equipment. </p>"""
    next_token: NotRequired["aws_sdk_lookoutequipment.types.next_token.NextToken"]
    """<p> An opaque pagination token indicating where to continue the listing of label groups. </p>"""
    max_results: NotRequired["aws_sdk_lookoutequipment.types.max_results.MaxResults"]
    """<p> Specifies the maximum number of labels to list. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListLabelsRequest) -> dict:
    out: dict = {}
    out["LabelGroupName"] = value["label_group_name"]
    if "interval_start_time" in value:
        import aws_sdk_lookoutequipment.types.timestamp

        out["IntervalStartTime"] = (
            aws_sdk_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["interval_start_time"]
            )
        )
    if "interval_end_time" in value:
        import aws_sdk_lookoutequipment.types.timestamp

        out["IntervalEndTime"] = (
            aws_sdk_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["interval_end_time"]
            )
        )
    if "fault_code" in value:
        out["FaultCode"] = value["fault_code"]
    if "equipment" in value:
        out["Equipment"] = value["equipment"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListLabelsRequest:
    out: ListLabelsRequest = {}  # type: ignore[typeddict-item]
    if "LabelGroupName" in data:
        out["label_group_name"] = data["LabelGroupName"]
    else:
        raise DeserializationError("ListLabelsRequest.label_group_name required")
    if "IntervalStartTime" in data:
        import aws_sdk_lookoutequipment.types.timestamp

        out["interval_start_time"] = (
            aws_sdk_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["IntervalStartTime"]
            )
        )
    if "IntervalEndTime" in data:
        import aws_sdk_lookoutequipment.types.timestamp

        out["interval_end_time"] = (
            aws_sdk_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["IntervalEndTime"]
            )
        )
    if "FaultCode" in data:
        out["fault_code"] = data["FaultCode"]
    if "Equipment" in data:
        out["equipment"] = data["Equipment"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out

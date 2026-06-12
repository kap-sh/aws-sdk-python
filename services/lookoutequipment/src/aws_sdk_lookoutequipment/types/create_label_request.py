"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#CreateLabelRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lookoutequipment.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.comments
    import aws_sdk_lookoutequipment.types.equipment
    import aws_sdk_lookoutequipment.types.fault_code
    import aws_sdk_lookoutequipment.types.idempotence_token
    import aws_sdk_lookoutequipment.types.label_group_name
    import aws_sdk_lookoutequipment.types.label_rating
    import aws_sdk_lookoutequipment.types.timestamp


class CreateLabelRequest(TypedDict):
    label_group_name: "aws_sdk_lookoutequipment.types.label_group_name.LabelGroupName"
    """<p> The name of a group of labels. </p> <p>Data in this field will be retained for service usage. Follow best practices for the security of your data. </p>"""
    start_time: "aws_sdk_lookoutequipment.types.timestamp.Timestamp"
    """<p> The start time of the labeled event. </p>"""
    end_time: "aws_sdk_lookoutequipment.types.timestamp.Timestamp"
    """<p> The end time of the labeled event. </p>"""
    rating: "aws_sdk_lookoutequipment.types.label_rating.LabelRating"
    """<p> Indicates whether a labeled event represents an anomaly. </p>"""
    fault_code: NotRequired["aws_sdk_lookoutequipment.types.fault_code.FaultCode"]
    """<p> Provides additional information about the label. The fault code must be defined in the FaultCodes attribute of the label group.</p> <p>Data in this field will be retained for service usage. Follow best practices for the security of your data. </p>"""
    notes: NotRequired["aws_sdk_lookoutequipment.types.comments.Comments"]
    """<p> Metadata providing additional information about the label. </p> <p>Data in this field will be retained for service usage. Follow best practices for the security of your data.</p>"""
    equipment: NotRequired["aws_sdk_lookoutequipment.types.equipment.Equipment"]
    """<p> Indicates that a label pertains to a particular piece of equipment. </p> <p>Data in this field will be retained for service usage. Follow best practices for the security of your data.</p>"""
    client_token: "aws_sdk_lookoutequipment.types.idempotence_token.IdempotenceToken"
    """<p> A unique identifier for the request to create a label. If you do not set the client request token, Lookout for Equipment generates one. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateLabelRequest) -> dict:
    out: dict = {}
    out["LabelGroupName"] = value["label_group_name"]
    import aws_sdk_lookoutequipment.types.timestamp

    out["StartTime"] = aws_sdk_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
        value["start_time"]
    )
    import aws_sdk_lookoutequipment.types.timestamp

    out["EndTime"] = aws_sdk_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
        value["end_time"]
    )
    import aws_sdk_lookoutequipment.types.label_rating

    out["Rating"] = aws_sdk_lookoutequipment.types.label_rating.serialize_aws_json_1_0(
        value["rating"]
    )
    if "fault_code" in value:
        out["FaultCode"] = value["fault_code"]
    if "notes" in value:
        out["Notes"] = value["notes"]
    if "equipment" in value:
        out["Equipment"] = value["equipment"]
    out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateLabelRequest:
    out: CreateLabelRequest = {}  # type: ignore[typeddict-item]
    if "LabelGroupName" in data:
        out["label_group_name"] = data["LabelGroupName"]
    else:
        raise DeserializationError("CreateLabelRequest.label_group_name required")
    if "StartTime" in data:
        import aws_sdk_lookoutequipment.types.timestamp

        out["start_time"] = (
            aws_sdk_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["StartTime"]
            )
        )
    else:
        raise DeserializationError("CreateLabelRequest.start_time required")
    if "EndTime" in data:
        import aws_sdk_lookoutequipment.types.timestamp

        out["end_time"] = (
            aws_sdk_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["EndTime"]
            )
        )
    else:
        raise DeserializationError("CreateLabelRequest.end_time required")
    if "Rating" in data:
        import aws_sdk_lookoutequipment.types.label_rating

        out["rating"] = (
            aws_sdk_lookoutequipment.types.label_rating.deserialize_aws_json_1_0(
                data["Rating"]
            )
        )
    else:
        raise DeserializationError("CreateLabelRequest.rating required")
    if "FaultCode" in data:
        out["fault_code"] = data["FaultCode"]
    if "Notes" in data:
        out["notes"] = data["Notes"]
    if "Equipment" in data:
        out["equipment"] = data["Equipment"]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    else:
        raise DeserializationError("CreateLabelRequest.client_token required")
    return out

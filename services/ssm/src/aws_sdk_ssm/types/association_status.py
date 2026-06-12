"""Generated from Smithy shape ``com.amazonaws.ssm#AssociationStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.association_status_name
    import aws_sdk_ssm.types.date_time
    import aws_sdk_ssm.types.status_additional_info
    import aws_sdk_ssm.types.status_message


class AssociationStatus(TypedDict):
    date: "aws_sdk_ssm.types.date_time.DateTime"
    """<p>The date when the status changed.</p>"""
    name: "aws_sdk_ssm.types.association_status_name.AssociationStatusName"
    """<p>The status.</p>"""
    message: "aws_sdk_ssm.types.status_message.StatusMessage"
    """<p>The reason for the status.</p>"""
    additional_info: NotRequired[
        "aws_sdk_ssm.types.status_additional_info.StatusAdditionalInfo"
    ]
    """<p>A user-defined string.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationStatus) -> dict:
    out: dict = {}
    import aws_sdk_ssm.types.date_time

    out["Date"] = aws_sdk_ssm.types.date_time.serialize_aws_json_1_1(value["date"])
    import aws_sdk_ssm.types.association_status_name

    out["Name"] = aws_sdk_ssm.types.association_status_name.serialize_aws_json_1_1(
        value["name"]
    )
    out["Message"] = value["message"]
    if "additional_info" in value:
        out["AdditionalInfo"] = value["additional_info"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociationStatus:
    out: AssociationStatus = {}  # type: ignore[typeddict-item]
    if "Date" in data:
        import aws_sdk_ssm.types.date_time

        out["date"] = aws_sdk_ssm.types.date_time.deserialize_aws_json_1_1(data["Date"])
    else:
        raise DeserializationError("AssociationStatus.date required")
    if "Name" in data:
        import aws_sdk_ssm.types.association_status_name

        out["name"] = (
            aws_sdk_ssm.types.association_status_name.deserialize_aws_json_1_1(
                data["Name"]
            )
        )
    else:
        raise DeserializationError("AssociationStatus.name required")
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("AssociationStatus.message required")
    if "AdditionalInfo" in data:
        out["additional_info"] = data["AdditionalInfo"]
    return out

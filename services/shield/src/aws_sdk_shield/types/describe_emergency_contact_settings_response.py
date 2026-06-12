"""Generated from Smithy shape ``com.amazonaws.shield#DescribeEmergencyContactSettingsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_shield.types.emergency_contact_list


class DescribeEmergencyContactSettingsResponse(TypedDict):
    emergency_contact_list: NotRequired[
        "aws_sdk_shield.types.emergency_contact_list.EmergencyContactList"
    ]
    """<p>A list of email addresses and phone numbers that the Shield Response Team (SRT) can use to contact you if you have proactive engagement enabled, for escalations to the SRT and to initiate proactive customer support.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEmergencyContactSettingsResponse) -> dict:
    out: dict = {}
    if "emergency_contact_list" in value:
        import aws_sdk_shield.types.emergency_contact_list

        out["EmergencyContactList"] = (
            aws_sdk_shield.types.emergency_contact_list.serialize_aws_json_1_1(
                value["emergency_contact_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEmergencyContactSettingsResponse:
    out: DescribeEmergencyContactSettingsResponse = {}  # type: ignore[typeddict-item]
    if "EmergencyContactList" in data:
        import aws_sdk_shield.types.emergency_contact_list

        out["emergency_contact_list"] = (
            aws_sdk_shield.types.emergency_contact_list.deserialize_aws_json_1_1(
                data["EmergencyContactList"]
            )
        )
    return out

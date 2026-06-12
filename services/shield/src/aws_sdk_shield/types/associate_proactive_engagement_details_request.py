"""Generated from Smithy shape ``com.amazonaws.shield#AssociateProactiveEngagementDetailsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_shield.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_shield.types.emergency_contact_list


class AssociateProactiveEngagementDetailsRequest(TypedDict):
    emergency_contact_list: (
        "aws_sdk_shield.types.emergency_contact_list.EmergencyContactList"
    )
    """<p>A list of email addresses and phone numbers that the Shield Response Team (SRT) can use to contact you for escalations to the SRT and to initiate proactive customer support. </p> <p>To enable proactive engagement, the contact list must include at least one phone number.</p> <note> <p>The contacts that you provide here replace any contacts that were already defined. If you already have contacts defined and want to use them, retrieve the list using <code>DescribeEmergencyContactSettings</code> and then provide it here. </p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateProactiveEngagementDetailsRequest) -> dict:
    out: dict = {}
    import aws_sdk_shield.types.emergency_contact_list

    out["EmergencyContactList"] = (
        aws_sdk_shield.types.emergency_contact_list.serialize_aws_json_1_1(
            value["emergency_contact_list"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateProactiveEngagementDetailsRequest:
    out: AssociateProactiveEngagementDetailsRequest = {}  # type: ignore[typeddict-item]
    if "EmergencyContactList" in data:
        import aws_sdk_shield.types.emergency_contact_list

        out["emergency_contact_list"] = (
            aws_sdk_shield.types.emergency_contact_list.deserialize_aws_json_1_1(
                data["EmergencyContactList"]
            )
        )
    else:
        raise DeserializationError(
            "AssociateProactiveEngagementDetailsRequest.emergency_contact_list required"
        )
    return out

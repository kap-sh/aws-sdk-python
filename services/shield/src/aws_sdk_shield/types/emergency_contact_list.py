"""Generated from Smithy shape ``com.amazonaws.shield#EmergencyContactList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_shield.types.emergency_contact

EmergencyContactList: TypeAlias = list[
    "aws_sdk_shield.types.emergency_contact.EmergencyContact"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EmergencyContactList) -> list:
    import aws_sdk_shield.types.emergency_contact

    out: list = []
    for item in value:
        out.append(aws_sdk_shield.types.emergency_contact.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EmergencyContactList:
    import aws_sdk_shield.types.emergency_contact

    out: EmergencyContactList = []
    for item in data:
        out.append(
            aws_sdk_shield.types.emergency_contact.deserialize_aws_json_1_1(item)
        )
    return out

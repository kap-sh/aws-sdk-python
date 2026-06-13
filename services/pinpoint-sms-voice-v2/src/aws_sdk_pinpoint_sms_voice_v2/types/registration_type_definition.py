"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RegistrationTypeDefinition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_type
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_type_display_hints
    import aws_sdk_pinpoint_sms_voice_v2.types.supported_association_list


class RegistrationTypeDefinition(TypedDict):
    registration_type: (
        "aws_sdk_pinpoint_sms_voice_v2.types.registration_type.RegistrationType"
    )
    """<p>The type of registration form. The list of <b>RegistrationTypes</b> can be found using the <a>DescribeRegistrationTypeDefinitions</a> action.</p>"""
    supported_associations: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.supported_association_list.SupportedAssociationList"
    ]
    """<p>The supported association behavior for the registration type.</p>"""
    display_hints: "aws_sdk_pinpoint_sms_voice_v2.types.registration_type_display_hints.RegistrationTypeDisplayHints"
    """<p>Provides help information on the registration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegistrationTypeDefinition) -> dict:
    out: dict = {}
    out["RegistrationType"] = value["registration_type"]
    if "supported_associations" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.supported_association_list

        out["SupportedAssociations"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.supported_association_list.serialize_aws_json_1_0(
                value["supported_associations"]
            )
        )
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_type_display_hints

    out["DisplayHints"] = (
        aws_sdk_pinpoint_sms_voice_v2.types.registration_type_display_hints.serialize_aws_json_1_0(
            value["display_hints"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> RegistrationTypeDefinition:
    out: RegistrationTypeDefinition = {}  # type: ignore[typeddict-item]
    if "RegistrationType" in data:
        out["registration_type"] = data["RegistrationType"]
    else:
        raise DeserializationError(
            "RegistrationTypeDefinition.registration_type required"
        )
    if "SupportedAssociations" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.supported_association_list

        out["supported_associations"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.supported_association_list.deserialize_aws_json_1_0(
                data["SupportedAssociations"]
            )
        )
    if "DisplayHints" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.registration_type_display_hints

        out["display_hints"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.registration_type_display_hints.deserialize_aws_json_1_0(
                data["DisplayHints"]
            )
        )
    else:
        raise DeserializationError("RegistrationTypeDefinition.display_hints required")
    return out

"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#SupportedAssociation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.iso_country_code
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_association_behavior
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_disassociation_behavior


class SupportedAssociation(TypedDict):
    resource_type: "str"
    """<p>Defines the behavior of when an origination identity and registration can be associated with each other.</p>"""
    iso_country_code: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.iso_country_code.IsoCountryCode"
    ]
    """<p>The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.</p>"""
    association_behavior: "aws_sdk_pinpoint_sms_voice_v2.types.registration_association_behavior.RegistrationAssociationBehavior"
    """<p>The association behavior.</p> <ul> <li> <p> <code>ASSOCIATE_BEFORE_SUBMIT</code> The origination identity has to be supplied when creating a registration.</p> </li> <li> <p> <code>ASSOCIATE_ON_APPROVAL</code> This applies to all sender ID registrations. The sender ID will be automatically provisioned once the registration is approved.</p> </li> <li> <p> <code>ASSOCIATE_AFTER_COMPLETE</code> This applies to phone number registrations when you must complete a registration first, then associate one or more phone numbers later. For example 10DLC campaigns and long codes. </p> </li> </ul>"""
    disassociation_behavior: "aws_sdk_pinpoint_sms_voice_v2.types.registration_disassociation_behavior.RegistrationDisassociationBehavior"
    """<p>The disassociation behavior.</p> <ul> <li> <p> <code>DISASSOCIATE_ALL_CLOSES_REGISTRATION</code> All origination identities must be disassociated from the registration before the registration can be closed.</p> </li> <li> <p> <code>DISASSOCIATE_ALL_ALLOWS_DELETE_REGISTRATION</code> All origination identities must be disassociated from the registration before the registration can be deleted.</p> </li> <li> <p> <code>DELETE_REGISTRATION_DISASSOCIATES</code> The registration can be deleted and all origination identities will be disasscoiated.</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SupportedAssociation) -> dict:
    out: dict = {}
    out["ResourceType"] = value["resource_type"]
    if "iso_country_code" in value:
        out["IsoCountryCode"] = value["iso_country_code"]
    out["AssociationBehavior"] = value["association_behavior"]
    out["DisassociationBehavior"] = value["disassociation_behavior"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SupportedAssociation:
    out: SupportedAssociation = {}  # type: ignore[typeddict-item]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    else:
        raise DeserializationError("SupportedAssociation.resource_type required")
    if "IsoCountryCode" in data:
        out["iso_country_code"] = data["IsoCountryCode"]
    if "AssociationBehavior" in data:
        out["association_behavior"] = data["AssociationBehavior"]
    else:
        raise DeserializationError("SupportedAssociation.association_behavior required")
    if "DisassociationBehavior" in data:
        out["disassociation_behavior"] = data["DisassociationBehavior"]
    else:
        raise DeserializationError(
            "SupportedAssociation.disassociation_behavior required"
        )
    return out

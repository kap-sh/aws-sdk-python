"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ListRegistrationAssociationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.next_token
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_association_metadata_list
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_type


class ListRegistrationAssociationsResult(TypedDict, closed=True):
    registration_arn: "str"
    """<p>The Amazon Resource Name (ARN) for the registration.</p>"""
    registration_id: "str"
    """<p>The unique identifier for the registration.</p>"""
    registration_type: (
        "aws_sdk_pinpoint_sms_voice_v2.types.registration_type.RegistrationType"
    )
    """<p>The type of registration form. The list of <b>RegistrationTypes</b> can be found using the <a>DescribeRegistrationTypeDefinitions</a> action.</p>"""
    registration_associations: "aws_sdk_pinpoint_sms_voice_v2.types.registration_association_metadata_list.RegistrationAssociationMetadataList"
    """<p>An array of RegistrationAssociationMetadata objects.</p>"""
    next_token: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRegistrationAssociationsResult) -> dict:
    out: dict = {}
    out["RegistrationArn"] = value["registration_arn"]
    out["RegistrationId"] = value["registration_id"]
    out["RegistrationType"] = value["registration_type"]
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_association_metadata_list

    out["RegistrationAssociations"] = (
        aws_sdk_pinpoint_sms_voice_v2.types.registration_association_metadata_list.serialize_aws_json_1_0(
            value["registration_associations"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRegistrationAssociationsResult:
    out: ListRegistrationAssociationsResult = {}  # type: ignore[typeddict-item]
    if "RegistrationArn" in data:
        out["registration_arn"] = data["RegistrationArn"]
    else:
        raise DeserializationError(
            "ListRegistrationAssociationsResult.registration_arn required"
        )
    if "RegistrationId" in data:
        out["registration_id"] = data["RegistrationId"]
    else:
        raise DeserializationError(
            "ListRegistrationAssociationsResult.registration_id required"
        )
    if "RegistrationType" in data:
        out["registration_type"] = data["RegistrationType"]
    else:
        raise DeserializationError(
            "ListRegistrationAssociationsResult.registration_type required"
        )
    if "RegistrationAssociations" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.registration_association_metadata_list

        out["registration_associations"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.registration_association_metadata_list.deserialize_aws_json_1_0(
                data["RegistrationAssociations"]
            )
        )
    else:
        raise DeserializationError(
            "ListRegistrationAssociationsResult.registration_associations required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

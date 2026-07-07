"""Generated from Smithy shape ``com.amazonaws.b2bi#CreateProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_b2bi.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.business_name
    import aws_sdk_b2bi.types.created_date
    import aws_sdk_b2bi.types.email
    import aws_sdk_b2bi.types.log_group_name
    import aws_sdk_b2bi.types.logging
    import aws_sdk_b2bi.types.phone
    import aws_sdk_b2bi.types.profile_id
    import aws_sdk_b2bi.types.profile_name
    import aws_sdk_b2bi.types.resource_arn


class CreateProfileResponse(TypedDict, closed=True):
    profile_id: "aws_sdk_b2bi.types.profile_id.ProfileId"
    """<p>Returns the unique, system-generated identifier for the profile.</p>"""
    profile_arn: "aws_sdk_b2bi.types.resource_arn.ResourceArn"
    """<p>Returns an Amazon Resource Name (ARN) for the profile.</p>"""
    name: "aws_sdk_b2bi.types.profile_name.ProfileName"
    """<p>Returns the name of the profile, used to identify it.</p>"""
    business_name: "aws_sdk_b2bi.types.business_name.BusinessName"
    """<p>Returns the name for the business associated with this profile.</p>"""
    phone: "aws_sdk_b2bi.types.phone.Phone"
    """<p>Returns the phone number associated with the profile.</p>"""
    email: NotRequired["aws_sdk_b2bi.types.email.Email"]
    """<p>Returns the email address associated with this customer profile.</p>"""
    logging: NotRequired["aws_sdk_b2bi.types.logging.Logging"]
    """<p>Returns whether or not logging is turned on for this profile.</p>"""
    log_group_name: NotRequired["aws_sdk_b2bi.types.log_group_name.LogGroupName"]
    """<p>Returns the name of the logging group.</p>"""
    created_at: "aws_sdk_b2bi.types.created_date.CreatedDate"
    """<p>Returns a timestamp representing the time the profile was created.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateProfileResponse) -> dict:
    out: dict = {}
    out["profileId"] = value["profile_id"]
    out["profileArn"] = value["profile_arn"]
    out["name"] = value["name"]
    out["businessName"] = value["business_name"]
    out["phone"] = value["phone"]
    if "email" in value:
        out["email"] = value["email"]
    if "logging" in value:
        import aws_sdk_b2bi.types.logging

        out["logging"] = aws_sdk_b2bi.types.logging.serialize_aws_json_1_0(
            value["logging"]
        )
    if "log_group_name" in value:
        out["logGroupName"] = value["log_group_name"]
    import aws_sdk_b2bi.types.created_date

    out["createdAt"] = aws_sdk_b2bi.types.created_date.serialize_aws_json_1_0(
        value["created_at"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateProfileResponse:
    out: CreateProfileResponse = {}  # type: ignore[typeddict-item]
    if "profileId" in data:
        out["profile_id"] = data["profileId"]
    else:
        raise DeserializationError("CreateProfileResponse.profile_id required")
    if "profileArn" in data:
        out["profile_arn"] = data["profileArn"]
    else:
        raise DeserializationError("CreateProfileResponse.profile_arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateProfileResponse.name required")
    if "businessName" in data:
        out["business_name"] = data["businessName"]
    else:
        raise DeserializationError("CreateProfileResponse.business_name required")
    if "phone" in data:
        out["phone"] = data["phone"]
    else:
        raise DeserializationError("CreateProfileResponse.phone required")
    if "email" in data:
        out["email"] = data["email"]
    if "logging" in data:
        import aws_sdk_b2bi.types.logging

        out["logging"] = aws_sdk_b2bi.types.logging.deserialize_aws_json_1_0(
            data["logging"]
        )
    if "logGroupName" in data:
        out["log_group_name"] = data["logGroupName"]
    if "createdAt" in data:
        import aws_sdk_b2bi.types.created_date

        out["created_at"] = aws_sdk_b2bi.types.created_date.deserialize_aws_json_1_0(
            data["createdAt"]
        )
    else:
        raise DeserializationError("CreateProfileResponse.created_at required")
    return out

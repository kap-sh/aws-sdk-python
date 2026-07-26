"""Generated from Smithy shape ``com.amazonaws.b2bi#UpdateProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_b2bi.errors import DeserializationError

if TYPE_CHECKING:
    import capo_b2bi.types.business_name
    import capo_b2bi.types.created_date
    import capo_b2bi.types.email
    import capo_b2bi.types.log_group_name
    import capo_b2bi.types.logging
    import capo_b2bi.types.modified_date
    import capo_b2bi.types.phone
    import capo_b2bi.types.profile_id
    import capo_b2bi.types.profile_name
    import capo_b2bi.types.resource_arn


class UpdateProfileResponse(TypedDict, closed=True):
    profile_id: "capo_b2bi.types.profile_id.ProfileId"
    """<p>Returns the unique, system-generated identifier for the profile.</p>"""
    profile_arn: "capo_b2bi.types.resource_arn.ResourceArn"
    """<p>Returns an Amazon Resource Name (ARN) for the profile.</p>"""
    name: "capo_b2bi.types.profile_name.ProfileName"
    """<p>Returns the name of the profile.</p>"""
    email: NotRequired["capo_b2bi.types.email.Email"]
    """<p>Returns the email address associated with this customer profile.</p>"""
    phone: "capo_b2bi.types.phone.Phone"
    """<p>Returns the phone number associated with the profile.</p>"""
    business_name: "capo_b2bi.types.business_name.BusinessName"
    """<p>Returns the name for the business associated with this profile.</p>"""
    logging: NotRequired["capo_b2bi.types.logging.Logging"]
    """<p>Specifies whether or not logging is enabled for this profile.</p>"""
    log_group_name: NotRequired["capo_b2bi.types.log_group_name.LogGroupName"]
    """<p>Returns the name of the logging group.</p>"""
    created_at: "capo_b2bi.types.created_date.CreatedDate"
    """<p>Returns a timestamp for creation date and time of the profile.</p>"""
    modified_at: NotRequired["capo_b2bi.types.modified_date.ModifiedDate"]
    """<p>Returns a timestamp for last time the profile was modified.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateProfileResponse) -> dict:
    out: dict = {}
    out["profileId"] = value["profile_id"]
    out["profileArn"] = value["profile_arn"]
    out["name"] = value["name"]
    if "email" in value:
        out["email"] = value["email"]
    out["phone"] = value["phone"]
    out["businessName"] = value["business_name"]
    if "logging" in value:
        import capo_b2bi.types.logging

        out["logging"] = capo_b2bi.types.logging.serialize_aws_json_1_0(
            value["logging"]
        )
    if "log_group_name" in value:
        out["logGroupName"] = value["log_group_name"]
    import capo_b2bi.types.created_date

    out["createdAt"] = capo_b2bi.types.created_date.serialize_aws_json_1_0(
        value["created_at"]
    )
    if "modified_at" in value:
        import capo_b2bi.types.modified_date

        out["modifiedAt"] = capo_b2bi.types.modified_date.serialize_aws_json_1_0(
            value["modified_at"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateProfileResponse:
    out: UpdateProfileResponse = {}  # type: ignore[typeddict-item]
    if "profileId" in data:
        out["profile_id"] = data["profileId"]
    else:
        raise DeserializationError("UpdateProfileResponse.profile_id required")
    if "profileArn" in data:
        out["profile_arn"] = data["profileArn"]
    else:
        raise DeserializationError("UpdateProfileResponse.profile_arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateProfileResponse.name required")
    if "email" in data:
        out["email"] = data["email"]
    if "phone" in data:
        out["phone"] = data["phone"]
    else:
        raise DeserializationError("UpdateProfileResponse.phone required")
    if "businessName" in data:
        out["business_name"] = data["businessName"]
    else:
        raise DeserializationError("UpdateProfileResponse.business_name required")
    if "logging" in data:
        import capo_b2bi.types.logging

        out["logging"] = capo_b2bi.types.logging.deserialize_aws_json_1_0(
            data["logging"]
        )
    if "logGroupName" in data:
        out["log_group_name"] = data["logGroupName"]
    if "createdAt" in data:
        import capo_b2bi.types.created_date

        out["created_at"] = capo_b2bi.types.created_date.deserialize_aws_json_1_0(
            data["createdAt"]
        )
    else:
        raise DeserializationError("UpdateProfileResponse.created_at required")
    if "modifiedAt" in data:
        import capo_b2bi.types.modified_date

        out["modified_at"] = capo_b2bi.types.modified_date.deserialize_aws_json_1_0(
            data["modifiedAt"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.b2bi#ProfileSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_b2bi.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.business_name
    import aws_sdk_b2bi.types.created_date
    import aws_sdk_b2bi.types.log_group_name
    import aws_sdk_b2bi.types.logging
    import aws_sdk_b2bi.types.modified_date
    import aws_sdk_b2bi.types.profile_id
    import aws_sdk_b2bi.types.profile_name


class ProfileSummary(TypedDict):
    profile_id: "aws_sdk_b2bi.types.profile_id.ProfileId"
    """<p>Returns the unique, system-generated identifier for the profile.</p>"""
    name: "aws_sdk_b2bi.types.profile_name.ProfileName"
    """<p>Returns the display name for profile.</p>"""
    business_name: "aws_sdk_b2bi.types.business_name.BusinessName"
    """<p>Returns the name for the business associated with this profile.</p>"""
    logging: NotRequired["aws_sdk_b2bi.types.logging.Logging"]
    """<p>Specifies whether or not logging is enabled for this profile.</p>"""
    log_group_name: NotRequired["aws_sdk_b2bi.types.log_group_name.LogGroupName"]
    """<p>Returns the name of the logging group.</p>"""
    created_at: "aws_sdk_b2bi.types.created_date.CreatedDate"
    """<p>Returns the timestamp for creation date and time of the profile.</p>"""
    modified_at: NotRequired["aws_sdk_b2bi.types.modified_date.ModifiedDate"]
    """<p>Returns the timestamp that identifies the most recent date and time that the profile was modified.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProfileSummary) -> dict:
    out: dict = {}
    out["profileId"] = value["profile_id"]
    out["name"] = value["name"]
    out["businessName"] = value["business_name"]
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
    if "modified_at" in value:
        import aws_sdk_b2bi.types.modified_date

        out["modifiedAt"] = aws_sdk_b2bi.types.modified_date.serialize_aws_json_1_0(
            value["modified_at"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ProfileSummary:
    out: ProfileSummary = {}  # type: ignore[typeddict-item]
    if "profileId" in data:
        out["profile_id"] = data["profileId"]
    else:
        raise DeserializationError("ProfileSummary.profile_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ProfileSummary.name required")
    if "businessName" in data:
        out["business_name"] = data["businessName"]
    else:
        raise DeserializationError("ProfileSummary.business_name required")
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
        raise DeserializationError("ProfileSummary.created_at required")
    if "modifiedAt" in data:
        import aws_sdk_b2bi.types.modified_date

        out["modified_at"] = aws_sdk_b2bi.types.modified_date.deserialize_aws_json_1_0(
            data["modifiedAt"]
        )
    return out

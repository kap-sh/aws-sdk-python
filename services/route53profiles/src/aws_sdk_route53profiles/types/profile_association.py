"""Generated from Smithy shape ``com.amazonaws.route53profiles#ProfileAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53profiles.types.account_id
    import aws_sdk_route53profiles.types.name
    import aws_sdk_route53profiles.types.profile_status
    import aws_sdk_route53profiles.types.resource_id
    import aws_sdk_route53profiles.types.rfc3339_timestamp
    import aws_sdk_route53profiles.types.string


class ProfileAssociation(TypedDict, closed=True):
    id: NotRequired["aws_sdk_route53profiles.types.resource_id.ResourceId"]
    """<p> ID of the Profile association. </p>"""
    name: NotRequired["aws_sdk_route53profiles.types.name.Name"]
    """<p> Name of the Profile association. </p>"""
    owner_id: NotRequired["aws_sdk_route53profiles.types.account_id.AccountId"]
    """<p> Amazon Web Services account ID of the Profile association owner. </p>"""
    profile_id: NotRequired["aws_sdk_route53profiles.types.resource_id.ResourceId"]
    """<p> ID of the Profile. </p>"""
    resource_id: NotRequired["aws_sdk_route53profiles.types.resource_id.ResourceId"]
    """<p> The Amazon Resource Name (ARN) of the VPC. </p>"""
    status: NotRequired["aws_sdk_route53profiles.types.profile_status.ProfileStatus"]
    """<p> Status of the Profile association. </p>"""
    status_message: NotRequired["aws_sdk_route53profiles.types.string.String"]
    """<p> Additional information about the Profile association. </p>"""
    creation_time: NotRequired[
        "aws_sdk_route53profiles.types.rfc3339_timestamp.Rfc3339Timestamp"
    ]
    """<p> The date and time that the Profile association was created, in Unix time format and Coordinated Universal Time (UTC). </p>"""
    modification_time: NotRequired[
        "aws_sdk_route53profiles.types.rfc3339_timestamp.Rfc3339Timestamp"
    ]
    """<p> The date and time that the Profile association was modified, in Unix time format and Coordinated Universal Time (UTC). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProfileAssociation) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "owner_id" in value:
        out["OwnerId"] = value["owner_id"]
    if "profile_id" in value:
        out["ProfileId"] = value["profile_id"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "status" in value:
        import aws_sdk_route53profiles.types.profile_status

        out["Status"] = aws_sdk_route53profiles.types.profile_status.serialize_json(
            value["status"]
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "creation_time" in value:
        import aws_sdk_route53profiles.types.rfc3339_timestamp

        out["CreationTime"] = (
            aws_sdk_route53profiles.types.rfc3339_timestamp.serialize_json(
                value["creation_time"]
            )
        )
    if "modification_time" in value:
        import aws_sdk_route53profiles.types.rfc3339_timestamp

        out["ModificationTime"] = (
            aws_sdk_route53profiles.types.rfc3339_timestamp.serialize_json(
                value["modification_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> ProfileAssociation:
    out: ProfileAssociation = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "OwnerId" in data:
        out["owner_id"] = data["OwnerId"]
    if "ProfileId" in data:
        out["profile_id"] = data["ProfileId"]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "Status" in data:
        import aws_sdk_route53profiles.types.profile_status

        out["status"] = aws_sdk_route53profiles.types.profile_status.deserialize_json(
            data["Status"]
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "CreationTime" in data:
        import aws_sdk_route53profiles.types.rfc3339_timestamp

        out["creation_time"] = (
            aws_sdk_route53profiles.types.rfc3339_timestamp.deserialize_json(
                data["CreationTime"]
            )
        )
    if "ModificationTime" in data:
        import aws_sdk_route53profiles.types.rfc3339_timestamp

        out["modification_time"] = (
            aws_sdk_route53profiles.types.rfc3339_timestamp.deserialize_json(
                data["ModificationTime"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.route53profiles#Profile``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53profiles.types.account_id
    import aws_sdk_route53profiles.types.arn
    import aws_sdk_route53profiles.types.creator_request_id
    import aws_sdk_route53profiles.types.name
    import aws_sdk_route53profiles.types.profile_status
    import aws_sdk_route53profiles.types.resource_id
    import aws_sdk_route53profiles.types.rfc3339_timestamp
    import aws_sdk_route53profiles.types.share_status
    import aws_sdk_route53profiles.types.string


class Profile(TypedDict, closed=True):
    id: NotRequired["aws_sdk_route53profiles.types.resource_id.ResourceId"]
    """<p> ID of the Profile. </p>"""
    arn: NotRequired["aws_sdk_route53profiles.types.arn.Arn"]
    """<p> The Amazon Resource Name (ARN) of the Profile. </p>"""
    name: NotRequired["aws_sdk_route53profiles.types.name.Name"]
    """<p> Name of the Profile. </p>"""
    owner_id: NotRequired["aws_sdk_route53profiles.types.account_id.AccountId"]
    """<p> Amazon Web Services account ID of the Profile owner. </p>"""
    status: NotRequired["aws_sdk_route53profiles.types.profile_status.ProfileStatus"]
    """<p> The status for the Profile. </p>"""
    status_message: NotRequired["aws_sdk_route53profiles.types.string.String"]
    """<p> Status message that includes additiona information about the Profile. </p>"""
    share_status: NotRequired["aws_sdk_route53profiles.types.share_status.ShareStatus"]
    """<p> Sharing status for the Profile. </p>"""
    creation_time: NotRequired[
        "aws_sdk_route53profiles.types.rfc3339_timestamp.Rfc3339Timestamp"
    ]
    """<p> The date and time that the Profile was created, in Unix time format and Coordinated Universal Time (UTC). </p>"""
    modification_time: NotRequired[
        "aws_sdk_route53profiles.types.rfc3339_timestamp.Rfc3339Timestamp"
    ]
    """<p> The date and time that the Profile was modified, in Unix time format and Coordinated Universal Time (UTC). </p>"""
    client_token: NotRequired[
        "aws_sdk_route53profiles.types.creator_request_id.CreatorRequestId"
    ]
    """<p> The <code>ClientToken</code> value that was assigned when the Profile was created. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Profile) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "owner_id" in value:
        out["OwnerId"] = value["owner_id"]
    if "status" in value:
        import aws_sdk_route53profiles.types.profile_status

        out["Status"] = aws_sdk_route53profiles.types.profile_status.serialize_json(
            value["status"]
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "share_status" in value:
        import aws_sdk_route53profiles.types.share_status

        out["ShareStatus"] = aws_sdk_route53profiles.types.share_status.serialize_json(
            value["share_status"]
        )
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
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> Profile:
    out: Profile = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "OwnerId" in data:
        out["owner_id"] = data["OwnerId"]
    if "Status" in data:
        import aws_sdk_route53profiles.types.profile_status

        out["status"] = aws_sdk_route53profiles.types.profile_status.deserialize_json(
            data["Status"]
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "ShareStatus" in data:
        import aws_sdk_route53profiles.types.share_status

        out["share_status"] = (
            aws_sdk_route53profiles.types.share_status.deserialize_json(
                data["ShareStatus"]
            )
        )
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
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out

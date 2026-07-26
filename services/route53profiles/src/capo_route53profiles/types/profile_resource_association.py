"""Generated from Smithy shape ``com.amazonaws.route53profiles#ProfileResourceAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53profiles.types.account_id
    import capo_route53profiles.types.arn
    import capo_route53profiles.types.name
    import capo_route53profiles.types.profile_status
    import capo_route53profiles.types.resource_id
    import capo_route53profiles.types.resource_properties
    import capo_route53profiles.types.rfc3339_timestamp
    import capo_route53profiles.types.string


class ProfileResourceAssociation(TypedDict, closed=True):
    id: NotRequired["capo_route53profiles.types.resource_id.ResourceId"]
    """<p> ID of the Profile resource association. </p>"""
    name: NotRequired["capo_route53profiles.types.name.Name"]
    """<p> Name of the Profile resource association. </p>"""
    owner_id: NotRequired["capo_route53profiles.types.account_id.AccountId"]
    """<p> Amazon Web Services account ID of the Profile resource association owner. </p>"""
    profile_id: NotRequired["capo_route53profiles.types.resource_id.ResourceId"]
    """<p> Profile ID of the Profile that the resources are associated with. </p>"""
    resource_arn: NotRequired["capo_route53profiles.types.arn.Arn"]
    """<p> The Amazon Resource Name (ARN) of the resource association. </p>"""
    resource_type: NotRequired["capo_route53profiles.types.string.String"]
    """<p> Resource type, such as a private hosted zone, or DNS Firewall rule group. </p>"""
    resource_properties: NotRequired[
        "capo_route53profiles.types.resource_properties.ResourceProperties"
    ]
    """<p> If the DNS resource is a DNS Firewall rule group, this indicates the priority. </p>"""
    status: NotRequired["capo_route53profiles.types.profile_status.ProfileStatus"]
    """<p> Status of the Profile resource association. </p>"""
    status_message: NotRequired["capo_route53profiles.types.string.String"]
    """<p> Additional information about the Profile resource association. </p>"""
    creation_time: NotRequired[
        "capo_route53profiles.types.rfc3339_timestamp.Rfc3339Timestamp"
    ]
    """<p> The date and time that the Profile resource association was created, in Unix time format and Coordinated Universal Time (UTC). </p>"""
    modification_time: NotRequired[
        "capo_route53profiles.types.rfc3339_timestamp.Rfc3339Timestamp"
    ]
    """<p> The date and time that the Profile resource association was modified, in Unix time format and Coordinated Universal Time (UTC). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProfileResourceAssociation) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "owner_id" in value:
        out["OwnerId"] = value["owner_id"]
    if "profile_id" in value:
        out["ProfileId"] = value["profile_id"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "resource_properties" in value:
        out["ResourceProperties"] = value["resource_properties"]
    if "status" in value:
        import capo_route53profiles.types.profile_status

        out["Status"] = capo_route53profiles.types.profile_status.serialize_json(
            value["status"]
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "creation_time" in value:
        import capo_route53profiles.types.rfc3339_timestamp

        out["CreationTime"] = (
            capo_route53profiles.types.rfc3339_timestamp.serialize_json(
                value["creation_time"]
            )
        )
    if "modification_time" in value:
        import capo_route53profiles.types.rfc3339_timestamp

        out["ModificationTime"] = (
            capo_route53profiles.types.rfc3339_timestamp.serialize_json(
                value["modification_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> ProfileResourceAssociation:
    out: ProfileResourceAssociation = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "OwnerId" in data:
        out["owner_id"] = data["OwnerId"]
    if "ProfileId" in data:
        out["profile_id"] = data["ProfileId"]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    if "ResourceProperties" in data:
        out["resource_properties"] = data["ResourceProperties"]
    if "Status" in data:
        import capo_route53profiles.types.profile_status

        out["status"] = capo_route53profiles.types.profile_status.deserialize_json(
            data["Status"]
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "CreationTime" in data:
        import capo_route53profiles.types.rfc3339_timestamp

        out["creation_time"] = (
            capo_route53profiles.types.rfc3339_timestamp.deserialize_json(
                data["CreationTime"]
            )
        )
    if "ModificationTime" in data:
        import capo_route53profiles.types.rfc3339_timestamp

        out["modification_time"] = (
            capo_route53profiles.types.rfc3339_timestamp.deserialize_json(
                data["ModificationTime"]
            )
        )
    return out

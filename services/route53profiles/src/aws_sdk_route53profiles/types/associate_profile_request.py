"""Generated from Smithy shape ``com.amazonaws.route53profiles#AssociateProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_route53profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53profiles.types.name
    import aws_sdk_route53profiles.types.resource_id
    import aws_sdk_route53profiles.types.tag_list


class AssociateProfileRequest(TypedDict, closed=True):
    profile_id: "aws_sdk_route53profiles.types.resource_id.ResourceId"
    """<p> ID of the Profile. </p>"""
    resource_id: "aws_sdk_route53profiles.types.resource_id.ResourceId"
    """<p> The ID of the VPC. </p>"""
    name: "aws_sdk_route53profiles.types.name.Name"
    """<p> A name for the association. </p>"""
    tags: NotRequired["aws_sdk_route53profiles.types.tag_list.TagList"]
    """<p> A list of the tag keys and values that you want to identify the Profile association. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateProfileRequest) -> dict:
    out: dict = {}
    out["ProfileId"] = value["profile_id"]
    out["ResourceId"] = value["resource_id"]
    out["Name"] = value["name"]
    if "tags" in value:
        import aws_sdk_route53profiles.types.tag_list

        out["Tags"] = aws_sdk_route53profiles.types.tag_list.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> AssociateProfileRequest:
    out: AssociateProfileRequest = {}  # type: ignore[typeddict-item]
    if "ProfileId" in data:
        out["profile_id"] = data["ProfileId"]
    else:
        raise DeserializationError("AssociateProfileRequest.profile_id required")
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError("AssociateProfileRequest.resource_id required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("AssociateProfileRequest.name required")
    if "Tags" in data:
        import aws_sdk_route53profiles.types.tag_list

        out["tags"] = aws_sdk_route53profiles.types.tag_list.deserialize_json(
            data["Tags"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.route53profiles#ProfileSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53profiles.types.arn
    import aws_sdk_route53profiles.types.name
    import aws_sdk_route53profiles.types.resource_id
    import aws_sdk_route53profiles.types.share_status


class ProfileSummary(TypedDict):
    id: NotRequired["aws_sdk_route53profiles.types.resource_id.ResourceId"]
    """<p> ID of the Profile. </p>"""
    arn: NotRequired["aws_sdk_route53profiles.types.arn.Arn"]
    """<p> The Amazon Resource Name (ARN) of the Profile. </p>"""
    name: NotRequired["aws_sdk_route53profiles.types.name.Name"]
    """<p> Name of the Profile. </p>"""
    share_status: NotRequired["aws_sdk_route53profiles.types.share_status.ShareStatus"]
    """<p> Share status of the Profile. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProfileSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "share_status" in value:
        import aws_sdk_route53profiles.types.share_status

        out["ShareStatus"] = aws_sdk_route53profiles.types.share_status.serialize_json(
            value["share_status"]
        )
    return out


def deserialize_json(data: dict) -> ProfileSummary:
    out: ProfileSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ShareStatus" in data:
        import aws_sdk_route53profiles.types.share_status

        out["share_status"] = (
            aws_sdk_route53profiles.types.share_status.deserialize_json(
                data["ShareStatus"]
            )
        )
    return out

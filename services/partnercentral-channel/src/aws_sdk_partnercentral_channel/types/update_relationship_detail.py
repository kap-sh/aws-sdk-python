"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#UpdateRelationshipDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_partnercentral_channel.types.arn
    import aws_sdk_partnercentral_channel.types.relationship_display_name
    import aws_sdk_partnercentral_channel.types.relationship_id
    import aws_sdk_partnercentral_channel.types.revision


class UpdateRelationshipDetail(TypedDict):
    arn: NotRequired["aws_sdk_partnercentral_channel.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the updated relationship.</p>"""
    id: NotRequired[
        "aws_sdk_partnercentral_channel.types.relationship_id.RelationshipId"
    ]
    """<p>The unique identifier of the updated relationship.</p>"""
    revision: NotRequired["aws_sdk_partnercentral_channel.types.revision.Revision"]
    """<p>The new revision number of the relationship.</p>"""
    display_name: NotRequired[
        "aws_sdk_partnercentral_channel.types.relationship_display_name.RelationshipDisplayName"
    ]
    """<p>The updated display name of the relationship.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateRelationshipDetail) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "id" in value:
        out["id"] = value["id"]
    if "revision" in value:
        out["revision"] = value["revision"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateRelationshipDetail:
    out: UpdateRelationshipDetail = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "id" in data:
        out["id"] = data["id"]
    if "revision" in data:
        out["revision"] = data["revision"]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    return out

"""Generated from Smithy shape ``com.amazonaws.wellarchitected#Lens``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.lens_arn
    import aws_sdk_wellarchitected.types.lens_description
    import aws_sdk_wellarchitected.types.lens_name
    import aws_sdk_wellarchitected.types.lens_owner
    import aws_sdk_wellarchitected.types.lens_version
    import aws_sdk_wellarchitected.types.share_invitation_id
    import aws_sdk_wellarchitected.types.tag_map


class Lens(TypedDict, closed=True):
    lens_arn: NotRequired["aws_sdk_wellarchitected.types.lens_arn.LensArn"]
    """<p>The ARN of a lens.</p>"""
    lens_version: NotRequired["aws_sdk_wellarchitected.types.lens_version.LensVersion"]
    """<p>The version of a lens.</p>"""
    name: NotRequired["aws_sdk_wellarchitected.types.lens_name.LensName"]
    description: NotRequired[
        "aws_sdk_wellarchitected.types.lens_description.LensDescription"
    ]
    owner: NotRequired["aws_sdk_wellarchitected.types.lens_owner.LensOwner"]
    """<p>The Amazon Web Services account ID that owns the lens.</p>"""
    share_invitation_id: NotRequired[
        "aws_sdk_wellarchitected.types.share_invitation_id.ShareInvitationId"
    ]
    """<p>The ID assigned to the share invitation.</p>"""
    tags: NotRequired["aws_sdk_wellarchitected.types.tag_map.TagMap"]
    """<p>The tags assigned to the lens.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Lens) -> dict:
    out: dict = {}
    if "lens_arn" in value:
        out["LensArn"] = value["lens_arn"]
    if "lens_version" in value:
        out["LensVersion"] = value["lens_version"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "share_invitation_id" in value:
        out["ShareInvitationId"] = value["share_invitation_id"]
    if "tags" in value:
        import aws_sdk_wellarchitected.types.tag_map

        out["Tags"] = aws_sdk_wellarchitected.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> Lens:
    out: Lens = {}  # type: ignore[typeddict-item]
    if "LensArn" in data:
        out["lens_arn"] = data["LensArn"]
    if "LensVersion" in data:
        out["lens_version"] = data["LensVersion"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Owner" in data:
        out["owner"] = data["Owner"]
    if "ShareInvitationId" in data:
        out["share_invitation_id"] = data["ShareInvitationId"]
    if "Tags" in data:
        import aws_sdk_wellarchitected.types.tag_map

        out["tags"] = aws_sdk_wellarchitected.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out

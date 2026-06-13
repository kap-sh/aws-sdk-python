"""Generated from Smithy shape ``com.amazonaws.repostspace#SendInvitesInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_repostspace.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_repostspace.types.accessor_id_list
    import aws_sdk_repostspace.types.invite_body
    import aws_sdk_repostspace.types.invite_title
    import aws_sdk_repostspace.types.space_id


class SendInvitesInput(TypedDict):
    space_id: "aws_sdk_repostspace.types.space_id.SpaceId"
    """<p>The ID of the private re:Post.</p>"""
    accessor_ids: "aws_sdk_repostspace.types.accessor_id_list.AccessorIdList"
    """<p>The array of identifiers for the users and groups.</p>"""
    title: "aws_sdk_repostspace.types.invite_title.InviteTitle"
    """<p>The title of the invite.</p>"""
    body: "aws_sdk_repostspace.types.invite_body.InviteBody"
    """<p>The body of the invite.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendInvitesInput) -> dict:
    out: dict = {}
    import aws_sdk_repostspace.types.accessor_id_list

    out["accessorIds"] = aws_sdk_repostspace.types.accessor_id_list.serialize_json(
        value["accessor_ids"]
    )
    out["title"] = value["title"]
    out["body"] = value["body"]
    return out


def deserialize_json(data: dict) -> SendInvitesInput:
    out: SendInvitesInput = {}  # type: ignore[typeddict-item]
    if "accessorIds" in data:
        import aws_sdk_repostspace.types.accessor_id_list

        out["accessor_ids"] = (
            aws_sdk_repostspace.types.accessor_id_list.deserialize_json(
                data["accessorIds"]
            )
        )
    else:
        raise DeserializationError("SendInvitesInput.accessor_ids required")
    if "title" in data:
        out["title"] = data["title"]
    else:
        raise DeserializationError("SendInvitesInput.title required")
    if "body" in data:
        out["body"] = data["body"]
    else:
        raise DeserializationError("SendInvitesInput.body required")
    return out

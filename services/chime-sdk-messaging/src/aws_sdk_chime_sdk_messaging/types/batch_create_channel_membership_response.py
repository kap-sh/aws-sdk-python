"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#BatchCreateChannelMembershipResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.batch_channel_memberships
    import aws_sdk_chime_sdk_messaging.types.batch_create_channel_membership_errors


class BatchCreateChannelMembershipResponse(TypedDict):
    batch_channel_memberships: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.batch_channel_memberships.BatchChannelMemberships"
    ]
    """<p>The list of channel memberships in the response.</p>"""
    errors: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.batch_create_channel_membership_errors.BatchCreateChannelMembershipErrors"
    ]
    """<p>If the action fails for one or more of the memberships in the request, a list of the memberships is returned, along with error codes and error messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateChannelMembershipResponse) -> dict:
    out: dict = {}
    if "batch_channel_memberships" in value:
        import aws_sdk_chime_sdk_messaging.types.batch_channel_memberships

        out["BatchChannelMemberships"] = (
            aws_sdk_chime_sdk_messaging.types.batch_channel_memberships.serialize_json(
                value["batch_channel_memberships"]
            )
        )
    if "errors" in value:
        import aws_sdk_chime_sdk_messaging.types.batch_create_channel_membership_errors

        out["Errors"] = (
            aws_sdk_chime_sdk_messaging.types.batch_create_channel_membership_errors.serialize_json(
                value["errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchCreateChannelMembershipResponse:
    out: BatchCreateChannelMembershipResponse = {}  # type: ignore[typeddict-item]
    if "BatchChannelMemberships" in data:
        import aws_sdk_chime_sdk_messaging.types.batch_channel_memberships

        out["batch_channel_memberships"] = (
            aws_sdk_chime_sdk_messaging.types.batch_channel_memberships.deserialize_json(
                data["BatchChannelMemberships"]
            )
        )
    if "Errors" in data:
        import aws_sdk_chime_sdk_messaging.types.batch_create_channel_membership_errors

        out["errors"] = (
            aws_sdk_chime_sdk_messaging.types.batch_create_channel_membership_errors.deserialize_json(
                data["Errors"]
            )
        )
    return out

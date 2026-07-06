"""Generated from Smithy shape ``com.amazonaws.wellarchitected#DeleteProfileShareInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.client_request_token
    import aws_sdk_wellarchitected.types.profile_arn
    import aws_sdk_wellarchitected.types.share_id


class DeleteProfileShareInput(TypedDict, closed=True):
    share_id: "aws_sdk_wellarchitected.types.share_id.ShareId"
    profile_arn: "aws_sdk_wellarchitected.types.profile_arn.ProfileArn"
    """<p>The profile ARN.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_wellarchitected.types.client_request_token.ClientRequestToken"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteProfileShareInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteProfileShareInput:
    out: DeleteProfileShareInput = {}  # type: ignore[typeddict-item]
    return out

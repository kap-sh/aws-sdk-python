"""Generated from Smithy shape ``com.amazonaws.wellarchitected#DeleteProfileShareInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.client_request_token
    import capo_wellarchitected.types.profile_arn
    import capo_wellarchitected.types.share_id


class DeleteProfileShareInput(TypedDict, closed=True):
    share_id: "capo_wellarchitected.types.share_id.ShareId"
    profile_arn: "capo_wellarchitected.types.profile_arn.ProfileArn"
    """<p>The profile ARN.</p>"""
    client_request_token: NotRequired[
        "capo_wellarchitected.types.client_request_token.ClientRequestToken"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteProfileShareInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteProfileShareInput:
    out: DeleteProfileShareInput = {}  # type: ignore[typeddict-item]
    return out

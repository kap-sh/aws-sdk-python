"""Generated from Smithy shape ``com.amazonaws.wellarchitected#DeleteProfileInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.client_request_token
    import capo_wellarchitected.types.profile_arn


class DeleteProfileInput(TypedDict, closed=True):
    profile_arn: "capo_wellarchitected.types.profile_arn.ProfileArn"
    """<p>The profile ARN.</p>"""
    client_request_token: NotRequired[
        "capo_wellarchitected.types.client_request_token.ClientRequestToken"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteProfileInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteProfileInput:
    out: DeleteProfileInput = {}  # type: ignore[typeddict-item]
    return out

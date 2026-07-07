"""Generated from Smithy shape ``com.amazonaws.wellarchitected#DeleteProfileInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.client_request_token
    import aws_sdk_wellarchitected.types.profile_arn


class DeleteProfileInput(TypedDict, closed=True):
    profile_arn: "aws_sdk_wellarchitected.types.profile_arn.ProfileArn"
    """<p>The profile ARN.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_wellarchitected.types.client_request_token.ClientRequestToken"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteProfileInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteProfileInput:
    out: DeleteProfileInput = {}  # type: ignore[typeddict-item]
    return out

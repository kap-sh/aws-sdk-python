"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#DeleteAppInstanceUserRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.chime_arn


class DeleteAppInstanceUserRequest(TypedDict):
    app_instance_user_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn"
    """<p>The ARN of the user request being deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAppInstanceUserRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAppInstanceUserRequest:
    out: DeleteAppInstanceUserRequest = {}  # type: ignore[typeddict-item]
    return out

"""Generated from Smithy shape ``com.amazonaws.securityhub#DeleteActionTargetRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class DeleteActionTargetRequest(TypedDict):
    action_target_arn: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Resource Name (ARN) of the custom action target to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteActionTargetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteActionTargetRequest:
    out: DeleteActionTargetRequest = {}  # type: ignore[typeddict-item]
    return out

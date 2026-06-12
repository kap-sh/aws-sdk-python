"""Generated from Smithy shape ``com.amazonaws.securityhub#DeleteConfigurationPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class DeleteConfigurationPolicyRequest(TypedDict):
    identifier: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    """<p> The Amazon Resource Name (ARN) or universally unique identifier (UUID) of the configuration policy. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConfigurationPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteConfigurationPolicyRequest:
    out: DeleteConfigurationPolicyRequest = {}  # type: ignore[typeddict-item]
    return out

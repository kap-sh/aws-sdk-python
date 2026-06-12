"""Generated from Smithy shape ``com.amazonaws.securityhub#GetConfigurationPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class GetConfigurationPolicyRequest(TypedDict):
    identifier: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    """<p> The Amazon Resource Name (ARN) or universally unique identifier (UUID) of the configuration policy. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfigurationPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetConfigurationPolicyRequest:
    out: GetConfigurationPolicyRequest = {}  # type: ignore[typeddict-item]
    return out

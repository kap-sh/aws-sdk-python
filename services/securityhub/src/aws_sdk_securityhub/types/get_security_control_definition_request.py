"""Generated from Smithy shape ``com.amazonaws.securityhub#GetSecurityControlDefinitionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class GetSecurityControlDefinitionRequest(TypedDict):
    security_control_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The ID of the security control to retrieve the definition for. This field doesn’t accept an Amazon Resource Name (ARN). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSecurityControlDefinitionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSecurityControlDefinitionRequest:
    out: GetSecurityControlDefinitionRequest = {}  # type: ignore[typeddict-item]
    return out

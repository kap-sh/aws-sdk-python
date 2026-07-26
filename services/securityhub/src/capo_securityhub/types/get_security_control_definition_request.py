"""Generated from Smithy shape ``com.amazonaws.securityhub#GetSecurityControlDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class GetSecurityControlDefinitionRequest(TypedDict, closed=True):
    security_control_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The ID of the security control to retrieve the definition for. This field doesn’t accept an Amazon Resource Name (ARN). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSecurityControlDefinitionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSecurityControlDefinitionRequest:
    out: GetSecurityControlDefinitionRequest = {}  # type: ignore[typeddict-item]
    return out

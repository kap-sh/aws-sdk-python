"""Generated from Smithy shape ``com.amazonaws.appintegrations#GetApplicationRequest``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.arn_or_uuid

class GetApplicationRequest(TypedDict):
    arn: "aws_sdk_appintegrations.types.arn_or_uuid.ArnOrUUID"
    """<p>The Amazon Resource Name (ARN) of the Application.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GetApplicationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetApplicationRequest:
    out: GetApplicationRequest = {}  # type: ignore[typeddict-item]
    return out
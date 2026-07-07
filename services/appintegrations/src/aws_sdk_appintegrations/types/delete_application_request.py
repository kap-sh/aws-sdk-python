"""Generated from Smithy shape ``com.amazonaws.appintegrations#DeleteApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.arn_or_uuid


class DeleteApplicationRequest(TypedDict, closed=True):
    arn: "aws_sdk_appintegrations.types.arn_or_uuid.ArnOrUUID"
    """<p>The Amazon Resource Name (ARN) of the Application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteApplicationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteApplicationRequest:
    out: DeleteApplicationRequest = {}  # type: ignore[typeddict-item]
    return out

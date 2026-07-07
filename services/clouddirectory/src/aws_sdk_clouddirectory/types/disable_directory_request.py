"""Generated from Smithy shape ``com.amazonaws.clouddirectory#DisableDirectoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arn


class DisableDirectoryRequest(TypedDict, closed=True):
    directory_arn: "aws_sdk_clouddirectory.types.arn.Arn"
    """<p>The ARN of the directory to disable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisableDirectoryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisableDirectoryRequest:
    out: DisableDirectoryRequest = {}  # type: ignore[typeddict-item]
    return out

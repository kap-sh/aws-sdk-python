"""Generated from Smithy shape ``com.amazonaws.clouddirectory#EnableDirectoryRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arn


class EnableDirectoryRequest(TypedDict):
    directory_arn: "aws_sdk_clouddirectory.types.arn.Arn"
    """<p>The ARN of the directory to enable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnableDirectoryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> EnableDirectoryRequest:
    out: EnableDirectoryRequest = {}  # type: ignore[typeddict-item]
    return out

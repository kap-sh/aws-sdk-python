"""Generated from Smithy shape ``com.amazonaws.macie2#GetResourceProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__string


class GetResourceProfileRequest(TypedDict, closed=True):
    resource_arn: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the S3 bucket that the request applies to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourceProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetResourceProfileRequest:
    out: GetResourceProfileRequest = {}  # type: ignore[typeddict-item]
    return out

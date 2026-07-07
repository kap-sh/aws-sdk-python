"""Generated from Smithy shape ``com.amazonaws.macie2#ListResourceProfileArtifactsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string


class ListResourceProfileArtifactsRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The nextToken string that specifies which page of results to return in a paginated response.</p>"""
    resource_arn: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the S3 bucket that the request applies to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResourceProfileArtifactsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListResourceProfileArtifactsRequest:
    out: ListResourceProfileArtifactsRequest = {}  # type: ignore[typeddict-item]
    return out

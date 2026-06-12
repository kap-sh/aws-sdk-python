"""Generated from Smithy shape ``com.amazonaws.amplifybackend#ListS3BucketsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.__string


class ListS3BucketsRequest(TypedDict):
    next_token: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>Reserved for future use.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListS3BucketsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListS3BucketsRequest:
    out: ListS3BucketsRequest = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out

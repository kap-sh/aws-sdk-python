"""Generated from Smithy shape ``com.amazonaws.codecatalyst#GetSourceRepositoryCloneUrlsResponse``."""

from typing import TypedDict

from aws_sdk_codecatalyst.errors import DeserializationError


class GetSourceRepositoryCloneUrlsResponse(TypedDict):
    https: "str"
    """<p>The HTTPS URL to use when cloning the source repository.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSourceRepositoryCloneUrlsResponse) -> dict:
    out: dict = {}
    out["https"] = value["https"]
    return out


def deserialize_json(data: dict) -> GetSourceRepositoryCloneUrlsResponse:
    out: GetSourceRepositoryCloneUrlsResponse = {}  # type: ignore[typeddict-item]
    if "https" in data:
        out["https"] = data["https"]
    else:
        raise DeserializationError(
            "GetSourceRepositoryCloneUrlsResponse.https required"
        )
    return out

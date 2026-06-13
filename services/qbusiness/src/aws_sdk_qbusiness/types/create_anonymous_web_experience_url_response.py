"""Generated from Smithy shape ``com.amazonaws.qbusiness#CreateAnonymousWebExperienceUrlResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.url


class CreateAnonymousWebExperienceUrlResponse(TypedDict):
    anonymous_url: NotRequired["aws_sdk_qbusiness.types.url.Url"]
    """<p>The unique URL for accessing the web experience.</p> <important> <p>This URL can only be used once and must be used within 5 minutes after it's generated.</p> </important>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAnonymousWebExperienceUrlResponse) -> dict:
    out: dict = {}
    if "anonymous_url" in value:
        out["anonymousUrl"] = value["anonymous_url"]
    return out


def deserialize_json(data: dict) -> CreateAnonymousWebExperienceUrlResponse:
    out: CreateAnonymousWebExperienceUrlResponse = {}  # type: ignore[typeddict-item]
    if "anonymousUrl" in data:
        out["anonymous_url"] = data["anonymousUrl"]
    return out

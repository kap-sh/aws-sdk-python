"""Generated from Smithy shape ``com.amazonaws.wafv2#GenerateMobileSdkReleaseUrlResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.download_url


class GenerateMobileSdkReleaseUrlResponse(TypedDict, closed=True):
    url: NotRequired["capo_wafv2.types.download_url.DownloadUrl"]
    """<p>The presigned download URL for the specified SDK release.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GenerateMobileSdkReleaseUrlResponse) -> dict:
    out: dict = {}
    if "url" in value:
        out["Url"] = value["url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GenerateMobileSdkReleaseUrlResponse:
    out: GenerateMobileSdkReleaseUrlResponse = {}  # type: ignore[typeddict-item]
    if "Url" in data:
        out["url"] = data["Url"]
    return out

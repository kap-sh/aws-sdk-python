"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#CreateApplicationPresignedUrlResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.authorized_url


class CreateApplicationPresignedUrlResponse(TypedDict, closed=True):
    authorized_url: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.authorized_url.AuthorizedUrl"
    ]
    """<p>The URL of the extension.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateApplicationPresignedUrlResponse) -> dict:
    out: dict = {}
    if "authorized_url" in value:
        out["AuthorizedUrl"] = value["authorized_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateApplicationPresignedUrlResponse:
    out: CreateApplicationPresignedUrlResponse = {}  # type: ignore[typeddict-item]
    if "AuthorizedUrl" in data:
        out["authorized_url"] = data["AuthorizedUrl"]
    return out

"""Generated from Smithy shape ``com.amazonaws.pricing#GetPriceListFileUrlResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pricing.types.string


class GetPriceListFileUrlResponse(TypedDict):
    url: NotRequired["aws_sdk_pricing.types.string.String"]
    """<p>The URL to download your Price List file from. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPriceListFileUrlResponse) -> dict:
    out: dict = {}
    if "url" in value:
        out["Url"] = value["url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPriceListFileUrlResponse:
    out: GetPriceListFileUrlResponse = {}  # type: ignore[typeddict-item]
    if "Url" in data:
        out["url"] = data["Url"]
    return out

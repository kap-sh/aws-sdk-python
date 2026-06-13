"""Generated from Smithy shape ``com.amazonaws.amp#ScraperStatus``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_amp.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amp.types.scraper_status_code


class ScraperStatus(TypedDict):
    status_code: "aws_sdk_amp.types.scraper_status_code.ScraperStatusCode"
    """<p>The current status of the scraper.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScraperStatus) -> dict:
    out: dict = {}
    out["statusCode"] = value["status_code"]
    return out


def deserialize_json(data: dict) -> ScraperStatus:
    out: ScraperStatus = {}  # type: ignore[typeddict-item]
    if "statusCode" in data:
        out["status_code"] = data["statusCode"]
    else:
        raise DeserializationError("ScraperStatus.status_code required")
    return out

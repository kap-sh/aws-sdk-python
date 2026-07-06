"""Generated from Smithy shape ``com.amazonaws.amp#ScraperLoggingConfigurationStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_amp.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amp.types.scraper_logging_configuration_status_code


class ScraperLoggingConfigurationStatus(TypedDict, closed=True):
    status_code: "aws_sdk_amp.types.scraper_logging_configuration_status_code.ScraperLoggingConfigurationStatusCode"
    """<p>The status code of the scraper logging configuration.</p>"""
    status_reason: NotRequired["str"]
    """<p>The reason for the current status of the scraper logging configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScraperLoggingConfigurationStatus) -> dict:
    out: dict = {}
    out["statusCode"] = value["status_code"]
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    return out


def deserialize_json(data: dict) -> ScraperLoggingConfigurationStatus:
    out: ScraperLoggingConfigurationStatus = {}  # type: ignore[typeddict-item]
    if "statusCode" in data:
        out["status_code"] = data["statusCode"]
    else:
        raise DeserializationError(
            "ScraperLoggingConfigurationStatus.status_code required"
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    return out

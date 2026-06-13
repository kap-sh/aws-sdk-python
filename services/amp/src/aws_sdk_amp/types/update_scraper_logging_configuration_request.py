"""Generated from Smithy shape ``com.amazonaws.amp#UpdateScraperLoggingConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_amp.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amp.types.scraper_components
    import aws_sdk_amp.types.scraper_id
    import aws_sdk_amp.types.scraper_logging_destination


class UpdateScraperLoggingConfigurationRequest(TypedDict):
    scraper_id: "aws_sdk_amp.types.scraper_id.ScraperId"
    """<p>The ID of the scraper whose logging configuration will be updated.</p>"""
    logging_destination: (
        "aws_sdk_amp.types.scraper_logging_destination.ScraperLoggingDestination"
    )
    """<p>The destination where scraper logs will be sent.</p>"""
    scraper_components: NotRequired[
        "aws_sdk_amp.types.scraper_components.ScraperComponents"
    ]
    """<p>The list of scraper components to configure for logging.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateScraperLoggingConfigurationRequest) -> dict:
    out: dict = {}
    import aws_sdk_amp.types.scraper_logging_destination

    out["loggingDestination"] = (
        aws_sdk_amp.types.scraper_logging_destination.serialize_json(
            value["logging_destination"]
        )
    )
    if "scraper_components" in value:
        import aws_sdk_amp.types.scraper_components

        out["scraperComponents"] = aws_sdk_amp.types.scraper_components.serialize_json(
            value["scraper_components"]
        )
    return out


def deserialize_json(data: dict) -> UpdateScraperLoggingConfigurationRequest:
    out: UpdateScraperLoggingConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "loggingDestination" in data:
        import aws_sdk_amp.types.scraper_logging_destination

        out["logging_destination"] = (
            aws_sdk_amp.types.scraper_logging_destination.deserialize_json(
                data["loggingDestination"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateScraperLoggingConfigurationRequest.logging_destination required"
        )
    if "scraperComponents" in data:
        import aws_sdk_amp.types.scraper_components

        out["scraper_components"] = (
            aws_sdk_amp.types.scraper_components.deserialize_json(
                data["scraperComponents"]
            )
        )
    return out

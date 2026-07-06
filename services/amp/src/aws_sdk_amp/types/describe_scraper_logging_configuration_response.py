"""Generated from Smithy shape ``com.amazonaws.amp#DescribeScraperLoggingConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_amp.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_amp.types.scraper_components
    import aws_sdk_amp.types.scraper_id
    import aws_sdk_amp.types.scraper_logging_configuration_status
    import aws_sdk_amp.types.scraper_logging_destination


class DescribeScraperLoggingConfigurationResponse(TypedDict, closed=True):
    status: "aws_sdk_amp.types.scraper_logging_configuration_status.ScraperLoggingConfigurationStatus"
    """<p>The status of the scraper logging configuration.</p>"""
    scraper_id: "aws_sdk_amp.types.scraper_id.ScraperId"
    """<p>The ID of the scraper.</p>"""
    logging_destination: (
        "aws_sdk_amp.types.scraper_logging_destination.ScraperLoggingDestination"
    )
    """<p>The destination where scraper logs are sent.</p>"""
    scraper_components: "aws_sdk_amp.types.scraper_components.ScraperComponents"
    """<p>The list of scraper components configured for logging.</p>"""
    modified_at: "datetime.datetime"
    """<p>The date and time when the logging configuration was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeScraperLoggingConfigurationResponse) -> dict:
    out: dict = {}
    import aws_sdk_amp.types.scraper_logging_configuration_status

    out["status"] = (
        aws_sdk_amp.types.scraper_logging_configuration_status.serialize_json(
            value["status"]
        )
    )
    out["scraperId"] = value["scraper_id"]
    import aws_sdk_amp.types.scraper_logging_destination

    out["loggingDestination"] = (
        aws_sdk_amp.types.scraper_logging_destination.serialize_json(
            value["logging_destination"]
        )
    )
    import aws_sdk_amp.types.scraper_components

    out["scraperComponents"] = aws_sdk_amp.types.scraper_components.serialize_json(
        value["scraper_components"]
    )
    import aws_sdk_amp.types._prelude.timestamp

    out["modifiedAt"] = aws_sdk_amp.types._prelude.timestamp.serialize_json(
        value["modified_at"]
    )
    return out


def deserialize_json(data: dict) -> DescribeScraperLoggingConfigurationResponse:
    out: DescribeScraperLoggingConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_amp.types.scraper_logging_configuration_status

        out["status"] = (
            aws_sdk_amp.types.scraper_logging_configuration_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeScraperLoggingConfigurationResponse.status required"
        )
    if "scraperId" in data:
        out["scraper_id"] = data["scraperId"]
    else:
        raise DeserializationError(
            "DescribeScraperLoggingConfigurationResponse.scraper_id required"
        )
    if "loggingDestination" in data:
        import aws_sdk_amp.types.scraper_logging_destination

        out["logging_destination"] = (
            aws_sdk_amp.types.scraper_logging_destination.deserialize_json(
                data["loggingDestination"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeScraperLoggingConfigurationResponse.logging_destination required"
        )
    if "scraperComponents" in data:
        import aws_sdk_amp.types.scraper_components

        out["scraper_components"] = (
            aws_sdk_amp.types.scraper_components.deserialize_json(
                data["scraperComponents"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeScraperLoggingConfigurationResponse.scraper_components required"
        )
    if "modifiedAt" in data:
        import aws_sdk_amp.types._prelude.timestamp

        out["modified_at"] = aws_sdk_amp.types._prelude.timestamp.deserialize_json(
            data["modifiedAt"]
        )
    else:
        raise DeserializationError(
            "DescribeScraperLoggingConfigurationResponse.modified_at required"
        )
    return out

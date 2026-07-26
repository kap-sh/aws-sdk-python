"""Generated from Smithy shape ``com.amazonaws.amp#UpdateScraperLoggingConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_amp.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amp.types.scraper_logging_configuration_status


class UpdateScraperLoggingConfigurationResponse(TypedDict, closed=True):
    status: "capo_amp.types.scraper_logging_configuration_status.ScraperLoggingConfigurationStatus"
    """<p>The status of the updated scraper logging configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateScraperLoggingConfigurationResponse) -> dict:
    out: dict = {}
    import capo_amp.types.scraper_logging_configuration_status

    out["status"] = capo_amp.types.scraper_logging_configuration_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> UpdateScraperLoggingConfigurationResponse:
    out: UpdateScraperLoggingConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import capo_amp.types.scraper_logging_configuration_status

        out["status"] = (
            capo_amp.types.scraper_logging_configuration_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateScraperLoggingConfigurationResponse.status required"
        )
    return out

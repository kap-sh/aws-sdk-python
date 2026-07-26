"""Generated from Smithy shape ``com.amazonaws.amp#DeleteScraperLoggingConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amp.types.idempotency_token
    import capo_amp.types.scraper_id


class DeleteScraperLoggingConfigurationRequest(TypedDict, closed=True):
    scraper_id: "capo_amp.types.scraper_id.ScraperId"
    """<p>The ID of the scraper whose logging configuration will be deleted.</p>"""
    client_token: NotRequired["capo_amp.types.idempotency_token.IdempotencyToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the request is processed exactly once.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteScraperLoggingConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteScraperLoggingConfigurationRequest:
    out: DeleteScraperLoggingConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out

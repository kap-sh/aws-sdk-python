"""Generated from Smithy shape ``com.amazonaws.amp#DeleteScraperRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amp.types.idempotency_token
    import aws_sdk_amp.types.scraper_id


class DeleteScraperRequest(TypedDict, closed=True):
    scraper_id: "aws_sdk_amp.types.scraper_id.ScraperId"
    """<p>The ID of the scraper to delete.</p>"""
    client_token: NotRequired["aws_sdk_amp.types.idempotency_token.IdempotencyToken"]
    """<p>(Optional) A unique, case-sensitive identifier that you can provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteScraperRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteScraperRequest:
    out: DeleteScraperRequest = {}  # type: ignore[typeddict-item]
    return out

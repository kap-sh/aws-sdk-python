"""Generated from Smithy shape ``com.amazonaws.emrserverless#GetResourceDashboardResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_serverless.types.url


class GetResourceDashboardResponse(TypedDict, closed=True):
    url: NotRequired["capo_emr_serverless.types.url.Url"]
    """<p>A URL to the resource dashboard. For an active resource, this URL opens the live application UI. For a terminated resource, this URL opens the persistent application UI. This value is not included in the response if the URL is not available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourceDashboardResponse) -> dict:
    out: dict = {}
    if "url" in value:
        out["url"] = value["url"]
    return out


def deserialize_json(data: dict) -> GetResourceDashboardResponse:
    out: GetResourceDashboardResponse = {}  # type: ignore[typeddict-item]
    if "url" in data:
        out["url"] = data["url"]
    return out

"""Generated from Smithy shape ``com.amazonaws.emrserverless#GetDashboardForJobRunResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.url


class GetDashboardForJobRunResponse(TypedDict):
    url: NotRequired["aws_sdk_emr_serverless.types.url.Url"]
    """<p>The URL to view job run's dashboard.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDashboardForJobRunResponse) -> dict:
    out: dict = {}
    if "url" in value:
        out["url"] = value["url"]
    return out


def deserialize_json(data: dict) -> GetDashboardForJobRunResponse:
    out: GetDashboardForJobRunResponse = {}  # type: ignore[typeddict-item]
    if "url" in data:
        out["url"] = data["url"]
    return out

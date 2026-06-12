"""Generated from Smithy shape ``com.amazonaws.cloudsearchdomain#SuggestResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudsearch_domain.types.suggest_model
    import aws_sdk_cloudsearch_domain.types.suggest_status


class SuggestResponse(TypedDict):
    status: NotRequired["aws_sdk_cloudsearch_domain.types.suggest_status.SuggestStatus"]
    """<p>The status of a <code>SuggestRequest</code>. Contains the resource ID (<code>rid</code>) and how long it took to process the request (<code>timems</code>).</p>"""
    suggest: NotRequired["aws_sdk_cloudsearch_domain.types.suggest_model.SuggestModel"]
    """<p>Container for the matching search suggestion information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuggestResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_cloudsearch_domain.types.suggest_status

        out["status"] = aws_sdk_cloudsearch_domain.types.suggest_status.serialize_json(
            value["status"]
        )
    if "suggest" in value:
        import aws_sdk_cloudsearch_domain.types.suggest_model

        out["suggest"] = aws_sdk_cloudsearch_domain.types.suggest_model.serialize_json(
            value["suggest"]
        )
    return out


def deserialize_json(data: dict) -> SuggestResponse:
    out: SuggestResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_cloudsearch_domain.types.suggest_status

        out["status"] = (
            aws_sdk_cloudsearch_domain.types.suggest_status.deserialize_json(
                data["status"]
            )
        )
    if "suggest" in data:
        import aws_sdk_cloudsearch_domain.types.suggest_model

        out["suggest"] = (
            aws_sdk_cloudsearch_domain.types.suggest_model.deserialize_json(
                data["suggest"]
            )
        )
    return out

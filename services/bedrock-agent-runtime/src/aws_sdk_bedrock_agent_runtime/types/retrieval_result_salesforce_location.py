"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrievalResultSalesforceLocation``."""

from typing import TypedDict

from typing_extensions import NotRequired


class RetrievalResultSalesforceLocation(TypedDict):
    url: NotRequired["str"]
    """<p>The Salesforce host URL for the data source location.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalResultSalesforceLocation) -> dict:
    out: dict = {}
    if "url" in value:
        out["url"] = value["url"]
    return out


def deserialize_json(data: dict) -> RetrievalResultSalesforceLocation:
    out: RetrievalResultSalesforceLocation = {}  # type: ignore[typeddict-item]
    if "url" in data:
        out["url"] = data["url"]
    return out

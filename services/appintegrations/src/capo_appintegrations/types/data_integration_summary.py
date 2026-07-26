"""Generated from Smithy shape ``com.amazonaws.appintegrations#DataIntegrationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appintegrations.types.arn
    import capo_appintegrations.types.name
    import capo_appintegrations.types.source_uri


class DataIntegrationSummary(TypedDict, closed=True):
    arn: NotRequired["capo_appintegrations.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the DataIntegration.</p>"""
    name: NotRequired["capo_appintegrations.types.name.Name"]
    """<p>The name of the DataIntegration.</p>"""
    source_uri: NotRequired["capo_appintegrations.types.source_uri.SourceURI"]
    """<p>The URI of the data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "source_uri" in value:
        out["SourceURI"] = value["source_uri"]
    return out


def deserialize_json(data: dict) -> DataIntegrationSummary:
    out: DataIntegrationSummary = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "SourceURI" in data:
        out["source_uri"] = data["SourceURI"]
    return out

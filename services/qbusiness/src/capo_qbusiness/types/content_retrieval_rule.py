"""Generated from Smithy shape ``com.amazonaws.qbusiness#ContentRetrievalRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.eligible_data_sources


class ContentRetrievalRule(TypedDict, closed=True):
    eligible_data_sources: NotRequired[
        "capo_qbusiness.types.eligible_data_sources.EligibleDataSources"
    ]
    """<p>Specifies data sources in a Amazon Q Business application to use for content generation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContentRetrievalRule) -> dict:
    out: dict = {}
    if "eligible_data_sources" in value:
        import capo_qbusiness.types.eligible_data_sources

        out["eligibleDataSources"] = (
            capo_qbusiness.types.eligible_data_sources.serialize_json(
                value["eligible_data_sources"]
            )
        )
    return out


def deserialize_json(data: dict) -> ContentRetrievalRule:
    out: ContentRetrievalRule = {}  # type: ignore[typeddict-item]
    if "eligibleDataSources" in data:
        import capo_qbusiness.types.eligible_data_sources

        out["eligible_data_sources"] = (
            capo_qbusiness.types.eligible_data_sources.deserialize_json(
                data["eligibleDataSources"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.qbusiness#ContentRetrievalRule``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.eligible_data_sources


class ContentRetrievalRule(TypedDict):
    eligible_data_sources: NotRequired[
        "aws_sdk_qbusiness.types.eligible_data_sources.EligibleDataSources"
    ]
    """<p>Specifies data sources in a Amazon Q Business application to use for content generation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContentRetrievalRule) -> dict:
    out: dict = {}
    if "eligible_data_sources" in value:
        import aws_sdk_qbusiness.types.eligible_data_sources

        out["eligibleDataSources"] = (
            aws_sdk_qbusiness.types.eligible_data_sources.serialize_json(
                value["eligible_data_sources"]
            )
        )
    return out


def deserialize_json(data: dict) -> ContentRetrievalRule:
    out: ContentRetrievalRule = {}  # type: ignore[typeddict-item]
    if "eligibleDataSources" in data:
        import aws_sdk_qbusiness.types.eligible_data_sources

        out["eligible_data_sources"] = (
            aws_sdk_qbusiness.types.eligible_data_sources.deserialize_json(
                data["eligibleDataSources"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#AudienceQualityMetrics``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.relevance_metrics


class AudienceQualityMetrics(TypedDict):
    relevance_metrics: "aws_sdk_cleanroomsml.types.relevance_metrics.RelevanceMetrics"
    """<p>The relevance scores of the generated audience.</p>"""
    recall_metric: NotRequired["float"]
    """<p>The recall score of the generated audience. Recall is the percentage of the most similar users (by default, the most similar 20%) from a sample of the training data that are included in the seed audience by the audience generation job. Values range from 0-1, larger values indicate a better audience. A recall value approximately equal to the maximum bin size indicates that the audience model is equivalent to random selection. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AudienceQualityMetrics) -> dict:
    out: dict = {}
    import aws_sdk_cleanroomsml.types.relevance_metrics

    out["relevanceMetrics"] = (
        aws_sdk_cleanroomsml.types.relevance_metrics.serialize_json(
            value["relevance_metrics"]
        )
    )
    if "recall_metric" in value:
        out["recallMetric"] = value["recall_metric"]
    return out


def deserialize_json(data: dict) -> AudienceQualityMetrics:
    out: AudienceQualityMetrics = {}  # type: ignore[typeddict-item]
    if "relevanceMetrics" in data:
        import aws_sdk_cleanroomsml.types.relevance_metrics

        out["relevance_metrics"] = (
            aws_sdk_cleanroomsml.types.relevance_metrics.deserialize_json(
                data["relevanceMetrics"]
            )
        )
    else:
        raise DeserializationError("AudienceQualityMetrics.relevance_metrics required")
    if "recallMetric" in data:
        out["recall_metric"] = data["recallMetric"]
    return out

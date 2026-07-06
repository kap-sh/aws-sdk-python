"""Generated from Smithy shape ``com.amazonaws.cleanrooms#DifferentialPrivacyPrivacyImpact``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.differential_privacy_preview_aggregation_list


class DifferentialPrivacyPrivacyImpact(TypedDict, closed=True):
    aggregations: "aws_sdk_cleanrooms.types.differential_privacy_preview_aggregation_list.DifferentialPrivacyPreviewAggregationList"
    """<p>The number of aggregation functions that you can perform.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DifferentialPrivacyPrivacyImpact) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.differential_privacy_preview_aggregation_list

    out["aggregations"] = (
        aws_sdk_cleanrooms.types.differential_privacy_preview_aggregation_list.serialize_json(
            value["aggregations"]
        )
    )
    return out


def deserialize_json(data: dict) -> DifferentialPrivacyPrivacyImpact:
    out: DifferentialPrivacyPrivacyImpact = {}  # type: ignore[typeddict-item]
    if "aggregations" in data:
        import aws_sdk_cleanrooms.types.differential_privacy_preview_aggregation_list

        out["aggregations"] = (
            aws_sdk_cleanrooms.types.differential_privacy_preview_aggregation_list.deserialize_json(
                data["aggregations"]
            )
        )
    else:
        raise DeserializationError(
            "DifferentialPrivacyPrivacyImpact.aggregations required"
        )
    return out

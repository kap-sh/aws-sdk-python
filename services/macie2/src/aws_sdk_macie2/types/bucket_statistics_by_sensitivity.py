"""Generated from Smithy shape ``com.amazonaws.macie2#BucketStatisticsBySensitivity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.sensitivity_aggregations


class BucketStatisticsBySensitivity(TypedDict, closed=True):
    classification_error: NotRequired[
        "aws_sdk_macie2.types.sensitivity_aggregations.SensitivityAggregations"
    ]
    """<p>The aggregated statistical data for all buckets that have a sensitivity score of -1.</p>"""
    not_classified: NotRequired[
        "aws_sdk_macie2.types.sensitivity_aggregations.SensitivityAggregations"
    ]
    """<p>The aggregated statistical data for all buckets that have a sensitivity score of 50.</p>"""
    not_sensitive: NotRequired[
        "aws_sdk_macie2.types.sensitivity_aggregations.SensitivityAggregations"
    ]
    """<p>The aggregated statistical data for all buckets that have a sensitivity score of 1-49.</p>"""
    sensitive: NotRequired[
        "aws_sdk_macie2.types.sensitivity_aggregations.SensitivityAggregations"
    ]
    """<p>The aggregated statistical data for all buckets that have a sensitivity score of 51-100.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BucketStatisticsBySensitivity) -> dict:
    out: dict = {}
    if "classification_error" in value:
        import aws_sdk_macie2.types.sensitivity_aggregations

        out["classificationError"] = (
            aws_sdk_macie2.types.sensitivity_aggregations.serialize_json(
                value["classification_error"]
            )
        )
    if "not_classified" in value:
        import aws_sdk_macie2.types.sensitivity_aggregations

        out["notClassified"] = (
            aws_sdk_macie2.types.sensitivity_aggregations.serialize_json(
                value["not_classified"]
            )
        )
    if "not_sensitive" in value:
        import aws_sdk_macie2.types.sensitivity_aggregations

        out["notSensitive"] = (
            aws_sdk_macie2.types.sensitivity_aggregations.serialize_json(
                value["not_sensitive"]
            )
        )
    if "sensitive" in value:
        import aws_sdk_macie2.types.sensitivity_aggregations

        out["sensitive"] = aws_sdk_macie2.types.sensitivity_aggregations.serialize_json(
            value["sensitive"]
        )
    return out


def deserialize_json(data: dict) -> BucketStatisticsBySensitivity:
    out: BucketStatisticsBySensitivity = {}  # type: ignore[typeddict-item]
    if "classificationError" in data:
        import aws_sdk_macie2.types.sensitivity_aggregations

        out["classification_error"] = (
            aws_sdk_macie2.types.sensitivity_aggregations.deserialize_json(
                data["classificationError"]
            )
        )
    if "notClassified" in data:
        import aws_sdk_macie2.types.sensitivity_aggregations

        out["not_classified"] = (
            aws_sdk_macie2.types.sensitivity_aggregations.deserialize_json(
                data["notClassified"]
            )
        )
    if "notSensitive" in data:
        import aws_sdk_macie2.types.sensitivity_aggregations

        out["not_sensitive"] = (
            aws_sdk_macie2.types.sensitivity_aggregations.deserialize_json(
                data["notSensitive"]
            )
        )
    if "sensitive" in data:
        import aws_sdk_macie2.types.sensitivity_aggregations

        out["sensitive"] = (
            aws_sdk_macie2.types.sensitivity_aggregations.deserialize_json(
                data["sensitive"]
            )
        )
    return out

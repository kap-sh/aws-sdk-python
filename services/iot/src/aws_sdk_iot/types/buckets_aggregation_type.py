"""Generated from Smithy shape ``com.amazonaws.iot#BucketsAggregationType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.terms_aggregation


class BucketsAggregationType(TypedDict, closed=True):
    terms_aggregation: NotRequired[
        "aws_sdk_iot.types.terms_aggregation.TermsAggregation"
    ]
    """<p>Performs an aggregation that will return a list of buckets. The list of buckets is a ranked list of the number of occurrences of an aggregation field value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BucketsAggregationType) -> dict:
    out: dict = {}
    if "terms_aggregation" in value:
        import aws_sdk_iot.types.terms_aggregation

        out["termsAggregation"] = aws_sdk_iot.types.terms_aggregation.serialize_json(
            value["terms_aggregation"]
        )
    return out


def deserialize_json(data: dict) -> BucketsAggregationType:
    out: BucketsAggregationType = {}  # type: ignore[typeddict-item]
    if "termsAggregation" in data:
        import aws_sdk_iot.types.terms_aggregation

        out["terms_aggregation"] = aws_sdk_iot.types.terms_aggregation.deserialize_json(
            data["termsAggregation"]
        )
    return out

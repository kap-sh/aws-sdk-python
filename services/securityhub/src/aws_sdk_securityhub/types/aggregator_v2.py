"""Generated from Smithy shape ``com.amazonaws.securityhub#AggregatorV2``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AggregatorV2(TypedDict, closed=True):
    aggregator_v2_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the aggregatorV2.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AggregatorV2) -> dict:
    out: dict = {}
    if "aggregator_v2_arn" in value:
        out["AggregatorV2Arn"] = value["aggregator_v2_arn"]
    return out


def deserialize_json(data: dict) -> AggregatorV2:
    out: AggregatorV2 = {}  # type: ignore[typeddict-item]
    if "AggregatorV2Arn" in data:
        out["aggregator_v2_arn"] = data["AggregatorV2Arn"]
    return out

"""Generated from Smithy shape ``com.amazonaws.securityhub#GetAggregatorV2Request``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class GetAggregatorV2Request(TypedDict, closed=True):
    aggregator_v2_arn: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    """<p>The ARN of the Aggregator V2.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAggregatorV2Request) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAggregatorV2Request:
    out: GetAggregatorV2Request = {}  # type: ignore[typeddict-item]
    return out

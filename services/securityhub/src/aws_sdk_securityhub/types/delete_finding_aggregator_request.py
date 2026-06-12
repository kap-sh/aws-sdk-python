"""Generated from Smithy shape ``com.amazonaws.securityhub#DeleteFindingAggregatorRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class DeleteFindingAggregatorRequest(TypedDict):
    finding_aggregator_arn: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    """<p>The ARN of the finding aggregator to delete. To obtain the ARN, use <code>ListFindingAggregators</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFindingAggregatorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteFindingAggregatorRequest:
    out: DeleteFindingAggregatorRequest = {}  # type: ignore[typeddict-item]
    return out

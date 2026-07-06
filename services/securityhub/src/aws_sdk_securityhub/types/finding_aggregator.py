"""Generated from Smithy shape ``com.amazonaws.securityhub#FindingAggregator``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class FindingAggregator(TypedDict, closed=True):
    finding_aggregator_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the finding aggregator. You use the finding aggregator ARN to retrieve details for, update, and delete the finding aggregator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingAggregator) -> dict:
    out: dict = {}
    if "finding_aggregator_arn" in value:
        out["FindingAggregatorArn"] = value["finding_aggregator_arn"]
    return out


def deserialize_json(data: dict) -> FindingAggregator:
    out: FindingAggregator = {}  # type: ignore[typeddict-item]
    if "FindingAggregatorArn" in data:
        out["finding_aggregator_arn"] = data["FindingAggregatorArn"]
    return out

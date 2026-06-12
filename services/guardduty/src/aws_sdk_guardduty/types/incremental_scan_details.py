"""Generated from Smithy shape ``com.amazonaws.guardduty#IncrementalScanDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.non_empty_string


class IncrementalScanDetails(TypedDict):
    baseline_resource_arn: NotRequired[
        "aws_sdk_guardduty.types.non_empty_string.NonEmptyString"
    ]
    """<p>Amazon Resource Name (ARN) of the baseline resource used for incremental scanning. The scan will only process changes since this baseline resource was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IncrementalScanDetails) -> dict:
    out: dict = {}
    if "baseline_resource_arn" in value:
        out["baselineResourceArn"] = value["baseline_resource_arn"]
    return out


def deserialize_json(data: dict) -> IncrementalScanDetails:
    out: IncrementalScanDetails = {}  # type: ignore[typeddict-item]
    if "baselineResourceArn" in data:
        out["baseline_resource_arn"] = data["baselineResourceArn"]
    return out

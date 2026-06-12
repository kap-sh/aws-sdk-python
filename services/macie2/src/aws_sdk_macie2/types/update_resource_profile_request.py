"""Generated from Smithy shape ``com.amazonaws.macie2#UpdateResourceProfileRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__integer
    import aws_sdk_macie2.types.__string


class UpdateResourceProfileRequest(TypedDict):
    resource_arn: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the S3 bucket that the request applies to.</p>"""
    sensitivity_score_override: NotRequired["aws_sdk_macie2.types.__integer.__integer"]
    """<p>The new sensitivity score for the bucket. Valid values are: 100, assign the maximum score and apply the <i>Sensitive</i> label to the bucket; and, null (empty), assign a score that Amazon Macie calculates automatically after you submit the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateResourceProfileRequest) -> dict:
    out: dict = {}
    if "sensitivity_score_override" in value:
        out["sensitivityScoreOverride"] = value["sensitivity_score_override"]
    return out


def deserialize_json(data: dict) -> UpdateResourceProfileRequest:
    out: UpdateResourceProfileRequest = {}  # type: ignore[typeddict-item]
    if "sensitivityScoreOverride" in data:
        out["sensitivity_score_override"] = data["sensitivityScoreOverride"]
    return out

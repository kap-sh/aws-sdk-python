"""Generated from Smithy shape ``com.amazonaws.frauddetector#DescribeDetectorResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.detector_version_summary_list
    import capo_frauddetector.types.fraud_detector_arn
    import capo_frauddetector.types.identifier
    import capo_frauddetector.types.string


class DescribeDetectorResult(TypedDict, closed=True):
    detector_id: NotRequired["capo_frauddetector.types.identifier.identifier"]
    """<p>The detector ID.</p>"""
    detector_version_summaries: NotRequired[
        "capo_frauddetector.types.detector_version_summary_list.DetectorVersionSummaryList"
    ]
    """<p>The status and description for each detector version.</p>"""
    next_token: NotRequired["capo_frauddetector.types.string.string"]
    """<p>The next token to be used for subsequent requests.</p>"""
    arn: NotRequired["capo_frauddetector.types.fraud_detector_arn.fraudDetectorArn"]
    """<p>The detector ARN.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDetectorResult) -> dict:
    out: dict = {}
    if "detector_id" in value:
        out["detectorId"] = value["detector_id"]
    if "detector_version_summaries" in value:
        import capo_frauddetector.types.detector_version_summary_list

        out["detectorVersionSummaries"] = (
            capo_frauddetector.types.detector_version_summary_list.serialize_aws_json_1_1(
                value["detector_version_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDetectorResult:
    out: DescribeDetectorResult = {}  # type: ignore[typeddict-item]
    if "detectorId" in data:
        out["detector_id"] = data["detectorId"]
    if "detectorVersionSummaries" in data:
        import capo_frauddetector.types.detector_version_summary_list

        out["detector_version_summaries"] = (
            capo_frauddetector.types.detector_version_summary_list.deserialize_aws_json_1_1(
                data["detectorVersionSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "arn" in data:
        out["arn"] = data["arn"]
    return out

"""Generated from Smithy shape ``com.amazonaws.frauddetector#DetectorVersionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.detector_version_summary

DetectorVersionSummaryList: TypeAlias = list[
    "aws_sdk_frauddetector.types.detector_version_summary.DetectorVersionSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectorVersionSummaryList) -> list:
    import aws_sdk_frauddetector.types.detector_version_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_frauddetector.types.detector_version_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DetectorVersionSummaryList:
    import aws_sdk_frauddetector.types.detector_version_summary

    out: DetectorVersionSummaryList = []
    for item in data:
        out.append(
            aws_sdk_frauddetector.types.detector_version_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out

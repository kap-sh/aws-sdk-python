"""Generated from Smithy shape ``com.amazonaws.frauddetector#DetectorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.detector

DetectorList: TypeAlias = list["aws_sdk_frauddetector.types.detector.Detector"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectorList) -> list:
    import aws_sdk_frauddetector.types.detector

    out: list = []
    for item in value:
        out.append(aws_sdk_frauddetector.types.detector.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DetectorList:
    import aws_sdk_frauddetector.types.detector

    out: DetectorList = []
    for item in data:
        out.append(aws_sdk_frauddetector.types.detector.deserialize_aws_json_1_1(item))
    return out

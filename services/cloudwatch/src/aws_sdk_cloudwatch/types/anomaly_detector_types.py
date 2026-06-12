"""Generated from Smithy shape ``com.amazonaws.cloudwatch#AnomalyDetectorTypes``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.anomaly_detector_type

AnomalyDetectorTypes: TypeAlias = list[
    "aws_sdk_cloudwatch.types.anomaly_detector_type.AnomalyDetectorType"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: AnomalyDetectorTypes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudwatch.types.anomaly_detector_type

    for n, item in enumerate(value, 1):
        aws_sdk_cloudwatch.types.anomaly_detector_type.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> AnomalyDetectorTypes:
    import aws_sdk_cloudwatch.types.anomaly_detector_type

    out: AnomalyDetectorTypes = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_cloudwatch.types.anomaly_detector_type.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: AnomalyDetectorTypes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudwatch.types.anomaly_detector_type

    for n, item in enumerate(value, 1):
        aws_sdk_cloudwatch.types.anomaly_detector_type.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> AnomalyDetectorTypes:
    import aws_sdk_cloudwatch.types.anomaly_detector_type

    out: AnomalyDetectorTypes = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_cloudwatch.types.anomaly_detector_type.deserialize_query(child)
        )
    return out


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AnomalyDetectorTypes) -> list:
    import aws_sdk_cloudwatch.types.anomaly_detector_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch.types.anomaly_detector_type.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AnomalyDetectorTypes:
    import aws_sdk_cloudwatch.types.anomaly_detector_type

    out: AnomalyDetectorTypes = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch.types.anomaly_detector_type.deserialize_aws_json_1_0(
                item
            )
        )
    return out

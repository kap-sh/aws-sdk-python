"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DescribeAnomalyDetectorsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.anomaly_detectors
    import aws_sdk_cloudwatch.types.next_token


class DescribeAnomalyDetectorsOutput(TypedDict):
    anomaly_detectors: NotRequired[
        "aws_sdk_cloudwatch.types.anomaly_detectors.AnomalyDetectors"
    ]
    """<p>The list of anomaly detection models returned by the operation.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch.types.next_token.NextToken"]
    """<p>A token that you can use in a subsequent operation to retrieve the next set of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeAnomalyDetectorsOutput) -> dict:
    out: dict = {}
    if "anomaly_detectors" in value:
        import aws_sdk_cloudwatch.types.anomaly_detectors

        out["AnomalyDetectors"] = (
            aws_sdk_cloudwatch.types.anomaly_detectors.serialize_aws_json_1_0(
                value["anomaly_detectors"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeAnomalyDetectorsOutput:
    out: DescribeAnomalyDetectorsOutput = {}  # type: ignore[typeddict-item]
    if "AnomalyDetectors" in data:
        import aws_sdk_cloudwatch.types.anomaly_detectors

        out["anomaly_detectors"] = (
            aws_sdk_cloudwatch.types.anomaly_detectors.deserialize_aws_json_1_0(
                data["AnomalyDetectors"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeAnomalyDetectorsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "anomaly_detectors" in value:
        import aws_sdk_cloudwatch.types.anomaly_detectors

        aws_sdk_cloudwatch.types.anomaly_detectors.serialize_query(
            value["anomaly_detectors"], pairs, f"{prefix}.AnomalyDetectors"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> DescribeAnomalyDetectorsOutput:
    out: DescribeAnomalyDetectorsOutput = {}  # type: ignore[typeddict-item]
    child_anomaly_detectors = el.find("AnomalyDetectors")
    if child_anomaly_detectors is not None:
        import aws_sdk_cloudwatch.types.anomaly_detectors

        out["anomaly_detectors"] = (
            aws_sdk_cloudwatch.types.anomaly_detectors.deserialize_query(
                child_anomaly_detectors
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out

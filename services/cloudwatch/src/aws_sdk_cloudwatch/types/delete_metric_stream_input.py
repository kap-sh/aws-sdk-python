"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DeleteMetricStreamInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.metric_stream_name


class DeleteMetricStreamInput(TypedDict, closed=True):
    name: NotRequired["aws_sdk_cloudwatch.types.metric_stream_name.MetricStreamName"]
    """<p>The name of the metric stream to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteMetricStreamInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteMetricStreamInput:
    out: DeleteMetricStreamInput = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteMetricStreamInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "name" in value:
        pairs.append((f"{prefix}.Name", str(value["name"])))


def deserialize_query(el: Element) -> DeleteMetricStreamInput:
    out: DeleteMetricStreamInput = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    return out

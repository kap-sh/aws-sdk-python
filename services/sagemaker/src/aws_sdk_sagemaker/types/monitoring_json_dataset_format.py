"""Generated from Smithy shape ``com.amazonaws.sagemaker#MonitoringJsonDatasetFormat``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.boolean


class MonitoringJsonDatasetFormat(TypedDict):
    line: NotRequired["aws_sdk_sagemaker.types.boolean.Boolean"]
    """<p>Indicates if the file should be read as a JSON object per line. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitoringJsonDatasetFormat) -> dict:
    out: dict = {}
    if "line" in value:
        out["Line"] = value["line"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MonitoringJsonDatasetFormat:
    out: MonitoringJsonDatasetFormat = {}  # type: ignore[typeddict-item]
    if "Line" in data:
        out["line"] = data["Line"]
    return out

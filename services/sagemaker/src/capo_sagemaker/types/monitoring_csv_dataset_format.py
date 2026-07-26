"""Generated from Smithy shape ``com.amazonaws.sagemaker#MonitoringCsvDatasetFormat``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.boolean


class MonitoringCsvDatasetFormat(TypedDict, closed=True):
    header: NotRequired["capo_sagemaker.types.boolean.Boolean"]
    """<p>Indicates if the CSV data has a header.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitoringCsvDatasetFormat) -> dict:
    out: dict = {}
    if "header" in value:
        out["Header"] = value["header"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MonitoringCsvDatasetFormat:
    out: MonitoringCsvDatasetFormat = {}  # type: ignore[typeddict-item]
    if "Header" in data:
        out["header"] = data["Header"]
    return out

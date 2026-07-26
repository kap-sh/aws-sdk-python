"""Generated from Smithy shape ``com.amazonaws.sagemaker#MonitoringDatasetFormat``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.monitoring_csv_dataset_format
    import capo_sagemaker.types.monitoring_json_dataset_format
    import capo_sagemaker.types.monitoring_parquet_dataset_format


class MonitoringDatasetFormat(TypedDict, closed=True):
    csv: NotRequired[
        "capo_sagemaker.types.monitoring_csv_dataset_format.MonitoringCsvDatasetFormat"
    ]
    """<p>The CSV dataset used in the monitoring job.</p>"""
    json: NotRequired[
        "capo_sagemaker.types.monitoring_json_dataset_format.MonitoringJsonDatasetFormat"
    ]
    """<p>The JSON dataset used in the monitoring job</p>"""
    parquet: NotRequired[
        "capo_sagemaker.types.monitoring_parquet_dataset_format.MonitoringParquetDatasetFormat"
    ]
    """<p>The Parquet dataset used in the monitoring job</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitoringDatasetFormat) -> dict:
    out: dict = {}
    if "csv" in value:
        import capo_sagemaker.types.monitoring_csv_dataset_format

        out["Csv"] = (
            capo_sagemaker.types.monitoring_csv_dataset_format.serialize_aws_json_1_1(
                value["csv"]
            )
        )
    if "json" in value:
        import capo_sagemaker.types.monitoring_json_dataset_format

        out["Json"] = (
            capo_sagemaker.types.monitoring_json_dataset_format.serialize_aws_json_1_1(
                value["json"]
            )
        )
    if "parquet" in value:
        import capo_sagemaker.types.monitoring_parquet_dataset_format

        out["Parquet"] = (
            capo_sagemaker.types.monitoring_parquet_dataset_format.serialize_aws_json_1_1(
                value["parquet"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MonitoringDatasetFormat:
    out: MonitoringDatasetFormat = {}  # type: ignore[typeddict-item]
    if "Csv" in data:
        import capo_sagemaker.types.monitoring_csv_dataset_format

        out["csv"] = (
            capo_sagemaker.types.monitoring_csv_dataset_format.deserialize_aws_json_1_1(
                data["Csv"]
            )
        )
    if "Json" in data:
        import capo_sagemaker.types.monitoring_json_dataset_format

        out["json"] = (
            capo_sagemaker.types.monitoring_json_dataset_format.deserialize_aws_json_1_1(
                data["Json"]
            )
        )
    if "Parquet" in data:
        import capo_sagemaker.types.monitoring_parquet_dataset_format

        out["parquet"] = (
            capo_sagemaker.types.monitoring_parquet_dataset_format.deserialize_aws_json_1_1(
                data["Parquet"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.emrcontainers#SparkSqlJobDriver``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.entry_point_path
    import aws_sdk_emr_containers.types.spark_sql_parameters


class SparkSqlJobDriver(TypedDict, closed=True):
    entry_point: NotRequired[
        "aws_sdk_emr_containers.types.entry_point_path.EntryPointPath"
    ]
    """<p>The SQL file to be executed.</p>"""
    spark_sql_parameters: NotRequired[
        "aws_sdk_emr_containers.types.spark_sql_parameters.SparkSqlParameters"
    ]
    """<p>The Spark parameters to be included in the Spark SQL command.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SparkSqlJobDriver) -> dict:
    out: dict = {}
    if "entry_point" in value:
        out["entryPoint"] = value["entry_point"]
    if "spark_sql_parameters" in value:
        out["sparkSqlParameters"] = value["spark_sql_parameters"]
    return out


def deserialize_json(data: dict) -> SparkSqlJobDriver:
    out: SparkSqlJobDriver = {}  # type: ignore[typeddict-item]
    if "entryPoint" in data:
        out["entry_point"] = data["entryPoint"]
    if "sparkSqlParameters" in data:
        out["spark_sql_parameters"] = data["sparkSqlParameters"]
    return out

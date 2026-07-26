"""Generated from Smithy shape ``com.amazonaws.emrcontainers#JobDriver``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_containers.types.spark_sql_job_driver
    import capo_emr_containers.types.spark_submit_job_driver


class JobDriver(TypedDict, closed=True):
    spark_submit_job_driver: NotRequired[
        "capo_emr_containers.types.spark_submit_job_driver.SparkSubmitJobDriver"
    ]
    """<p>The job driver parameters specified for spark submit.</p>"""
    spark_sql_job_driver: NotRequired[
        "capo_emr_containers.types.spark_sql_job_driver.SparkSqlJobDriver"
    ]
    """<p>The job driver for job type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobDriver) -> dict:
    out: dict = {}
    if "spark_submit_job_driver" in value:
        import capo_emr_containers.types.spark_submit_job_driver

        out["sparkSubmitJobDriver"] = (
            capo_emr_containers.types.spark_submit_job_driver.serialize_json(
                value["spark_submit_job_driver"]
            )
        )
    if "spark_sql_job_driver" in value:
        import capo_emr_containers.types.spark_sql_job_driver

        out["sparkSqlJobDriver"] = (
            capo_emr_containers.types.spark_sql_job_driver.serialize_json(
                value["spark_sql_job_driver"]
            )
        )
    return out


def deserialize_json(data: dict) -> JobDriver:
    out: JobDriver = {}  # type: ignore[typeddict-item]
    if "sparkSubmitJobDriver" in data:
        import capo_emr_containers.types.spark_submit_job_driver

        out["spark_submit_job_driver"] = (
            capo_emr_containers.types.spark_submit_job_driver.deserialize_json(
                data["sparkSubmitJobDriver"]
            )
        )
    if "sparkSqlJobDriver" in data:
        import capo_emr_containers.types.spark_sql_job_driver

        out["spark_sql_job_driver"] = (
            capo_emr_containers.types.spark_sql_job_driver.deserialize_json(
                data["sparkSqlJobDriver"]
            )
        )
    return out

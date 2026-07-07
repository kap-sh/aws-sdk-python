"""Generated from Smithy shape ``com.amazonaws.emrserverless#JobDriver``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_emr_serverless.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.hive
    import aws_sdk_emr_serverless.types.spark_submit


class _JobDriver_sparkSubmit(TypedDict, closed=True):
    sparkSubmit: "aws_sdk_emr_serverless.types.spark_submit.SparkSubmit"


class _JobDriver_hive(TypedDict, closed=True):
    hive: "aws_sdk_emr_serverless.types.hive.Hive"


JobDriver: TypeAlias = _JobDriver_sparkSubmit | _JobDriver_hive


# --- restJson1 ser/de ---
def serialize_json(value: JobDriver) -> dict:
    if "sparkSubmit" in value:
        import aws_sdk_emr_serverless.types.spark_submit

        return {
            "sparkSubmit": aws_sdk_emr_serverless.types.spark_submit.serialize_json(
                value["sparkSubmit"]
            )
        }
    elif "hive" in value:
        import aws_sdk_emr_serverless.types.hive

        return {"hive": aws_sdk_emr_serverless.types.hive.serialize_json(value["hive"])}
    else:
        raise SerializationError("JobDriver: no variant present")


def deserialize_json(data: dict) -> JobDriver:
    if "sparkSubmit" in data:
        import aws_sdk_emr_serverless.types.spark_submit

        return {
            "sparkSubmit": aws_sdk_emr_serverless.types.spark_submit.deserialize_json(
                data["sparkSubmit"]
            )
        }
    elif "hive" in data:
        import aws_sdk_emr_serverless.types.hive

        return {
            "hive": aws_sdk_emr_serverless.types.hive.deserialize_json(data["hive"])
        }
    else:
        raise DeserializationError("JobDriver: no recognized variant key")

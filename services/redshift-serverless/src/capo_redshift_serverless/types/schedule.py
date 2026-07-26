"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#Schedule``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_redshift_serverless.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import datetime


class _Schedule_at(TypedDict, closed=True):
    at: "datetime.datetime"


class _Schedule_cron(TypedDict, closed=True):
    cron: "str"


Schedule: TypeAlias = _Schedule_at | _Schedule_cron


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Schedule) -> dict:
    if "at" in value:
        import capo_redshift_serverless.types._prelude.timestamp

        return {
            "at": capo_redshift_serverless.types._prelude.timestamp.serialize_aws_json_1_1(
                value["at"]
            )
        }
    elif "cron" in value:
        return {"cron": value["cron"]}
    else:
        raise SerializationError("Schedule: no variant present")


def deserialize_aws_json_1_1(data: dict) -> Schedule:
    if "at" in data:
        import capo_redshift_serverless.types._prelude.timestamp

        return {
            "at": capo_redshift_serverless.types._prelude.timestamp.deserialize_aws_json_1_1(
                data["at"]
            )
        }
    elif "cron" in data:
        return {"cron": data["cron"]}
    else:
        raise DeserializationError("Schedule: no recognized variant key")

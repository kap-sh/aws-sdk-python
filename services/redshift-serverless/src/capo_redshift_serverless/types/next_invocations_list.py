"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#NextInvocationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import datetime

NextInvocationsList: TypeAlias = list["datetime.datetime"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NextInvocationsList) -> list:
    import capo_redshift_serverless.types._prelude.timestamp

    out: list = []
    for item in value:
        out.append(
            capo_redshift_serverless.types._prelude.timestamp.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> NextInvocationsList:
    import capo_redshift_serverless.types._prelude.timestamp

    out: NextInvocationsList = []
    for item in data:
        out.append(
            capo_redshift_serverless.types._prelude.timestamp.deserialize_aws_json_1_1(
                item
            )
        )
    return out

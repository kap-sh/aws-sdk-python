"""Generated from Smithy shape ``com.amazonaws.redshiftdata#SqlParametersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_redshift_data.types.sql_parameter

SqlParametersList: TypeAlias = list[
    "aws_sdk_redshift_data.types.sql_parameter.SqlParameter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SqlParametersList) -> list:
    import aws_sdk_redshift_data.types.sql_parameter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_redshift_data.types.sql_parameter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SqlParametersList:
    import aws_sdk_redshift_data.types.sql_parameter

    out: SqlParametersList = []
    for item in data:
        out.append(
            aws_sdk_redshift_data.types.sql_parameter.deserialize_aws_json_1_1(item)
        )
    return out

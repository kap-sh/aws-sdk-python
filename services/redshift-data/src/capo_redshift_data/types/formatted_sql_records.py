"""Generated from Smithy shape ``com.amazonaws.redshiftdata#FormattedSqlRecords``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_redshift_data.types.query_records

FormattedSqlRecords: TypeAlias = list[
    "capo_redshift_data.types.query_records.QueryRecords"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FormattedSqlRecords) -> list:
    import capo_redshift_data.types.query_records

    out: list = []
    for item in value:
        out.append(capo_redshift_data.types.query_records.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FormattedSqlRecords:
    import capo_redshift_data.types.query_records

    out: FormattedSqlRecords = []
    for item in data:
        out.append(
            capo_redshift_data.types.query_records.deserialize_aws_json_1_1(item)
        )
    return out

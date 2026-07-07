"""Generated from Smithy shape ``com.amazonaws.quicksight#PhysicalTable``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.custom_sql
    import aws_sdk_quicksight.types.relational_table
    import aws_sdk_quicksight.types.s3_source
    import aws_sdk_quicksight.types.saa_s_table


class _PhysicalTable_RelationalTable(TypedDict, closed=True):
    RelationalTable: "aws_sdk_quicksight.types.relational_table.RelationalTable"


class _PhysicalTable_CustomSql(TypedDict, closed=True):
    CustomSql: "aws_sdk_quicksight.types.custom_sql.CustomSql"


class _PhysicalTable_S3Source(TypedDict, closed=True):
    S3Source: "aws_sdk_quicksight.types.s3_source.S3Source"


class _PhysicalTable_SaaSTable(TypedDict, closed=True):
    SaaSTable: "aws_sdk_quicksight.types.saa_s_table.SaaSTable"


PhysicalTable: TypeAlias = (
    _PhysicalTable_RelationalTable
    | _PhysicalTable_CustomSql
    | _PhysicalTable_S3Source
    | _PhysicalTable_SaaSTable
)


# --- restJson1 ser/de ---
def serialize_json(value: PhysicalTable) -> dict:
    if "RelationalTable" in value:
        import aws_sdk_quicksight.types.relational_table

        return {
            "RelationalTable": aws_sdk_quicksight.types.relational_table.serialize_json(
                value["RelationalTable"]
            )
        }
    elif "CustomSql" in value:
        import aws_sdk_quicksight.types.custom_sql

        return {
            "CustomSql": aws_sdk_quicksight.types.custom_sql.serialize_json(
                value["CustomSql"]
            )
        }
    elif "S3Source" in value:
        import aws_sdk_quicksight.types.s3_source

        return {
            "S3Source": aws_sdk_quicksight.types.s3_source.serialize_json(
                value["S3Source"]
            )
        }
    elif "SaaSTable" in value:
        import aws_sdk_quicksight.types.saa_s_table

        return {
            "SaaSTable": aws_sdk_quicksight.types.saa_s_table.serialize_json(
                value["SaaSTable"]
            )
        }
    else:
        raise SerializationError("PhysicalTable: no variant present")


def deserialize_json(data: dict) -> PhysicalTable:
    if "RelationalTable" in data:
        import aws_sdk_quicksight.types.relational_table

        return {
            "RelationalTable": aws_sdk_quicksight.types.relational_table.deserialize_json(
                data["RelationalTable"]
            )
        }
    elif "CustomSql" in data:
        import aws_sdk_quicksight.types.custom_sql

        return {
            "CustomSql": aws_sdk_quicksight.types.custom_sql.deserialize_json(
                data["CustomSql"]
            )
        }
    elif "S3Source" in data:
        import aws_sdk_quicksight.types.s3_source

        return {
            "S3Source": aws_sdk_quicksight.types.s3_source.deserialize_json(
                data["S3Source"]
            )
        }
    elif "SaaSTable" in data:
        import aws_sdk_quicksight.types.saa_s_table

        return {
            "SaaSTable": aws_sdk_quicksight.types.saa_s_table.deserialize_json(
                data["SaaSTable"]
            )
        }
    else:
        raise DeserializationError("PhysicalTable: no recognized variant key")

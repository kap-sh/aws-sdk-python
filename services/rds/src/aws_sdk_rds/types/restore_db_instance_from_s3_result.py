"""Generated from Smithy shape ``com.amazonaws.rds#RestoreDBInstanceFromS3Result``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.db_instance


class RestoreDBInstanceFromS3Result(TypedDict, closed=True):
    db_instance: NotRequired["aws_sdk_rds.types.db_instance.DBInstance"]


# --- awsQuery ser/de ---
def serialize_query(
    value: RestoreDBInstanceFromS3Result, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_instance" in value:
        import aws_sdk_rds.types.db_instance

        aws_sdk_rds.types.db_instance.serialize_query(
            value["db_instance"], pairs, f"{prefix}.DBInstance"
        )


def deserialize_query(el: Element) -> RestoreDBInstanceFromS3Result:
    out: RestoreDBInstanceFromS3Result = {}  # type: ignore[typeddict-item]
    child_db_instance = el.find("DBInstance")
    if child_db_instance is not None:
        import aws_sdk_rds.types.db_instance

        out["db_instance"] = aws_sdk_rds.types.db_instance.deserialize_query(
            child_db_instance
        )
    return out

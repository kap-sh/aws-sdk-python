"""Generated from Smithy shape ``com.amazonaws.rds#DescribeValidDBInstanceModificationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.valid_db_instance_modifications_message


class DescribeValidDBInstanceModificationsResult(TypedDict, closed=True):
    valid_db_instance_modifications_message: NotRequired[
        "aws_sdk_rds.types.valid_db_instance_modifications_message.ValidDBInstanceModificationsMessage"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeValidDBInstanceModificationsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "valid_db_instance_modifications_message" in value:
        import aws_sdk_rds.types.valid_db_instance_modifications_message

        aws_sdk_rds.types.valid_db_instance_modifications_message.serialize_query(
            value["valid_db_instance_modifications_message"],
            pairs,
            f"{prefix}.ValidDBInstanceModificationsMessage",
        )


def deserialize_query(el: Element) -> DescribeValidDBInstanceModificationsResult:
    out: DescribeValidDBInstanceModificationsResult = {}  # type: ignore[typeddict-item]
    child_valid_db_instance_modifications_message = el.find(
        "ValidDBInstanceModificationsMessage"
    )
    if child_valid_db_instance_modifications_message is not None:
        import aws_sdk_rds.types.valid_db_instance_modifications_message

        out["valid_db_instance_modifications_message"] = (
            aws_sdk_rds.types.valid_db_instance_modifications_message.deserialize_query(
                child_valid_db_instance_modifications_message
            )
        )
    return out

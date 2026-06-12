"""Generated from Smithy shape ``com.amazonaws.glue#UpdateIcebergTableInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.iceberg_table_update_list


class UpdateIcebergTableInput(TypedDict):
    updates: "aws_sdk_glue.types.iceberg_table_update_list.IcebergTableUpdateList"
    """<p>The list of table update operations that specify the changes to be made to the Iceberg table, including schema modifications, partition specifications, and table properties.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateIcebergTableInput) -> dict:
    out: dict = {}
    import aws_sdk_glue.types.iceberg_table_update_list

    out["Updates"] = (
        aws_sdk_glue.types.iceberg_table_update_list.serialize_aws_json_1_1(
            value["updates"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateIcebergTableInput:
    out: UpdateIcebergTableInput = {}  # type: ignore[typeddict-item]
    if "Updates" in data:
        import aws_sdk_glue.types.iceberg_table_update_list

        out["updates"] = (
            aws_sdk_glue.types.iceberg_table_update_list.deserialize_aws_json_1_1(
                data["Updates"]
            )
        )
    else:
        raise DeserializationError("UpdateIcebergTableInput.updates required")
    return out

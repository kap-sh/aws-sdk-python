"""Generated from Smithy shape ``com.amazonaws.glue#UpdateIcebergInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.update_iceberg_table_input


class UpdateIcebergInput(TypedDict, closed=True):
    update_iceberg_table_input: (
        "capo_glue.types.update_iceberg_table_input.UpdateIcebergTableInput"
    )
    """<p>The specific update operations to be applied to the Iceberg table, containing a list of updates that define the new state of the table including schema, partitions, and properties.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateIcebergInput) -> dict:
    out: dict = {}
    import capo_glue.types.update_iceberg_table_input

    out["UpdateIcebergTableInput"] = (
        capo_glue.types.update_iceberg_table_input.serialize_aws_json_1_1(
            value["update_iceberg_table_input"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateIcebergInput:
    out: UpdateIcebergInput = {}  # type: ignore[typeddict-item]
    if "UpdateIcebergTableInput" in data:
        import capo_glue.types.update_iceberg_table_input

        out["update_iceberg_table_input"] = (
            capo_glue.types.update_iceberg_table_input.deserialize_aws_json_1_1(
                data["UpdateIcebergTableInput"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateIcebergInput.update_iceberg_table_input required"
        )
    return out

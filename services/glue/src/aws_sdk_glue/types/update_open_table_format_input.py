"""Generated from Smithy shape ``com.amazonaws.glue#UpdateOpenTableFormatInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.update_iceberg_input


class UpdateOpenTableFormatInput(TypedDict, closed=True):
    update_iceberg_input: NotRequired[
        "aws_sdk_glue.types.update_iceberg_input.UpdateIcebergInput"
    ]
    """<p>Apache Iceberg-specific update parameters that define the table modifications to be applied, including schema changes, partition specifications, and table properties.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateOpenTableFormatInput) -> dict:
    out: dict = {}
    if "update_iceberg_input" in value:
        import aws_sdk_glue.types.update_iceberg_input

        out["UpdateIcebergInput"] = (
            aws_sdk_glue.types.update_iceberg_input.serialize_aws_json_1_1(
                value["update_iceberg_input"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateOpenTableFormatInput:
    out: UpdateOpenTableFormatInput = {}  # type: ignore[typeddict-item]
    if "UpdateIcebergInput" in data:
        import aws_sdk_glue.types.update_iceberg_input

        out["update_iceberg_input"] = (
            aws_sdk_glue.types.update_iceberg_input.deserialize_aws_json_1_1(
                data["UpdateIcebergInput"]
            )
        )
    return out

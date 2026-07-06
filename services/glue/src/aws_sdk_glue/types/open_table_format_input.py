"""Generated from Smithy shape ``com.amazonaws.glue#OpenTableFormatInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.iceberg_input


class OpenTableFormatInput(TypedDict, closed=True):
    iceberg_input: NotRequired["aws_sdk_glue.types.iceberg_input.IcebergInput"]
    """<p>Specifies an <code>IcebergInput</code> structure that defines an Apache Iceberg metadata table.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpenTableFormatInput) -> dict:
    out: dict = {}
    if "iceberg_input" in value:
        import aws_sdk_glue.types.iceberg_input

        out["IcebergInput"] = aws_sdk_glue.types.iceberg_input.serialize_aws_json_1_1(
            value["iceberg_input"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OpenTableFormatInput:
    out: OpenTableFormatInput = {}  # type: ignore[typeddict-item]
    if "IcebergInput" in data:
        import aws_sdk_glue.types.iceberg_input

        out["iceberg_input"] = (
            aws_sdk_glue.types.iceberg_input.deserialize_aws_json_1_1(
                data["IcebergInput"]
            )
        )
    return out

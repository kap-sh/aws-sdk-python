"""Generated from Smithy shape ``com.amazonaws.glue#CompactionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.iceberg_compaction_configuration


class CompactionConfiguration(TypedDict, closed=True):
    iceberg_configuration: NotRequired[
        "aws_sdk_glue.types.iceberg_compaction_configuration.IcebergCompactionConfiguration"
    ]
    """<p>The configuration for an Iceberg compaction optimizer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CompactionConfiguration) -> dict:
    out: dict = {}
    if "iceberg_configuration" in value:
        import aws_sdk_glue.types.iceberg_compaction_configuration

        out["icebergConfiguration"] = (
            aws_sdk_glue.types.iceberg_compaction_configuration.serialize_aws_json_1_1(
                value["iceberg_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CompactionConfiguration:
    out: CompactionConfiguration = {}  # type: ignore[typeddict-item]
    if "icebergConfiguration" in data:
        import aws_sdk_glue.types.iceberg_compaction_configuration

        out["iceberg_configuration"] = (
            aws_sdk_glue.types.iceberg_compaction_configuration.deserialize_aws_json_1_1(
                data["icebergConfiguration"]
            )
        )
    return out

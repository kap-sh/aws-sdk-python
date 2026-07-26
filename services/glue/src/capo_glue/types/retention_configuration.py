"""Generated from Smithy shape ``com.amazonaws.glue#RetentionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.iceberg_retention_configuration


class RetentionConfiguration(TypedDict, closed=True):
    iceberg_configuration: NotRequired[
        "capo_glue.types.iceberg_retention_configuration.IcebergRetentionConfiguration"
    ]
    """<p>The configuration for an Iceberg snapshot retention optimizer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RetentionConfiguration) -> dict:
    out: dict = {}
    if "iceberg_configuration" in value:
        import capo_glue.types.iceberg_retention_configuration

        out["icebergConfiguration"] = (
            capo_glue.types.iceberg_retention_configuration.serialize_aws_json_1_1(
                value["iceberg_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RetentionConfiguration:
    out: RetentionConfiguration = {}  # type: ignore[typeddict-item]
    if "icebergConfiguration" in data:
        import capo_glue.types.iceberg_retention_configuration

        out["iceberg_configuration"] = (
            capo_glue.types.iceberg_retention_configuration.deserialize_aws_json_1_1(
                data["icebergConfiguration"]
            )
        )
    return out

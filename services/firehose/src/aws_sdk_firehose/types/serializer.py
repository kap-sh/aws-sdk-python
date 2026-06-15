"""Generated from Smithy shape ``com.amazonaws.firehose#Serializer``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_firehose.types.orc_ser_de
    import aws_sdk_firehose.types.parquet_ser_de


class Serializer(TypedDict):
    parquet_ser_de: NotRequired["aws_sdk_firehose.types.parquet_ser_de.ParquetSerDe"]
    r"""<p>A serializer to use for converting data to the Parquet format before storing it in Amazon S3. For more information, see <a href=\"https://parquet.apache.org/docs/contribution-guidelines/\">Apache Parquet</a>.</p>"""
    orc_ser_de: NotRequired["aws_sdk_firehose.types.orc_ser_de.OrcSerDe"]
    r"""<p>A serializer to use for converting data to the ORC format before storing it in Amazon S3. For more information, see <a href=\"https://orc.apache.org/docs/\">Apache ORC</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Serializer) -> dict:
    out: dict = {}
    if "parquet_ser_de" in value:
        import aws_sdk_firehose.types.parquet_ser_de

        out["ParquetSerDe"] = (
            aws_sdk_firehose.types.parquet_ser_de.serialize_aws_json_1_1(
                value["parquet_ser_de"]
            )
        )
    if "orc_ser_de" in value:
        import aws_sdk_firehose.types.orc_ser_de

        out["OrcSerDe"] = aws_sdk_firehose.types.orc_ser_de.serialize_aws_json_1_1(
            value["orc_ser_de"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Serializer:
    out: Serializer = {}  # type: ignore[typeddict-item]
    if "ParquetSerDe" in data:
        import aws_sdk_firehose.types.parquet_ser_de

        out["parquet_ser_de"] = (
            aws_sdk_firehose.types.parquet_ser_de.deserialize_aws_json_1_1(
                data["ParquetSerDe"]
            )
        )
    if "OrcSerDe" in data:
        import aws_sdk_firehose.types.orc_ser_de

        out["orc_ser_de"] = aws_sdk_firehose.types.orc_ser_de.deserialize_aws_json_1_1(
            data["OrcSerDe"]
        )
    return out

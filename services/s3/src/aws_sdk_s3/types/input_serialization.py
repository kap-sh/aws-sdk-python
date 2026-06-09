"""Generated from Smithy shape ``com.amazonaws.s3#InputSerialization``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.compression_type
    import aws_sdk_s3.types.csv_input
    import aws_sdk_s3.types.json_input
    import aws_sdk_s3.types.parquet_input


class InputSerialization(TypedDict):
    csv: NotRequired["aws_sdk_s3.types.csv_input.CSVInput"]
    """<p>Describes the serialization of a CSV-encoded object.</p>"""
    compression_type: NotRequired["aws_sdk_s3.types.compression_type.CompressionType"]
    """<p>Specifies object's compression format. Valid values: NONE, GZIP, BZIP2. Default Value: NONE.</p>"""
    json: NotRequired["aws_sdk_s3.types.json_input.JSONInput"]
    """<p>Specifies JSON as object's input serialization format.</p>"""
    parquet: NotRequired["aws_sdk_s3.types.parquet_input.ParquetInput"]
    """<p>Specifies Parquet as object's input serialization format.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: InputSerialization, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "csv" in value:
        import aws_sdk_s3.types.csv_input

        aws_sdk_s3.types.csv_input.serialize_xml(value["csv"], el, "CSV")
    if "compression_type" in value:
        import aws_sdk_s3.types.compression_type

        aws_sdk_s3.types.compression_type.serialize_xml(
            value["compression_type"], el, "CompressionType"
        )
    if "json" in value:
        import aws_sdk_s3.types.json_input

        aws_sdk_s3.types.json_input.serialize_xml(value["json"], el, "JSON")
    if "parquet" in value:
        import aws_sdk_s3.types.parquet_input

        aws_sdk_s3.types.parquet_input.serialize_xml(value["parquet"], el, "Parquet")


def deserialize_xml(el: Element) -> InputSerialization:
    out: InputSerialization = {}  # type: ignore[typeddict-item]
    child_csv = el.find("CSV")
    if child_csv is not None:
        import aws_sdk_s3.types.csv_input

        out["csv"] = aws_sdk_s3.types.csv_input.deserialize_xml(child_csv)
    child_compression_type = el.find("CompressionType")
    if child_compression_type is not None:
        import aws_sdk_s3.types.compression_type

        out["compression_type"] = aws_sdk_s3.types.compression_type.deserialize_xml(
            child_compression_type
        )
    child_json = el.find("JSON")
    if child_json is not None:
        import aws_sdk_s3.types.json_input

        out["json"] = aws_sdk_s3.types.json_input.deserialize_xml(child_json)
    child_parquet = el.find("Parquet")
    if child_parquet is not None:
        import aws_sdk_s3.types.parquet_input

        out["parquet"] = aws_sdk_s3.types.parquet_input.deserialize_xml(child_parquet)
    return out

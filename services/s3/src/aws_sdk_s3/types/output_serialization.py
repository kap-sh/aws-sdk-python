"""Generated from Smithy shape ``com.amazonaws.s3#OutputSerialization``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.csv_output
    import aws_sdk_s3.types.json_output


class OutputSerialization(TypedDict):
    csv: NotRequired["aws_sdk_s3.types.csv_output.CSVOutput"]
    """<p>Describes the serialization of CSV-encoded Select results.</p>"""
    json: NotRequired["aws_sdk_s3.types.json_output.JSONOutput"]
    """<p>Specifies JSON as request's output serialization format.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: OutputSerialization, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "csv" in value:
        import aws_sdk_s3.types.csv_output

        aws_sdk_s3.types.csv_output.serialize_xml(value["csv"], el, "CSV")
    if "json" in value:
        import aws_sdk_s3.types.json_output

        aws_sdk_s3.types.json_output.serialize_xml(value["json"], el, "JSON")


def deserialize_xml(el: Element) -> OutputSerialization:
    out: OutputSerialization = {}  # type: ignore[typeddict-item]
    child_csv = el.find("CSV")
    if child_csv is not None:
        import aws_sdk_s3.types.csv_output

        out["csv"] = aws_sdk_s3.types.csv_output.deserialize_xml(child_csv)
    child_json = el.find("JSON")
    if child_json is not None:
        import aws_sdk_s3.types.json_output

        out["json"] = aws_sdk_s3.types.json_output.deserialize_xml(child_json)
    return out

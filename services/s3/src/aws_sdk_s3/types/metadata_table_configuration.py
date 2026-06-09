"""Generated from Smithy shape ``com.amazonaws.s3#MetadataTableConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3.types.s3_tables_destination


class MetadataTableConfiguration(TypedDict):
    s3_tables_destination: "aws_sdk_s3.types.s3_tables_destination.S3TablesDestination"
    """<p> The destination information for the metadata table configuration. The destination table bucket must be in the same Region and Amazon Web Services account as the general purpose bucket. The specified metadata table name must be unique within the <code>aws_s3_metadata</code> namespace in the destination table bucket. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: MetadataTableConfiguration, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_s3.types.s3_tables_destination

    aws_sdk_s3.types.s3_tables_destination.serialize_xml(
        value["s3_tables_destination"], el, "S3TablesDestination"
    )


def deserialize_xml(el: Element) -> MetadataTableConfiguration:
    out: MetadataTableConfiguration = {}  # type: ignore[typeddict-item]
    child_s3_tables_destination = el.find("S3TablesDestination")
    if child_s3_tables_destination is not None:
        import aws_sdk_s3.types.s3_tables_destination

        out["s3_tables_destination"] = (
            aws_sdk_s3.types.s3_tables_destination.deserialize_xml(
                child_s3_tables_destination
            )
        )
    else:
        raise DeserializationError(
            "MetadataTableConfiguration.s3_tables_destination required"
        )
    return out

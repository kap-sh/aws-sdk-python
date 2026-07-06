"""Generated from Smithy shape ``com.amazonaws.s3#MetadataTableConfigurationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3.types.s3_tables_destination_result


class MetadataTableConfigurationResult(TypedDict, closed=True):
    s3_tables_destination_result: (
        "aws_sdk_s3.types.s3_tables_destination_result.S3TablesDestinationResult"
    )
    """<p> The destination information for the metadata table configuration. The destination table bucket must be in the same Region and Amazon Web Services account as the general purpose bucket. The specified metadata table name must be unique within the <code>aws_s3_metadata</code> namespace in the destination table bucket. </p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: MetadataTableConfigurationResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_s3.types.s3_tables_destination_result

    aws_sdk_s3.types.s3_tables_destination_result.serialize_xml(
        value["s3_tables_destination_result"], el, "S3TablesDestinationResult"
    )


def deserialize_xml(el: Element) -> MetadataTableConfigurationResult:
    out: MetadataTableConfigurationResult = {}  # type: ignore[typeddict-item]
    child_s3_tables_destination_result = el.find("S3TablesDestinationResult")
    if child_s3_tables_destination_result is not None:
        import aws_sdk_s3.types.s3_tables_destination_result

        out["s3_tables_destination_result"] = (
            aws_sdk_s3.types.s3_tables_destination_result.deserialize_xml(
                child_s3_tables_destination_result
            )
        )
    else:
        raise DeserializationError(
            "MetadataTableConfigurationResult.s3_tables_destination_result required"
        )
    return out

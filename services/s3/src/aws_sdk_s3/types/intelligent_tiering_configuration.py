"""Generated from Smithy shape ``com.amazonaws.s3#IntelligentTieringConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3.types.intelligent_tiering_filter
    import aws_sdk_s3.types.intelligent_tiering_id
    import aws_sdk_s3.types.intelligent_tiering_status
    import aws_sdk_s3.types.tiering_list


class IntelligentTieringConfiguration(TypedDict, closed=True):
    id: "aws_sdk_s3.types.intelligent_tiering_id.IntelligentTieringId"
    """<p>The ID used to identify the S3 Intelligent-Tiering configuration.</p>"""
    filter: NotRequired[
        "aws_sdk_s3.types.intelligent_tiering_filter.IntelligentTieringFilter"
    ]
    """<p>Specifies a bucket filter. The configuration only includes objects that meet the filter's criteria.</p>"""
    status: "aws_sdk_s3.types.intelligent_tiering_status.IntelligentTieringStatus"
    """<p>Specifies the status of the configuration.</p>"""
    tierings: "aws_sdk_s3.types.tiering_list.TieringList"
    """<p>Specifies the S3 Intelligent-Tiering storage class tier of the configuration.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: IntelligentTieringConfiguration, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    if "filter" in value:
        import aws_sdk_s3.types.intelligent_tiering_filter

        aws_sdk_s3.types.intelligent_tiering_filter.serialize_xml(
            value["filter"], el, "Filter"
        )
    import aws_sdk_s3.types.intelligent_tiering_status

    aws_sdk_s3.types.intelligent_tiering_status.serialize_xml(
        value["status"], el, "Status"
    )
    import aws_sdk_s3.types.tiering_list

    aws_sdk_s3.types.tiering_list.serialize_xml_flat(value["tierings"], el, "Tiering")


def deserialize_xml(el: Element) -> IntelligentTieringConfiguration:
    out: IntelligentTieringConfiguration = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        raise DeserializationError("IntelligentTieringConfiguration.id required")
    child_filter = el.find("Filter")
    if child_filter is not None:
        import aws_sdk_s3.types.intelligent_tiering_filter

        out["filter"] = aws_sdk_s3.types.intelligent_tiering_filter.deserialize_xml(
            child_filter
        )
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_s3.types.intelligent_tiering_status

        out["status"] = aws_sdk_s3.types.intelligent_tiering_status.deserialize_xml(
            child_status
        )
    else:
        raise DeserializationError("IntelligentTieringConfiguration.status required")
    if el.find("Tiering") is not None:
        import aws_sdk_s3.types.tiering_list

        out["tierings"] = aws_sdk_s3.types.tiering_list.deserialize_xml_flat(
            el, "Tiering"
        )
    else:
        raise DeserializationError("IntelligentTieringConfiguration.tierings required")
    return out

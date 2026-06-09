"""Generated from Smithy shape ``com.amazonaws.s3#GetObjectAttributesParts``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.is_truncated
    import aws_sdk_s3.types.max_parts
    import aws_sdk_s3.types.next_part_number_marker
    import aws_sdk_s3.types.part_number_marker
    import aws_sdk_s3.types.parts_count
    import aws_sdk_s3.types.parts_list


class GetObjectAttributesParts(TypedDict):
    total_parts_count: NotRequired["aws_sdk_s3.types.parts_count.PartsCount"]
    """<p>The total number of parts.</p>"""
    part_number_marker: NotRequired[
        "aws_sdk_s3.types.part_number_marker.PartNumberMarker"
    ]
    """<p>The marker for the current part.</p>"""
    next_part_number_marker: NotRequired[
        "aws_sdk_s3.types.next_part_number_marker.NextPartNumberMarker"
    ]
    """<p>When a list is truncated, this element specifies the last part in the list, as well as the value to use for the <code>PartNumberMarker</code> request parameter in a subsequent request.</p>"""
    max_parts: NotRequired["aws_sdk_s3.types.max_parts.MaxParts"]
    """<p>The maximum number of parts allowed in the response.</p>"""
    is_truncated: NotRequired["aws_sdk_s3.types.is_truncated.IsTruncated"]
    """<p>Indicates whether the returned list of parts is truncated. A value of <code>true</code> indicates that the list was truncated. A list can be truncated if the number of parts exceeds the limit returned in the <code>MaxParts</code> element.</p>"""
    parts: NotRequired["aws_sdk_s3.types.parts_list.PartsList"]
    """<p>A container for elements related to a particular part. A response can contain zero or more <code>Parts</code> elements.</p> <note> <ul> <li> <p> <b>General purpose buckets</b> - For <code>GetObjectAttributes</code>, if an additional checksum (including <code>x-amz-checksum-crc32</code>, <code>x-amz-checksum-crc32c</code>, <code>x-amz-checksum-sha1</code>, or <code>x-amz-checksum-sha256</code>) isn't applied to the object specified in the request, the response doesn't return the <code>Part</code> element.</p> </li> <li> <p> <b>Directory buckets</b> - For <code>GetObjectAttributes</code>, regardless of whether an additional checksum is applied to the object specified in the request, the response returns the <code>Part</code> element.</p> </li> </ul> </note>"""


# --- restXml ser/de ---
def serialize_xml(value: GetObjectAttributesParts, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "total_parts_count" in value:
        SubElement(el, "PartsCount").text = str(value["total_parts_count"])
    if "part_number_marker" in value:
        SubElement(el, "PartNumberMarker").text = str(value["part_number_marker"])
    if "next_part_number_marker" in value:
        SubElement(el, "NextPartNumberMarker").text = str(
            value["next_part_number_marker"]
        )
    if "max_parts" in value:
        SubElement(el, "MaxParts").text = str(value["max_parts"])
    if "is_truncated" in value:
        SubElement(el, "IsTruncated").text = (
            "true" if value["is_truncated"] else "false"
        )
    if "parts" in value:
        import aws_sdk_s3.types.parts_list

        aws_sdk_s3.types.parts_list.serialize_xml_flat(value["parts"], el, "Part")


def deserialize_xml(el: Element) -> GetObjectAttributesParts:
    out: GetObjectAttributesParts = {}  # type: ignore[typeddict-item]
    child_total_parts_count = el.find("PartsCount")
    if child_total_parts_count is not None:
        out["total_parts_count"] = int(child_total_parts_count.text or "")
    child_part_number_marker = el.find("PartNumberMarker")
    if child_part_number_marker is not None:
        out["part_number_marker"] = str(child_part_number_marker.text or "")
    child_next_part_number_marker = el.find("NextPartNumberMarker")
    if child_next_part_number_marker is not None:
        out["next_part_number_marker"] = str(child_next_part_number_marker.text or "")
    child_max_parts = el.find("MaxParts")
    if child_max_parts is not None:
        out["max_parts"] = int(child_max_parts.text or "")
    child_is_truncated = el.find("IsTruncated")
    if child_is_truncated is not None:
        out["is_truncated"] = (child_is_truncated.text or "").lower() == "true"
    if el.find("Part") is not None:
        import aws_sdk_s3.types.parts_list

        out["parts"] = aws_sdk_s3.types.parts_list.deserialize_xml_flat(el, "Part")
    return out

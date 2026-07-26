"""Generated from Smithy shape ``com.amazonaws.s3#BucketInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.bucket_type
    import capo_s3.types.data_redundancy


class BucketInfo(TypedDict, closed=True):
    data_redundancy: NotRequired["capo_s3.types.data_redundancy.DataRedundancy"]
    """<p>The number of Zone (Availability Zone or Local Zone) that's used for redundancy for the bucket.</p>"""
    type: NotRequired["capo_s3.types.bucket_type.BucketType"]
    """<p>The type of bucket.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: BucketInfo, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "data_redundancy" in value:
        import capo_s3.types.data_redundancy

        capo_s3.types.data_redundancy.serialize_xml(
            value["data_redundancy"], el, "DataRedundancy"
        )
    if "type" in value:
        import capo_s3.types.bucket_type

        capo_s3.types.bucket_type.serialize_xml(value["type"], el, "Type")


def deserialize_xml(el: Element) -> BucketInfo:
    out: BucketInfo = {}  # type: ignore[typeddict-item]
    child_data_redundancy = el.find("DataRedundancy")
    if child_data_redundancy is not None:
        import capo_s3.types.data_redundancy

        out["data_redundancy"] = capo_s3.types.data_redundancy.deserialize_xml(
            child_data_redundancy
        )
    child_type = el.find("Type")
    if child_type is not None:
        import capo_s3.types.bucket_type

        out["type"] = capo_s3.types.bucket_type.deserialize_xml(child_type)
    return out

"""Generated from Smithy shape ``com.amazonaws.cloudfront#AliasICPRecordal``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.icp_recordal_status
    import aws_sdk_cloudfront.types.string


class AliasICPRecordal(TypedDict):
    cname: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>A domain name associated with a distribution.</p>"""
    icp_recordal_status: NotRequired[
        "aws_sdk_cloudfront.types.icp_recordal_status.ICPRecordalStatus"
    ]
    """<p>The Internet Content Provider (ICP) recordal status for a CNAME. The ICPRecordalStatus is set to APPROVED for all CNAMEs (aliases) in Amazon Web Services Regions outside of China.</p> <p>The status values returned are the following:</p> <ul> <li> <p> <b>APPROVED</b> indicates that the associated CNAME has a valid ICP recordal number. Multiple CNAMEs can be associated with a distribution, and CNAMEs can correspond to different ICP recordals. To be marked as APPROVED, that is, valid to use with the China Regions, a CNAME must have one ICP recordal number associated with it.</p> </li> <li> <p> <b>SUSPENDED</b> indicates that the associated CNAME does not have a valid ICP recordal number.</p> </li> <li> <p> <b>PENDING</b> indicates that CloudFront can't determine the ICP recordal status of the CNAME associated with the distribution because there was an error in trying to determine the status. You can try again to see if the error is resolved in which case CloudFront returns an APPROVED or SUSPENDED status.</p> </li> </ul>"""


# --- restXml ser/de ---
def serialize_xml(value: AliasICPRecordal, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "cname" in value:
        SubElement(el, "CNAME").text = str(value["cname"])
    if "icp_recordal_status" in value:
        import aws_sdk_cloudfront.types.icp_recordal_status

        aws_sdk_cloudfront.types.icp_recordal_status.serialize_xml(
            value["icp_recordal_status"], el, "ICPRecordalStatus"
        )


def deserialize_xml(el: Element) -> AliasICPRecordal:
    out: AliasICPRecordal = {}  # type: ignore[typeddict-item]
    child_cname = el.find("CNAME")
    if child_cname is not None:
        out["cname"] = str(child_cname.text or "")
    child_icp_recordal_status = el.find("ICPRecordalStatus")
    if child_icp_recordal_status is not None:
        import aws_sdk_cloudfront.types.icp_recordal_status

        out["icp_recordal_status"] = (
            aws_sdk_cloudfront.types.icp_recordal_status.deserialize_xml(
                child_icp_recordal_status
            )
        )
    return out

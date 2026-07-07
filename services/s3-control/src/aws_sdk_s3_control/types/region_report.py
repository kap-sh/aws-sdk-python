"""Generated from Smithy shape ``com.amazonaws.s3control#RegionReport``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.account_id
    import aws_sdk_s3_control.types.bucket_name
    import aws_sdk_s3_control.types.region_name


class RegionReport(TypedDict, closed=True):
    bucket: NotRequired["aws_sdk_s3_control.types.bucket_name.BucketName"]
    """<p>The name of the bucket.</p>"""
    region: NotRequired["aws_sdk_s3_control.types.region_name.RegionName"]
    """<p>The name of the Region.</p>"""
    bucket_account_id: NotRequired["aws_sdk_s3_control.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID that owns the Amazon S3 bucket that's associated with this Multi-Region Access Point.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: RegionReport, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "bucket" in value:
        SubElement(el, "Bucket").text = str(value["bucket"])
    if "region" in value:
        SubElement(el, "Region").text = str(value["region"])
    if "bucket_account_id" in value:
        SubElement(el, "BucketAccountId").text = str(value["bucket_account_id"])


def deserialize_xml(el: Element) -> RegionReport:
    out: RegionReport = {}  # type: ignore[typeddict-item]
    child_bucket = el.find("Bucket")
    if child_bucket is not None:
        out["bucket"] = str(child_bucket.text or "")
    child_region = el.find("Region")
    if child_region is not None:
        out["region"] = str(child_region.text or "")
    child_bucket_account_id = el.find("BucketAccountId")
    if child_bucket_account_id is not None:
        out["bucket_account_id"] = str(child_bucket_account_id.text or "")
    return out

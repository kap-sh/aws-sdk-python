"""Generated from Smithy shape ``com.amazonaws.cloudfront#LoggingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.boolean
    import capo_cloudfront.types.string


class LoggingConfig(TypedDict, closed=True):
    enabled: "capo_cloudfront.types.boolean.boolean"
    """<p>Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you don't want to enable logging when you create a distribution or if you want to disable logging for an existing distribution, specify <code>false</code> for <code>Enabled</code>, and specify empty <code>Bucket</code> and <code>Prefix</code> elements. If you specify <code>false</code> for <code>Enabled</code> but you specify values for <code>Bucket</code> and <code>prefix</code>, the values are automatically deleted.</p>"""
    include_cookies: "capo_cloudfront.types.boolean.boolean"
    """<p>Specifies whether you want CloudFront to include cookies in access logs, specify <code>true</code> for <code>IncludeCookies</code>. If you choose to include cookies in logs, CloudFront logs all cookies regardless of how you configure the cache behaviors for this distribution. If you don't want to include cookies when you create a distribution or if you want to disable include cookies for an existing distribution, specify <code>false</code> for <code>IncludeCookies</code>.</p>"""
    bucket: "capo_cloudfront.types.string.string"
    """<p>The Amazon S3 bucket to store the access logs in, for example, <code>amzn-s3-demo-bucket.s3.amazonaws.com</code>.</p>"""
    prefix: "capo_cloudfront.types.string.string"
    """<p>An optional string that you want CloudFront to prefix to the access log <code>filenames</code> for this distribution, for example, <code>myprefix/</code>. If you want to enable logging, but you don't want to specify a prefix, you still must include an empty <code>Prefix</code> element in the <code>Logging</code> element.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: LoggingConfig, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Enabled").text = "true" if value.get("enabled", False) else "false"
    SubElement(el, "IncludeCookies").text = (
        "true" if value.get("include_cookies", False) else "false"
    )
    SubElement(el, "Bucket").text = str(value.get("bucket", ""))
    SubElement(el, "Prefix").text = str(value.get("prefix", ""))


def deserialize_xml(el: Element) -> LoggingConfig:
    out: LoggingConfig = {}  # type: ignore[typeddict-item]
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    else:
        out["enabled"] = False
    child_include_cookies = el.find("IncludeCookies")
    if child_include_cookies is not None:
        out["include_cookies"] = (child_include_cookies.text or "").lower() == "true"
    else:
        out["include_cookies"] = False
    child_bucket = el.find("Bucket")
    if child_bucket is not None:
        out["bucket"] = str(child_bucket.text or "")
    else:
        out["bucket"] = ""
    child_prefix = el.find("Prefix")
    if child_prefix is not None:
        out["prefix"] = str(child_prefix.text or "")
    else:
        out["prefix"] = ""
    return out

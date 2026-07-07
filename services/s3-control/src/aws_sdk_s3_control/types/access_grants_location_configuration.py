"""Generated from Smithy shape ``com.amazonaws.s3control#AccessGrantsLocationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.s3_prefix


class AccessGrantsLocationConfiguration(TypedDict, closed=True):
    s3_sub_prefix: NotRequired["aws_sdk_s3_control.types.s3_prefix.S3Prefix"]
    """<p>The <code>S3SubPrefix</code> is appended to the location scope creating the grant scope. Use this field to narrow the scope of the grant to a subset of the location scope. This field is required if the location scope is the default location <code>s3://</code> because you cannot create a grant for all of your S3 data in the Region and must narrow the scope. For example, if the location scope is the default location <code>s3://</code>, the <code>S3SubPrefx</code> can be a <bucket-name>/*, so the full grant scope path would be <code>s3://<bucket-name>/*</code>. Or the <code>S3SubPrefx</code> can be <code><bucket-name>/<prefix-name>*</code>, so the full grant scope path would be or <code>s3://<bucket-name>/<prefix-name>*</code>.</p> <p>If the <code>S3SubPrefix</code> includes a prefix, append the wildcard character <code>*</code> after the prefix to indicate that you want to include all object key names in the bucket that start with that prefix. </p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: AccessGrantsLocationConfiguration, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "s3_sub_prefix" in value:
        SubElement(el, "S3SubPrefix").text = str(value["s3_sub_prefix"])


def deserialize_xml(el: Element) -> AccessGrantsLocationConfiguration:
    out: AccessGrantsLocationConfiguration = {}  # type: ignore[typeddict-item]
    child_s3_sub_prefix = el.find("S3SubPrefix")
    if child_s3_sub_prefix is not None:
        out["s3_sub_prefix"] = str(child_s3_sub_prefix.text or "")
    return out

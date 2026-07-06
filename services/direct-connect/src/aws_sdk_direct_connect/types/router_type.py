"""Generated from Smithy shape ``com.amazonaws.directconnect#RouterType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.platform
    import aws_sdk_direct_connect.types.router_type_identifier
    import aws_sdk_direct_connect.types.software
    import aws_sdk_direct_connect.types.vendor
    import aws_sdk_direct_connect.types.xslt_template_name
    import aws_sdk_direct_connect.types.xslt_template_name_for_mac_sec


class RouterType(TypedDict, closed=True):
    vendor: NotRequired["aws_sdk_direct_connect.types.vendor.Vendor"]
    """<p>The vendor for the virtual interface's router.</p>"""
    platform: NotRequired["aws_sdk_direct_connect.types.platform.Platform"]
    """<p>The virtual interface router platform.</p>"""
    software: NotRequired["aws_sdk_direct_connect.types.software.Software"]
    """<p>The router software. </p>"""
    xslt_template_name: NotRequired[
        "aws_sdk_direct_connect.types.xslt_template_name.XsltTemplateName"
    ]
    """<p>The template for the virtual interface's router.</p>"""
    xslt_template_name_for_mac_sec: NotRequired[
        "aws_sdk_direct_connect.types.xslt_template_name_for_mac_sec.XsltTemplateNameForMacSec"
    ]
    """<p>The MAC Security (MACsec) template for the virtual interface's router.</p>"""
    router_type_identifier: NotRequired[
        "aws_sdk_direct_connect.types.router_type_identifier.RouterTypeIdentifier"
    ]
    """<p>Identifies the router by a combination of vendor, platform, and software version. For example, <code>CiscoSystemsInc-2900SeriesRouters-IOS124</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RouterType) -> dict:
    out: dict = {}
    if "vendor" in value:
        out["vendor"] = value["vendor"]
    if "platform" in value:
        out["platform"] = value["platform"]
    if "software" in value:
        out["software"] = value["software"]
    if "xslt_template_name" in value:
        out["xsltTemplateName"] = value["xslt_template_name"]
    if "xslt_template_name_for_mac_sec" in value:
        out["xsltTemplateNameForMacSec"] = value["xslt_template_name_for_mac_sec"]
    if "router_type_identifier" in value:
        out["routerTypeIdentifier"] = value["router_type_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RouterType:
    out: RouterType = {}  # type: ignore[typeddict-item]
    if "vendor" in data:
        out["vendor"] = data["vendor"]
    if "platform" in data:
        out["platform"] = data["platform"]
    if "software" in data:
        out["software"] = data["software"]
    if "xsltTemplateName" in data:
        out["xslt_template_name"] = data["xsltTemplateName"]
    if "xsltTemplateNameForMacSec" in data:
        out["xslt_template_name_for_mac_sec"] = data["xsltTemplateNameForMacSec"]
    if "routerTypeIdentifier" in data:
        out["router_type_identifier"] = data["routerTypeIdentifier"]
    return out

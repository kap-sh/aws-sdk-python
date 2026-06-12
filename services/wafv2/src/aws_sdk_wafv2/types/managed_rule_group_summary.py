"""Generated from Smithy shape ``com.amazonaws.wafv2#ManagedRuleGroupSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.boolean
    import aws_sdk_wafv2.types.entity_description
    import aws_sdk_wafv2.types.entity_name
    import aws_sdk_wafv2.types.vendor_name


class ManagedRuleGroupSummary(TypedDict):
    vendor_name: NotRequired["aws_sdk_wafv2.types.vendor_name.VendorName"]
    """<p>The name of the managed rule group vendor. You use this, along with the rule group name, to identify a rule group.</p>"""
    name: NotRequired["aws_sdk_wafv2.types.entity_name.EntityName"]
    """<p>The name of the managed rule group. You use this, along with the vendor name, to identify the rule group.</p>"""
    versioning_supported: "aws_sdk_wafv2.types.boolean.Boolean"
    """<p>Indicates whether the managed rule group is versioned. If it is, you can retrieve the versions list by calling <a>ListAvailableManagedRuleGroupVersions</a>. </p>"""
    description: NotRequired["aws_sdk_wafv2.types.entity_description.EntityDescription"]
    """<p>The description of the managed rule group, provided by Amazon Web Services Managed Rules or the Amazon Web Services Marketplace seller who manages it.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedRuleGroupSummary) -> dict:
    out: dict = {}
    if "vendor_name" in value:
        out["VendorName"] = value["vendor_name"]
    if "name" in value:
        out["Name"] = value["name"]
    out["VersioningSupported"] = value.get("versioning_supported", False)
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedRuleGroupSummary:
    out: ManagedRuleGroupSummary = {}  # type: ignore[typeddict-item]
    if "VendorName" in data:
        out["vendor_name"] = data["VendorName"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "VersioningSupported" in data:
        out["versioning_supported"] = data["VersioningSupported"]
    else:
        out["versioning_supported"] = False
    if "Description" in data:
        out["description"] = data["Description"]
    return out

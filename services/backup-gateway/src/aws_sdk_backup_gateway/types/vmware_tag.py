"""Generated from Smithy shape ``com.amazonaws.backupgateway#VmwareTag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup_gateway.types.string
    import aws_sdk_backup_gateway.types.vmware_category
    import aws_sdk_backup_gateway.types.vmware_tag_name


class VmwareTag(TypedDict, closed=True):
    vmware_category: NotRequired[
        "aws_sdk_backup_gateway.types.vmware_category.VmwareCategory"
    ]
    """<p>The is the category of VMware.</p>"""
    vmware_tag_name: NotRequired[
        "aws_sdk_backup_gateway.types.vmware_tag_name.VmwareTagName"
    ]
    """<p>This is the user-defined name of a VMware tag.</p>"""
    vmware_tag_description: NotRequired["aws_sdk_backup_gateway.types.string.string"]
    """<p>This is a user-defined description of a VMware tag.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VmwareTag) -> dict:
    out: dict = {}
    if "vmware_category" in value:
        out["VmwareCategory"] = value["vmware_category"]
    if "vmware_tag_name" in value:
        out["VmwareTagName"] = value["vmware_tag_name"]
    if "vmware_tag_description" in value:
        out["VmwareTagDescription"] = value["vmware_tag_description"]
    return out


def deserialize_aws_json_1_0(data: dict) -> VmwareTag:
    out: VmwareTag = {}  # type: ignore[typeddict-item]
    if "VmwareCategory" in data:
        out["vmware_category"] = data["VmwareCategory"]
    if "VmwareTagName" in data:
        out["vmware_tag_name"] = data["VmwareTagName"]
    if "VmwareTagDescription" in data:
        out["vmware_tag_description"] = data["VmwareTagDescription"]
    return out

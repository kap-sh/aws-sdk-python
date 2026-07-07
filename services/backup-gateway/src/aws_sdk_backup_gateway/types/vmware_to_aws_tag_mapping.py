"""Generated from Smithy shape ``com.amazonaws.backupgateway#VmwareToAwsTagMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_backup_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_backup_gateway.types.tag_key
    import aws_sdk_backup_gateway.types.tag_value
    import aws_sdk_backup_gateway.types.vmware_category
    import aws_sdk_backup_gateway.types.vmware_tag_name


class VmwareToAwsTagMapping(TypedDict, closed=True):
    vmware_category: "aws_sdk_backup_gateway.types.vmware_category.VmwareCategory"
    """<p>The is the category of VMware.</p>"""
    vmware_tag_name: "aws_sdk_backup_gateway.types.vmware_tag_name.VmwareTagName"
    """<p>This is the user-defined name of a VMware tag.</p>"""
    aws_tag_key: "aws_sdk_backup_gateway.types.tag_key.TagKey"
    """<p>The key part of the Amazon Web Services tag's key-value pair.</p>"""
    aws_tag_value: "aws_sdk_backup_gateway.types.tag_value.TagValue"
    """<p>The value part of the Amazon Web Services tag's key-value pair.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VmwareToAwsTagMapping) -> dict:
    out: dict = {}
    out["VmwareCategory"] = value["vmware_category"]
    out["VmwareTagName"] = value["vmware_tag_name"]
    out["AwsTagKey"] = value["aws_tag_key"]
    out["AwsTagValue"] = value["aws_tag_value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> VmwareToAwsTagMapping:
    out: VmwareToAwsTagMapping = {}  # type: ignore[typeddict-item]
    if "VmwareCategory" in data:
        out["vmware_category"] = data["VmwareCategory"]
    else:
        raise DeserializationError("VmwareToAwsTagMapping.vmware_category required")
    if "VmwareTagName" in data:
        out["vmware_tag_name"] = data["VmwareTagName"]
    else:
        raise DeserializationError("VmwareToAwsTagMapping.vmware_tag_name required")
    if "AwsTagKey" in data:
        out["aws_tag_key"] = data["AwsTagKey"]
    else:
        raise DeserializationError("VmwareToAwsTagMapping.aws_tag_key required")
    if "AwsTagValue" in data:
        out["aws_tag_value"] = data["AwsTagValue"]
    else:
        raise DeserializationError("VmwareToAwsTagMapping.aws_tag_value required")
    return out

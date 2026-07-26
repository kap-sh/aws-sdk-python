"""Generated from Smithy shape ``com.amazonaws.imagebuilder#AmiDistributionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.account_list
    import capo_imagebuilder.types.ami_name_string
    import capo_imagebuilder.types.launch_permission_configuration
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.tag_map


class AmiDistributionConfiguration(TypedDict, closed=True):
    name: NotRequired["capo_imagebuilder.types.ami_name_string.AmiNameString"]
    """<p>The name of the output AMI.</p>"""
    description: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The description of the AMI distribution configuration. Minimum and maximum length are in characters.</p>"""
    target_account_ids: NotRequired["capo_imagebuilder.types.account_list.AccountList"]
    """<p>The ID of an account to which you want to distribute an image.</p>"""
    ami_tags: NotRequired["capo_imagebuilder.types.tag_map.TagMap"]
    """<p>The tags to apply to AMIs distributed to this Region.</p>"""
    kms_key_id: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    r"""<p>The Amazon Resource Name (ARN) that uniquely identifies the KMS key used to encrypt the distributed image. This can be either the Key ARN or the Alias ARN. For more information, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN\">Key identifiers (KeyId)</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    launch_permission: NotRequired[
        "capo_imagebuilder.types.launch_permission_configuration.LaunchPermissionConfiguration"
    ]
    """<p>Launch permissions can be used to configure which Amazon Web Services accounts can use the AMI to launch instances.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AmiDistributionConfiguration) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "target_account_ids" in value:
        import capo_imagebuilder.types.account_list

        out["targetAccountIds"] = capo_imagebuilder.types.account_list.serialize_json(
            value["target_account_ids"]
        )
    if "ami_tags" in value:
        import capo_imagebuilder.types.tag_map

        out["amiTags"] = capo_imagebuilder.types.tag_map.serialize_json(
            value["ami_tags"]
        )
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "launch_permission" in value:
        import capo_imagebuilder.types.launch_permission_configuration

        out["launchPermission"] = (
            capo_imagebuilder.types.launch_permission_configuration.serialize_json(
                value["launch_permission"]
            )
        )
    return out


def deserialize_json(data: dict) -> AmiDistributionConfiguration:
    out: AmiDistributionConfiguration = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "targetAccountIds" in data:
        import capo_imagebuilder.types.account_list

        out["target_account_ids"] = (
            capo_imagebuilder.types.account_list.deserialize_json(
                data["targetAccountIds"]
            )
        )
    if "amiTags" in data:
        import capo_imagebuilder.types.tag_map

        out["ami_tags"] = capo_imagebuilder.types.tag_map.deserialize_json(
            data["amiTags"]
        )
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    if "launchPermission" in data:
        import capo_imagebuilder.types.launch_permission_configuration

        out["launch_permission"] = (
            capo_imagebuilder.types.launch_permission_configuration.deserialize_json(
                data["launchPermission"]
            )
        )
    return out

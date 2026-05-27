"""Generated from Smithy shape ``com.amazonaws.ec2#NitroTpmInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.nitro_tpm_supported_versions_list


class NitroTpmInfo(TypedDict):
    supported_versions: NotRequired[
        "aws_sdk_ec2.types.nitro_tpm_supported_versions_list.NitroTpmSupportedVersionsList"
    ]
    """<p>Indicates the supported NitroTPM versions.</p>"""

"""Generated from Smithy shape ``com.amazonaws.ec2#FpgaImage``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.fpga_image_state
    import aws_sdk_ec2.types.instance_types_list
    import aws_sdk_ec2.types.pci_id
    import aws_sdk_ec2.types.product_code_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class FpgaImage(TypedDict):
    fpga_image_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The FPGA image identifier (AFI ID).</p>"""
    fpga_image_global_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The global FPGA image identifier (AGFI ID).</p>"""
    name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the AFI.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description of the AFI.</p>"""
    shell_version: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The version of the Amazon Web Services Shell that was used to create the bitstream.</p>"""
    pci_id: NotRequired["aws_sdk_ec2.types.pci_id.PciId"]
    """<p>Information about the PCI bus.</p>"""
    state: NotRequired["aws_sdk_ec2.types.fpga_image_state.FpgaImageState"]
    """<p>Information about the state of the AFI.</p>"""
    create_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The date and time the AFI was created.</p>"""
    update_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The time of the most recent update to the AFI.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the AFI.</p>"""
    owner_alias: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The alias of the AFI owner. Possible values include <code>self</code>, <code>amazon</code>, and <code>aws-marketplace</code>.</p>"""
    product_codes: NotRequired["aws_sdk_ec2.types.product_code_list.ProductCodeList"]
    """<p>The product codes for the AFI.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the AFI.</p>"""
    public: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the AFI is public.</p>"""
    data_retention_support: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether data retention support is enabled for the AFI.</p>"""
    instance_types: NotRequired[
        "aws_sdk_ec2.types.instance_types_list.InstanceTypesList"
    ]
    """<p>The instance types supported by the AFI.</p>"""

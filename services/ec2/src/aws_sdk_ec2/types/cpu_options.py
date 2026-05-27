"""Generated from Smithy shape ``com.amazonaws.ec2#CpuOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.amd_sev_snp_specification
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.nested_virtualization_specification


class CpuOptions(TypedDict):
    core_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of CPU cores for the instance.</p>"""
    threads_per_core: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of threads per CPU core.</p>"""
    amd_sev_snp: NotRequired[
        "aws_sdk_ec2.types.amd_sev_snp_specification.AmdSevSnpSpecification"
    ]
    """<p>Indicates whether the instance is enabled for AMD SEV-SNP. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sev-snp.html\">AMD SEV-SNP</a>.</p>"""
    nested_virtualization: NotRequired[
        "aws_sdk_ec2.types.nested_virtualization_specification.NestedVirtualizationSpecification"
    ]
    """<p>Indicates whether the instance is enabled for nested virtualization.</p>"""

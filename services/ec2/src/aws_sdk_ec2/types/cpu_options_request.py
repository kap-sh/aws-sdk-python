"""Generated from Smithy shape ``com.amazonaws.ec2#CpuOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.amd_sev_snp_specification
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.nested_virtualization_specification


class CpuOptionsRequest(TypedDict):
    core_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of CPU cores for the instance.</p>"""
    threads_per_core: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of threads per CPU core. To disable multithreading for the instance, specify a value of <code>1</code>. Otherwise, specify the default value of <code>2</code>.</p>"""
    amd_sev_snp: NotRequired[
        "aws_sdk_ec2.types.amd_sev_snp_specification.AmdSevSnpSpecification"
    ]
    """<p>Indicates whether to enable the instance for AMD SEV-SNP. AMD SEV-SNP is supported with M6a, R6a, and C6a instance types only. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sev-snp.html\">AMD SEV-SNP</a>.</p>"""
    nested_virtualization: NotRequired[
        "aws_sdk_ec2.types.nested_virtualization_specification.NestedVirtualizationSpecification"
    ]
    """<p>Indicates whether to enable the instance for nested virtualization. Nested virtualization is supported only on 8th generation Intel-based instance types (c8i, m8i, r8i, and their flex variants). When nested virtualization is enabled, Virtual Secure Mode (VSM) is automatically disabled for the instance.</p>"""

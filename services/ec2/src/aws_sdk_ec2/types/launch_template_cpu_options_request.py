"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateCpuOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.amd_sev_snp_specification
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.nested_virtualization_specification


class LaunchTemplateCpuOptionsRequest(TypedDict):
    core_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of CPU cores for the instance.</p>"""
    threads_per_core: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of threads per CPU core. To disable multithreading for the instance, specify a value of <code>1</code>. Otherwise, specify the default value of <code>2</code>.</p>"""
    amd_sev_snp: NotRequired[
        "aws_sdk_ec2.types.amd_sev_snp_specification.AmdSevSnpSpecification"
    ]
    r"""<p>Indicates whether to enable the instance for AMD SEV-SNP. AMD SEV-SNP is supported with M6a, R6a, and C6a instance types only. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sev-snp.html\">AMD SEV-SNP for Amazon EC2 instances</a>.</p>"""
    nested_virtualization: NotRequired[
        "aws_sdk_ec2.types.nested_virtualization_specification.NestedVirtualizationSpecification"
    ]
    """<p>Indicates whether to enable the instance for nested virtualization. Nested virtualization is supported only on 8th generation Intel-based instance types (c8i, m8i, r8i, and their flex variants). When nested virtualization is enabled, Virtual Secure Mode (VSM) is automatically disabled for the instance.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchTemplateCpuOptionsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "core_count" in value:
        pairs.append((f"{prefix}.CoreCount", str(value["core_count"])))
    if "threads_per_core" in value:
        pairs.append((f"{prefix}.ThreadsPerCore", str(value["threads_per_core"])))
    if "amd_sev_snp" in value:
        import aws_sdk_ec2.types.amd_sev_snp_specification

        aws_sdk_ec2.types.amd_sev_snp_specification.serialize_ec2_query(
            value["amd_sev_snp"], pairs, f"{prefix}.AmdSevSnp"
        )
    if "nested_virtualization" in value:
        import aws_sdk_ec2.types.nested_virtualization_specification

        aws_sdk_ec2.types.nested_virtualization_specification.serialize_ec2_query(
            value["nested_virtualization"], pairs, f"{prefix}.NestedVirtualization"
        )


def deserialize_ec2_query(el: Element) -> LaunchTemplateCpuOptionsRequest:
    out: LaunchTemplateCpuOptionsRequest = {}  # type: ignore[typeddict-item]
    child_core_count = el.find("CoreCount")
    if child_core_count is not None:
        out["core_count"] = int(child_core_count.text or "")
    child_threads_per_core = el.find("ThreadsPerCore")
    if child_threads_per_core is not None:
        out["threads_per_core"] = int(child_threads_per_core.text or "")
    child_amd_sev_snp = el.find("AmdSevSnp")
    if child_amd_sev_snp is not None:
        import aws_sdk_ec2.types.amd_sev_snp_specification

        out["amd_sev_snp"] = (
            aws_sdk_ec2.types.amd_sev_snp_specification.deserialize_ec2_query(
                child_amd_sev_snp
            )
        )
    child_nested_virtualization = el.find("NestedVirtualization")
    if child_nested_virtualization is not None:
        import aws_sdk_ec2.types.nested_virtualization_specification

        out["nested_virtualization"] = (
            aws_sdk_ec2.types.nested_virtualization_specification.deserialize_ec2_query(
                child_nested_virtualization
            )
        )
    return out

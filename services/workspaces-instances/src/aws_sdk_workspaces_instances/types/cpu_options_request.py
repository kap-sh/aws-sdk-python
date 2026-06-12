"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#CpuOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.amd_sev_snp_enum
    import aws_sdk_workspaces_instances.types.non_negative_integer

class CpuOptionsRequest(TypedDict):
    amd_sev_snp: NotRequired["aws_sdk_workspaces_instances.types.amd_sev_snp_enum.AmdSevSnpEnum"]
    """<p>AMD Secure Encrypted Virtualization configuration.</p>"""
    core_count: NotRequired["aws_sdk_workspaces_instances.types.non_negative_integer.NonNegativeInteger"]
    """<p>Number of CPU cores to allocate.</p>"""
    threads_per_core: NotRequired["aws_sdk_workspaces_instances.types.non_negative_integer.NonNegativeInteger"]
    """<p>Number of threads per CPU core.</p>"""

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CpuOptionsRequest) -> dict:
    out: dict = {}
    if "amd_sev_snp" in value:
        import aws_sdk_workspaces_instances.types.amd_sev_snp_enum
        out["AmdSevSnp"] = aws_sdk_workspaces_instances.types.amd_sev_snp_enum.serialize_aws_json_1_0(value["amd_sev_snp"])
    if "core_count" in value:
        out["CoreCount"] = value["core_count"]
    if "threads_per_core" in value:
        out["ThreadsPerCore"] = value["threads_per_core"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CpuOptionsRequest:
    out: CpuOptionsRequest = {}  # type: ignore[typeddict-item]
    if "AmdSevSnp" in data:
        import aws_sdk_workspaces_instances.types.amd_sev_snp_enum
        out["amd_sev_snp"] = aws_sdk_workspaces_instances.types.amd_sev_snp_enum.deserialize_aws_json_1_0(data["AmdSevSnp"])
    if "CoreCount" in data:
        out["core_count"] = data["CoreCount"]
    if "ThreadsPerCore" in data:
        out["threads_per_core"] = data["ThreadsPerCore"]
    return out
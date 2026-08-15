"""Generated from Smithy shape ``com.amazonaws.ec2#HostCpuOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.amd_sev_snp


class HostCpuOptionsRequest(TypedDict, closed=True):
    amd_sev_snp: NotRequired["capo_ec2.types.amd_sev_snp.AmdSevSnp"]
    """<p>Specifies whether AMD Secure Encrypted Virtualization-Secure Nested Paging (AMD SEV-SNP) is enabled or disabled for the Dedicated Host. If you don't specify a value, AMD SEV-SNP is <code>disabled</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: HostCpuOptionsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "amd_sev_snp" in value:
        import capo_ec2.types.amd_sev_snp

        capo_ec2.types.amd_sev_snp.serialize_ec2_query(
            value["amd_sev_snp"], pairs, f"{key_prefix}AmdSevSnp"
        )


def deserialize_ec2_query(el: Element) -> HostCpuOptionsRequest:
    out: HostCpuOptionsRequest = {}  # type: ignore[typeddict-item]
    child_amd_sev_snp = el.find("AmdSevSnp")
    if child_amd_sev_snp is not None:
        import capo_ec2.types.amd_sev_snp

        out["amd_sev_snp"] = capo_ec2.types.amd_sev_snp.deserialize_ec2_query(
            child_amd_sev_snp
        )
    return out

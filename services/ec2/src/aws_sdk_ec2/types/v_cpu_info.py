"""Generated from Smithy shape ``com.amazonaws.ec2#VCpuInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.core_count
    import aws_sdk_ec2.types.core_count_list
    import aws_sdk_ec2.types.threads_per_core
    import aws_sdk_ec2.types.threads_per_core_list
    import aws_sdk_ec2.types.v_cpu_count


class VCpuInfo(TypedDict):
    default_v_cpus: NotRequired["aws_sdk_ec2.types.v_cpu_count.VCpuCount"]
    """<p>The default number of vCPUs for the instance type.</p>"""
    default_cores: NotRequired["aws_sdk_ec2.types.core_count.CoreCount"]
    """<p>The default number of cores for the instance type.</p>"""
    default_threads_per_core: NotRequired[
        "aws_sdk_ec2.types.threads_per_core.ThreadsPerCore"
    ]
    """<p>The default number of threads per core for the instance type.</p>"""
    valid_cores: NotRequired["aws_sdk_ec2.types.core_count_list.CoreCountList"]
    """<p>The valid number of cores that can be configured for the instance type.</p>"""
    valid_threads_per_core: NotRequired[
        "aws_sdk_ec2.types.threads_per_core_list.ThreadsPerCoreList"
    ]
    """<p>The valid number of threads per core that can be configured for the instance type.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VCpuInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "default_v_cpus" in value:
        pairs.append((f"{prefix}.DefaultVCpus", str(value["default_v_cpus"])))
    if "default_cores" in value:
        pairs.append((f"{prefix}.DefaultCores", str(value["default_cores"])))
    if "default_threads_per_core" in value:
        pairs.append(
            (f"{prefix}.DefaultThreadsPerCore", str(value["default_threads_per_core"]))
        )
    if "valid_cores" in value:
        import aws_sdk_ec2.types.core_count_list

        aws_sdk_ec2.types.core_count_list.serialize_ec2_query(
            value["valid_cores"], pairs, f"{prefix}.ValidCores"
        )
    if "valid_threads_per_core" in value:
        import aws_sdk_ec2.types.threads_per_core_list

        aws_sdk_ec2.types.threads_per_core_list.serialize_ec2_query(
            value["valid_threads_per_core"], pairs, f"{prefix}.ValidThreadsPerCore"
        )


def deserialize_ec2_query(el: Element) -> VCpuInfo:
    out: VCpuInfo = {}  # type: ignore[typeddict-item]
    child_default_v_cpus = el.find("DefaultVCpus")
    if child_default_v_cpus is not None:
        out["default_v_cpus"] = int(child_default_v_cpus.text or "")
    child_default_cores = el.find("DefaultCores")
    if child_default_cores is not None:
        out["default_cores"] = int(child_default_cores.text or "")
    child_default_threads_per_core = el.find("DefaultThreadsPerCore")
    if child_default_threads_per_core is not None:
        out["default_threads_per_core"] = int(child_default_threads_per_core.text or "")
    if el.find("ValidCores") is not None:
        import aws_sdk_ec2.types.core_count_list

        out["valid_cores"] = aws_sdk_ec2.types.core_count_list.deserialize_ec2_query(
            el, "ValidCores"
        )
    if el.find("ValidThreadsPerCore") is not None:
        import aws_sdk_ec2.types.threads_per_core_list

        out["valid_threads_per_core"] = (
            aws_sdk_ec2.types.threads_per_core_list.deserialize_ec2_query(
                el, "ValidThreadsPerCore"
            )
        )
    return out

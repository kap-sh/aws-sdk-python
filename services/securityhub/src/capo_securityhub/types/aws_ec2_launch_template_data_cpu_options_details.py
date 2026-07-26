"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2LaunchTemplateDataCpuOptionsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.integer


class AwsEc2LaunchTemplateDataCpuOptionsDetails(TypedDict, closed=True):
    core_count: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p> The number of CPU cores for the instance. </p>"""
    threads_per_core: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p> The number of threads per CPU core. A value of <code>1</code> disables multithreading for the instance, The default value is <code>2</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2LaunchTemplateDataCpuOptionsDetails) -> dict:
    out: dict = {}
    if "core_count" in value:
        out["CoreCount"] = value["core_count"]
    if "threads_per_core" in value:
        out["ThreadsPerCore"] = value["threads_per_core"]
    return out


def deserialize_json(data: dict) -> AwsEc2LaunchTemplateDataCpuOptionsDetails:
    out: AwsEc2LaunchTemplateDataCpuOptionsDetails = {}  # type: ignore[typeddict-item]
    if "CoreCount" in data:
        out["core_count"] = data["CoreCount"]
    if "ThreadsPerCore" in data:
        out["threads_per_core"] = data["ThreadsPerCore"]
    return out

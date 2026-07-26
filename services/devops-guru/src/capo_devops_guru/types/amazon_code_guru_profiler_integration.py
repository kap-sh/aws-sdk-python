"""Generated from Smithy shape ``com.amazonaws.devopsguru#AmazonCodeGuruProfilerIntegration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.event_source_opt_in_status


class AmazonCodeGuruProfilerIntegration(TypedDict, closed=True):
    status: NotRequired[
        "capo_devops_guru.types.event_source_opt_in_status.EventSourceOptInStatus"
    ]
    """<p>The status of the CodeGuru Profiler integration. Specifies if DevOps Guru is enabled to consume recommendations that are generated from Amazon CodeGuru Profiler.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AmazonCodeGuruProfilerIntegration) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_devops_guru.types.event_source_opt_in_status

        out["Status"] = (
            capo_devops_guru.types.event_source_opt_in_status.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> AmazonCodeGuruProfilerIntegration:
    out: AmazonCodeGuruProfilerIntegration = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import capo_devops_guru.types.event_source_opt_in_status

        out["status"] = (
            capo_devops_guru.types.event_source_opt_in_status.deserialize_json(
                data["Status"]
            )
        )
    return out

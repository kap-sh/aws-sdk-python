"""Generated from Smithy shape ``com.amazonaws.devopsguru#AmazonCodeGuruProfilerIntegration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.event_source_opt_in_status


class AmazonCodeGuruProfilerIntegration(TypedDict):
    status: NotRequired[
        "aws_sdk_devops_guru.types.event_source_opt_in_status.EventSourceOptInStatus"
    ]
    """<p>The status of the CodeGuru Profiler integration. Specifies if DevOps Guru is enabled to consume recommendations that are generated from Amazon CodeGuru Profiler.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AmazonCodeGuruProfilerIntegration) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_devops_guru.types.event_source_opt_in_status

        out["Status"] = (
            aws_sdk_devops_guru.types.event_source_opt_in_status.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> AmazonCodeGuruProfilerIntegration:
    out: AmazonCodeGuruProfilerIntegration = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_devops_guru.types.event_source_opt_in_status

        out["status"] = (
            aws_sdk_devops_guru.types.event_source_opt_in_status.deserialize_json(
                data["Status"]
            )
        )
    return out

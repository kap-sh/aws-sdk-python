"""Generated from Smithy shape ``com.amazonaws.devopsguru#EventSourcesConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.amazon_code_guru_profiler_integration


class EventSourcesConfig(TypedDict):
    amazon_code_guru_profiler: NotRequired[
        "aws_sdk_devops_guru.types.amazon_code_guru_profiler_integration.AmazonCodeGuruProfilerIntegration"
    ]
    """<p>Information about whether DevOps Guru is configured to consume recommendations which are generated from AWS CodeGuru Profiler.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventSourcesConfig) -> dict:
    out: dict = {}
    if "amazon_code_guru_profiler" in value:
        import aws_sdk_devops_guru.types.amazon_code_guru_profiler_integration

        out["AmazonCodeGuruProfiler"] = (
            aws_sdk_devops_guru.types.amazon_code_guru_profiler_integration.serialize_json(
                value["amazon_code_guru_profiler"]
            )
        )
    return out


def deserialize_json(data: dict) -> EventSourcesConfig:
    out: EventSourcesConfig = {}  # type: ignore[typeddict-item]
    if "AmazonCodeGuruProfiler" in data:
        import aws_sdk_devops_guru.types.amazon_code_guru_profiler_integration

        out["amazon_code_guru_profiler"] = (
            aws_sdk_devops_guru.types.amazon_code_guru_profiler_integration.deserialize_json(
                data["AmazonCodeGuruProfiler"]
            )
        )
    return out

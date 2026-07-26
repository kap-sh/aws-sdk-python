"""Generated from Smithy shape ``com.amazonaws.devopsguru#EventSourcesConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.amazon_code_guru_profiler_integration


class EventSourcesConfig(TypedDict, closed=True):
    amazon_code_guru_profiler: NotRequired[
        "capo_devops_guru.types.amazon_code_guru_profiler_integration.AmazonCodeGuruProfilerIntegration"
    ]
    """<p>Information about whether DevOps Guru is configured to consume recommendations which are generated from AWS CodeGuru Profiler.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventSourcesConfig) -> dict:
    out: dict = {}
    if "amazon_code_guru_profiler" in value:
        import capo_devops_guru.types.amazon_code_guru_profiler_integration

        out["AmazonCodeGuruProfiler"] = (
            capo_devops_guru.types.amazon_code_guru_profiler_integration.serialize_json(
                value["amazon_code_guru_profiler"]
            )
        )
    return out


def deserialize_json(data: dict) -> EventSourcesConfig:
    out: EventSourcesConfig = {}  # type: ignore[typeddict-item]
    if "AmazonCodeGuruProfiler" in data:
        import capo_devops_guru.types.amazon_code_guru_profiler_integration

        out["amazon_code_guru_profiler"] = (
            capo_devops_guru.types.amazon_code_guru_profiler_integration.deserialize_json(
                data["AmazonCodeGuruProfiler"]
            )
        )
    return out

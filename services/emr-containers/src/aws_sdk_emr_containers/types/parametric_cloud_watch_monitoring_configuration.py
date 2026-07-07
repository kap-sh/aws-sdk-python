"""Generated from Smithy shape ``com.amazonaws.emrcontainers#ParametricCloudWatchMonitoringConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.string256
    import aws_sdk_emr_containers.types.template_parameter


class ParametricCloudWatchMonitoringConfiguration(TypedDict, closed=True):
    log_group_name: NotRequired[
        "aws_sdk_emr_containers.types.template_parameter.TemplateParameter"
    ]
    """<p> The name of the log group for log publishing.</p>"""
    log_stream_name_prefix: NotRequired[
        "aws_sdk_emr_containers.types.string256.String256"
    ]
    """<p> The specified name prefix for log streams.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParametricCloudWatchMonitoringConfiguration) -> dict:
    out: dict = {}
    if "log_group_name" in value:
        out["logGroupName"] = value["log_group_name"]
    if "log_stream_name_prefix" in value:
        out["logStreamNamePrefix"] = value["log_stream_name_prefix"]
    return out


def deserialize_json(data: dict) -> ParametricCloudWatchMonitoringConfiguration:
    out: ParametricCloudWatchMonitoringConfiguration = {}  # type: ignore[typeddict-item]
    if "logGroupName" in data:
        out["log_group_name"] = data["logGroupName"]
    if "logStreamNamePrefix" in data:
        out["log_stream_name_prefix"] = data["logStreamNamePrefix"]
    return out

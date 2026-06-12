"""Generated from Smithy shape ``com.amazonaws.devopsguru#LogsAnomalyDetectionIntegrationConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.opt_in_status


class LogsAnomalyDetectionIntegrationConfig(TypedDict):
    opt_in_status: NotRequired["aws_sdk_devops_guru.types.opt_in_status.OptInStatus"]
    """<p>Specifies if DevOps Guru is configured to perform log anomaly detection on CloudWatch log groups.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogsAnomalyDetectionIntegrationConfig) -> dict:
    out: dict = {}
    if "opt_in_status" in value:
        import aws_sdk_devops_guru.types.opt_in_status

        out["OptInStatus"] = aws_sdk_devops_guru.types.opt_in_status.serialize_json(
            value["opt_in_status"]
        )
    return out


def deserialize_json(data: dict) -> LogsAnomalyDetectionIntegrationConfig:
    out: LogsAnomalyDetectionIntegrationConfig = {}  # type: ignore[typeddict-item]
    if "OptInStatus" in data:
        import aws_sdk_devops_guru.types.opt_in_status

        out["opt_in_status"] = aws_sdk_devops_guru.types.opt_in_status.deserialize_json(
            data["OptInStatus"]
        )
    return out

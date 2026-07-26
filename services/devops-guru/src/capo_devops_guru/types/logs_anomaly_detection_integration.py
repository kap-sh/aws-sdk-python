"""Generated from Smithy shape ``com.amazonaws.devopsguru#LogsAnomalyDetectionIntegration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.opt_in_status


class LogsAnomalyDetectionIntegration(TypedDict, closed=True):
    opt_in_status: NotRequired["capo_devops_guru.types.opt_in_status.OptInStatus"]
    """<p>Specifies if DevOps Guru is configured to perform log anomaly detection on CloudWatch log groups.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogsAnomalyDetectionIntegration) -> dict:
    out: dict = {}
    if "opt_in_status" in value:
        import capo_devops_guru.types.opt_in_status

        out["OptInStatus"] = capo_devops_guru.types.opt_in_status.serialize_json(
            value["opt_in_status"]
        )
    return out


def deserialize_json(data: dict) -> LogsAnomalyDetectionIntegration:
    out: LogsAnomalyDetectionIntegration = {}  # type: ignore[typeddict-item]
    if "OptInStatus" in data:
        import capo_devops_guru.types.opt_in_status

        out["opt_in_status"] = capo_devops_guru.types.opt_in_status.deserialize_json(
            data["OptInStatus"]
        )
    return out

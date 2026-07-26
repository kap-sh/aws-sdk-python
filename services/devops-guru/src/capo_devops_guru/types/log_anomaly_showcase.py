"""Generated from Smithy shape ``com.amazonaws.devopsguru#LogAnomalyShowcase``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.log_anomaly_classes


class LogAnomalyShowcase(TypedDict, closed=True):
    log_anomaly_classes: NotRequired[
        "capo_devops_guru.types.log_anomaly_classes.LogAnomalyClasses"
    ]
    """<p> A list of anomalous log events that may be related. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogAnomalyShowcase) -> dict:
    out: dict = {}
    if "log_anomaly_classes" in value:
        import capo_devops_guru.types.log_anomaly_classes

        out["LogAnomalyClasses"] = (
            capo_devops_guru.types.log_anomaly_classes.serialize_json(
                value["log_anomaly_classes"]
            )
        )
    return out


def deserialize_json(data: dict) -> LogAnomalyShowcase:
    out: LogAnomalyShowcase = {}  # type: ignore[typeddict-item]
    if "LogAnomalyClasses" in data:
        import capo_devops_guru.types.log_anomaly_classes

        out["log_anomaly_classes"] = (
            capo_devops_guru.types.log_anomaly_classes.deserialize_json(
                data["LogAnomalyClasses"]
            )
        )
    return out

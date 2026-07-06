"""Generated from Smithy shape ``com.amazonaws.autoscaling#ProcessType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.xml_string_max_len255


class ProcessType(TypedDict, closed=True):
    process_name: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>One of the following processes:</p> <ul> <li> <p> <code>Launch</code> </p> </li> <li> <p> <code>Terminate</code> </p> </li> <li> <p> <code>AddToLoadBalancer</code> </p> </li> <li> <p> <code>AlarmNotification</code> </p> </li> <li> <p> <code>AZRebalance</code> </p> </li> <li> <p> <code>HealthCheck</code> </p> </li> <li> <p> <code>InstanceRefresh</code> </p> </li> <li> <p> <code>ReplaceUnhealthy</code> </p> </li> <li> <p> <code>ScheduledActions</code> </p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ProcessType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "process_name" in value:
        pairs.append((f"{prefix}.ProcessName", str(value["process_name"])))


def deserialize_query(el: Element) -> ProcessType:
    out: ProcessType = {}  # type: ignore[typeddict-item]
    child_process_name = el.find("ProcessName")
    if child_process_name is not None:
        out["process_name"] = str(child_process_name.text or "")
    return out

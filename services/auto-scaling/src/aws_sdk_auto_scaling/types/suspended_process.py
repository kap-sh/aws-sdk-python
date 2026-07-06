"""Generated from Smithy shape ``com.amazonaws.autoscaling#SuspendedProcess``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.xml_string_max_len255


class SuspendedProcess(TypedDict, closed=True):
    process_name: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the suspended process.</p>"""
    suspension_reason: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The reason that the process was suspended.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SuspendedProcess, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "process_name" in value:
        pairs.append((f"{prefix}.ProcessName", str(value["process_name"])))
    if "suspension_reason" in value:
        pairs.append((f"{prefix}.SuspensionReason", str(value["suspension_reason"])))


def deserialize_query(el: Element) -> SuspendedProcess:
    out: SuspendedProcess = {}  # type: ignore[typeddict-item]
    child_process_name = el.find("ProcessName")
    if child_process_name is not None:
        out["process_name"] = str(child_process_name.text or "")
    child_suspension_reason = el.find("SuspensionReason")
    if child_suspension_reason is not None:
        out["suspension_reason"] = str(child_suspension_reason.text or "")
    return out

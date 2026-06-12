"""Generated from Smithy shape ``com.amazonaws.autoscaling#ProcessesType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.processes


class ProcessesType(TypedDict):
    processes: NotRequired["aws_sdk_auto_scaling.types.processes.Processes"]
    """<p>The names of the process types.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ProcessesType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "processes" in value:
        import aws_sdk_auto_scaling.types.processes

        aws_sdk_auto_scaling.types.processes.serialize_query(
            value["processes"], pairs, f"{prefix}.Processes"
        )


def deserialize_query(el: Element) -> ProcessesType:
    out: ProcessesType = {}  # type: ignore[typeddict-item]
    child_processes = el.find("Processes")
    if child_processes is not None:
        import aws_sdk_auto_scaling.types.processes

        out["processes"] = aws_sdk_auto_scaling.types.processes.deserialize_query(
            child_processes
        )
    return out

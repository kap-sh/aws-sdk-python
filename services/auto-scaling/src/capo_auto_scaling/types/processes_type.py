"""Generated from Smithy shape ``com.amazonaws.autoscaling#ProcessesType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.processes


class ProcessesType(TypedDict, closed=True):
    processes: NotRequired["capo_auto_scaling.types.processes.Processes"]
    """<p>The names of the process types.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ProcessesType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "processes" in value:
        import capo_auto_scaling.types.processes

        capo_auto_scaling.types.processes.serialize_query(
            value["processes"], pairs, f"{key_prefix}Processes"
        )


def deserialize_query(el: Element) -> ProcessesType:
    out: ProcessesType = {}  # type: ignore[typeddict-item]
    child_processes = el.find("Processes")
    if child_processes is not None:
        import capo_auto_scaling.types.processes

        out["processes"] = capo_auto_scaling.types.processes.deserialize_query(
            child_processes
        )
    return out

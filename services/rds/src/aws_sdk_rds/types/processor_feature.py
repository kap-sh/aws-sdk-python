"""Generated from Smithy shape ``com.amazonaws.rds#ProcessorFeature``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.string


class ProcessorFeature(TypedDict, closed=True):
    name: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The name of the processor feature. Valid names are <code>coreCount</code> and <code>threadsPerCore</code>.</p>"""
    value: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The value of a processor feature.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ProcessorFeature, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "name" in value:
        pairs.append((f"{prefix}.Name", str(value["name"])))
    if "value" in value:
        pairs.append((f"{prefix}.Value", str(value["value"])))


def deserialize_query(el: Element) -> ProcessorFeature:
    out: ProcessorFeature = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = str(child_value.text or "")
    return out

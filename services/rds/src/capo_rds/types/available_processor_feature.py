"""Generated from Smithy shape ``com.amazonaws.rds#AvailableProcessorFeature``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string


class AvailableProcessorFeature(TypedDict, closed=True):
    name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the processor feature. Valid names are <code>coreCount</code> and <code>threadsPerCore</code>.</p>"""
    default_value: NotRequired["capo_rds.types.string.String"]
    """<p>The default value for the processor feature of the DB instance class.</p>"""
    allowed_values: NotRequired["capo_rds.types.string.String"]
    """<p>The allowed values for the processor feature of the DB instance class.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AvailableProcessorFeature, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "name" in value:
        pairs.append((f"{key_prefix}Name", str(value["name"])))
    if "default_value" in value:
        pairs.append((f"{key_prefix}DefaultValue", str(value["default_value"])))
    if "allowed_values" in value:
        pairs.append((f"{key_prefix}AllowedValues", str(value["allowed_values"])))


def deserialize_query(el: Element) -> AvailableProcessorFeature:
    out: AvailableProcessorFeature = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_default_value = el.find("DefaultValue")
    if child_default_value is not None:
        out["default_value"] = str(child_default_value.text or "")
    child_allowed_values = el.find("AllowedValues")
    if child_allowed_values is not None:
        out["allowed_values"] = str(child_allowed_values.text or "")
    return out

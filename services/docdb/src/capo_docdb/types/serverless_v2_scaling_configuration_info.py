"""Generated from Smithy shape ``com.amazonaws.docdb#ServerlessV2ScalingConfigurationInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.double_optional


class ServerlessV2ScalingConfigurationInfo(TypedDict, closed=True):
    min_capacity: NotRequired["capo_docdb.types.double_optional.DoubleOptional"]
    """<p>The minimum number of Amazon DocumentDB capacity units (DCUs) for an instance in an Amazon DocumentDB Serverless cluster. You can specify DCU values in half-step increments, such as 8, 8.5, 9, and so on.</p>"""
    max_capacity: NotRequired["capo_docdb.types.double_optional.DoubleOptional"]
    """<p>The maximum number of Amazon DocumentDB capacity units (DCUs) for an instance in an Amazon DocumentDB Serverless cluster. You can specify DCU values in half-step increments, such as 32, 32.5, 33, and so on. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ServerlessV2ScalingConfigurationInfo,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "min_capacity" in value:
        pairs.append((f"{key_prefix}MinCapacity", str(value["min_capacity"])))
    if "max_capacity" in value:
        pairs.append((f"{key_prefix}MaxCapacity", str(value["max_capacity"])))


def deserialize_query(el: Element) -> ServerlessV2ScalingConfigurationInfo:
    out: ServerlessV2ScalingConfigurationInfo = {}  # type: ignore[typeddict-item]
    child_min_capacity = el.find("MinCapacity")
    if child_min_capacity is not None:
        out["min_capacity"] = float(child_min_capacity.text or "")
    child_max_capacity = el.find("MaxCapacity")
    if child_max_capacity is not None:
        out["max_capacity"] = float(child_max_capacity.text or "")
    return out

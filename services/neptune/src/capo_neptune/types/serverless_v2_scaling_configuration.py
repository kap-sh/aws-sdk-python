"""Generated from Smithy shape ``com.amazonaws.neptune#ServerlessV2ScalingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.double_optional


class ServerlessV2ScalingConfiguration(TypedDict, closed=True):
    min_capacity: NotRequired["capo_neptune.types.double_optional.DoubleOptional"]
    """<p>The minimum number of Neptune capacity units (NCUs) for a DB instance in a Neptune Serverless cluster. You can specify NCU values in half-step increments, such as 8, 8.5, 9, and so on.</p>"""
    max_capacity: NotRequired["capo_neptune.types.double_optional.DoubleOptional"]
    """<p>The maximum number of Neptune capacity units (NCUs) for a DB instance in a Neptune Serverless cluster. You can specify NCU values in half-step increments, such as 40, 40.5, 41, and so on.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ServerlessV2ScalingConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "min_capacity" in value:
        pairs.append((f"{prefix}.MinCapacity", str(value["min_capacity"])))
    if "max_capacity" in value:
        pairs.append((f"{prefix}.MaxCapacity", str(value["max_capacity"])))


def deserialize_query(el: Element) -> ServerlessV2ScalingConfiguration:
    out: ServerlessV2ScalingConfiguration = {}  # type: ignore[typeddict-item]
    child_min_capacity = el.find("MinCapacity")
    if child_min_capacity is not None:
        out["min_capacity"] = float(child_min_capacity.text or "")
    child_max_capacity = el.find("MaxCapacity")
    if child_max_capacity is not None:
        out["max_capacity"] = float(child_max_capacity.text or "")
    return out

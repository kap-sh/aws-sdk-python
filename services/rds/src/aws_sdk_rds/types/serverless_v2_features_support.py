"""Generated from Smithy shape ``com.amazonaws.rds#ServerlessV2FeaturesSupport``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.double_optional


class ServerlessV2FeaturesSupport(TypedDict):
    min_capacity: NotRequired["aws_sdk_rds.types.double_optional.DoubleOptional"]
    """<p>If the minimum capacity is 0 ACUs, the engine version or platform version supports the automatic pause/resume feature of Aurora Serverless v2.</p>"""
    max_capacity: NotRequired["aws_sdk_rds.types.double_optional.DoubleOptional"]
    """<p> Specifies the upper Aurora Serverless v2 capacity limit for a particular engine version or platform version. Depending on the engine version, the maximum capacity for an Aurora Serverless v2 cluster might be <code>256</code> or <code>128</code>. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ServerlessV2FeaturesSupport, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "min_capacity" in value:
        pairs.append((f"{prefix}.MinCapacity", str(value["min_capacity"])))
    if "max_capacity" in value:
        pairs.append((f"{prefix}.MaxCapacity", str(value["max_capacity"])))


def deserialize_query(el: Element) -> ServerlessV2FeaturesSupport:
    out: ServerlessV2FeaturesSupport = {}  # type: ignore[typeddict-item]
    child_min_capacity = el.find("MinCapacity")
    if child_min_capacity is not None:
        out["min_capacity"] = float(child_min_capacity.text or "")
    child_max_capacity = el.find("MaxCapacity")
    if child_max_capacity is not None:
        out["max_capacity"] = float(child_max_capacity.text or "")
    return out

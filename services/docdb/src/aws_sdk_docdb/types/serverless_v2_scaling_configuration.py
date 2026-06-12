"""Generated from Smithy shape ``com.amazonaws.docdb#ServerlessV2ScalingConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_docdb.types.double_optional


class ServerlessV2ScalingConfiguration(TypedDict):
    min_capacity: NotRequired["aws_sdk_docdb.types.double_optional.DoubleOptional"]
    """<p>The minimum number of Amazon DocumentDB capacity units (DCUs) for an instance in an Amazon DocumentDB Serverless cluster. You can specify DCU values in half-step increments, such as 8, 8.5, 9, and so on.</p>"""
    max_capacity: NotRequired["aws_sdk_docdb.types.double_optional.DoubleOptional"]
    """<p>The maximum number of Amazon DocumentDB capacity units (DCUs) for an instance in an Amazon DocumentDB Serverless cluster. You can specify DCU values in half-step increments, such as 32, 32.5, 33, and so on.</p>"""


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

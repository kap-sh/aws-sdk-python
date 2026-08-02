"""Generated from Smithy shape ``com.amazonaws.rds#ServerlessV2ScalingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.double_optional
    import capo_rds.types.integer_optional


class ServerlessV2ScalingConfiguration(TypedDict, closed=True):
    min_capacity: NotRequired["capo_rds.types.double_optional.DoubleOptional"]
    """<p>The minimum number of Aurora capacity units (ACUs) for a DB instance in an Aurora Serverless v2 cluster. You can specify ACU values in half-step increments, such as 8, 8.5, 9, and so on. For Aurora versions that support the Aurora Serverless v2 auto-pause feature, the smallest value that you can use is 0. For versions that don't support Aurora Serverless v2 auto-pause, the smallest value that you can use is 0.5. </p>"""
    max_capacity: NotRequired["capo_rds.types.double_optional.DoubleOptional"]
    """<p>The maximum number of Aurora capacity units (ACUs) for a DB instance in an Aurora Serverless v2 cluster. You can specify ACU values in half-step increments, such as 32, 32.5, 33, and so on. The largest value that you can use is 256 for recent Aurora versions, or 128 for older versions. You can check the attributes of your engine version or platform version to determine the specific maximum capacity supported.</p>"""
    seconds_until_auto_pause: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>Specifies the number of seconds an Aurora Serverless v2 DB instance must be idle before Aurora attempts to automatically pause it. </p> <p>Specify a value between 300 seconds (five minutes) and 86,400 seconds (one day). The default is 300 seconds.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ServerlessV2ScalingConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "min_capacity" in value:
        pairs.append((f"{key_prefix}MinCapacity", str(value["min_capacity"])))
    if "max_capacity" in value:
        pairs.append((f"{key_prefix}MaxCapacity", str(value["max_capacity"])))
    if "seconds_until_auto_pause" in value:
        pairs.append(
            (
                f"{key_prefix}SecondsUntilAutoPause",
                str(value["seconds_until_auto_pause"]),
            )
        )


def deserialize_query(el: Element) -> ServerlessV2ScalingConfiguration:
    out: ServerlessV2ScalingConfiguration = {}  # type: ignore[typeddict-item]
    child_min_capacity = el.find("MinCapacity")
    if child_min_capacity is not None:
        out["min_capacity"] = float(child_min_capacity.text or "")
    child_max_capacity = el.find("MaxCapacity")
    if child_max_capacity is not None:
        out["max_capacity"] = float(child_max_capacity.text or "")
    child_seconds_until_auto_pause = el.find("SecondsUntilAutoPause")
    if child_seconds_until_auto_pause is not None:
        out["seconds_until_auto_pause"] = int(child_seconds_until_auto_pause.text or "")
    return out

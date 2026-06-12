"""Generated from Smithy shape ``com.amazonaws.rds#ServerlessV2ScalingConfigurationInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.double_optional
    import aws_sdk_rds.types.integer_optional


class ServerlessV2ScalingConfigurationInfo(TypedDict):
    min_capacity: NotRequired["aws_sdk_rds.types.double_optional.DoubleOptional"]
    """<p>The minimum number of Aurora capacity units (ACUs) for a DB instance in an Aurora Serverless v2 cluster. You can specify ACU values in half-step increments, such as 8, 8.5, 9, and so on. For Aurora versions that support the Aurora Serverless v2 auto-pause feature, the smallest value that you can use is 0. For versions that don't support Aurora Serverless v2 auto-pause, the smallest value that you can use is 0.5. </p>"""
    max_capacity: NotRequired["aws_sdk_rds.types.double_optional.DoubleOptional"]
    """<p>The maximum number of Aurora capacity units (ACUs) for a DB instance in an Aurora Serverless v2 cluster. You can specify ACU values in half-step increments, such as 32, 32.5, 33, and so on. The largest value that you can use is 256 for recent Aurora versions, or 128 for older versions. You can check the attributes of your engine version or platform version to determine the specific maximum capacity supported.</p>"""
    seconds_until_auto_pause: NotRequired[
        "aws_sdk_rds.types.integer_optional.IntegerOptional"
    ]
    """<p> The number of seconds an Aurora Serverless v2 DB instance must be idle before Aurora attempts to automatically pause it. This property is only shown when the minimum capacity for the cluster is set to 0 ACUs. Changing the minimum capacity to a nonzero value removes this property. If you later change the minimum capacity back to 0 ACUs, this property is reset to its default value unless you specify it again. </p> <p>This value ranges between 300 seconds (five minutes) and 86,400 seconds (one day). The default is 300 seconds.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ServerlessV2ScalingConfigurationInfo,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "min_capacity" in value:
        pairs.append((f"{prefix}.MinCapacity", str(value["min_capacity"])))
    if "max_capacity" in value:
        pairs.append((f"{prefix}.MaxCapacity", str(value["max_capacity"])))
    if "seconds_until_auto_pause" in value:
        pairs.append(
            (f"{prefix}.SecondsUntilAutoPause", str(value["seconds_until_auto_pause"]))
        )


def deserialize_query(el: Element) -> ServerlessV2ScalingConfigurationInfo:
    out: ServerlessV2ScalingConfigurationInfo = {}  # type: ignore[typeddict-item]
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

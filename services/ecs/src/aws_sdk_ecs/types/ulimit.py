"""Generated from Smithy shape ``com.amazonaws.ecs#Ulimit``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.integer
    import aws_sdk_ecs.types.ulimit_name


class Ulimit(TypedDict):
    name: "aws_sdk_ecs.types.ulimit_name.UlimitName"
    """<p>The <code>type</code> of the <code>ulimit</code>.</p>"""
    soft_limit: "aws_sdk_ecs.types.integer.Integer"
    """<p>The soft limit for the <code>ulimit</code> type. The value can be specified in bytes, seconds, or as a count, depending on the <code>type</code> of the <code>ulimit</code>.</p>"""
    hard_limit: "aws_sdk_ecs.types.integer.Integer"
    """<p>The hard limit for the <code>ulimit</code> type. The value can be specified in bytes, seconds, or as a count, depending on the <code>type</code> of the <code>ulimit</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Ulimit) -> dict:
    out: dict = {}
    import aws_sdk_ecs.types.ulimit_name

    out["name"] = aws_sdk_ecs.types.ulimit_name.serialize_aws_json_1_1(value["name"])
    out["softLimit"] = value.get("soft_limit", 0)
    out["hardLimit"] = value.get("hard_limit", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> Ulimit:
    out: Ulimit = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_ecs.types.ulimit_name

        out["name"] = aws_sdk_ecs.types.ulimit_name.deserialize_aws_json_1_1(
            data["name"]
        )
    else:
        raise DeserializationError("Ulimit.name required")
    if "softLimit" in data:
        out["soft_limit"] = data["softLimit"]
    else:
        out["soft_limit"] = 0
    if "hardLimit" in data:
        out["hard_limit"] = data["hardLimit"]
    else:
        out["hard_limit"] = 0
    return out

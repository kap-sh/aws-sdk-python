"""Generated from Smithy shape ``com.amazonaws.eks#Taint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.taint_effect
    import aws_sdk_eks.types.taint_key
    import aws_sdk_eks.types.taint_value


class Taint(TypedDict, closed=True):
    key: NotRequired["aws_sdk_eks.types.taint_key.taintKey"]
    """<p>The key of the taint.</p>"""
    value: NotRequired["aws_sdk_eks.types.taint_value.taintValue"]
    """<p>The value of the taint.</p>"""
    effect: NotRequired["aws_sdk_eks.types.taint_effect.TaintEffect"]
    """<p>The effect of the taint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Taint) -> dict:
    out: dict = {}
    if "key" in value:
        out["key"] = value["key"]
    if "value" in value:
        out["value"] = value["value"]
    if "effect" in value:
        import aws_sdk_eks.types.taint_effect

        out["effect"] = aws_sdk_eks.types.taint_effect.serialize_json(value["effect"])
    return out


def deserialize_json(data: dict) -> Taint:
    out: Taint = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    if "value" in data:
        out["value"] = data["value"]
    if "effect" in data:
        import aws_sdk_eks.types.taint_effect

        out["effect"] = aws_sdk_eks.types.taint_effect.deserialize_json(data["effect"])
    return out

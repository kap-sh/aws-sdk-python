"""Generated from Smithy shape ``com.amazonaws.eks#UpdateParam``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.string
    import aws_sdk_eks.types.update_param_type


class UpdateParam(TypedDict, closed=True):
    type: NotRequired["aws_sdk_eks.types.update_param_type.UpdateParamType"]
    """<p>The keys associated with an update request.</p>"""
    value: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The value of the keys submitted as part of an update request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateParam) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_eks.types.update_param_type

        out["type"] = aws_sdk_eks.types.update_param_type.serialize_json(value["type"])
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> UpdateParam:
    out: UpdateParam = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_eks.types.update_param_type

        out["type"] = aws_sdk_eks.types.update_param_type.deserialize_json(data["type"])
    if "value" in data:
        out["value"] = data["value"]
    return out

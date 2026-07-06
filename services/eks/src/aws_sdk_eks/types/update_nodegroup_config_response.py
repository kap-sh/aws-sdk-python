"""Generated from Smithy shape ``com.amazonaws.eks#UpdateNodegroupConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.update


class UpdateNodegroupConfigResponse(TypedDict, closed=True):
    update: NotRequired["aws_sdk_eks.types.update.Update"]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateNodegroupConfigResponse) -> dict:
    out: dict = {}
    if "update" in value:
        import aws_sdk_eks.types.update

        out["update"] = aws_sdk_eks.types.update.serialize_json(value["update"])
    return out


def deserialize_json(data: dict) -> UpdateNodegroupConfigResponse:
    out: UpdateNodegroupConfigResponse = {}  # type: ignore[typeddict-item]
    if "update" in data:
        import aws_sdk_eks.types.update

        out["update"] = aws_sdk_eks.types.update.deserialize_json(data["update"])
    return out

"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ComputationModelResolveToResourceSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.resolve_to


class ComputationModelResolveToResourceSummary(TypedDict):
    resolve_to: NotRequired["aws_sdk_iotsitewise.types.resolve_to.ResolveTo"]


# --- restJson1 ser/de ---
def serialize_json(value: ComputationModelResolveToResourceSummary) -> dict:
    out: dict = {}
    if "resolve_to" in value:
        import aws_sdk_iotsitewise.types.resolve_to

        out["resolveTo"] = aws_sdk_iotsitewise.types.resolve_to.serialize_json(
            value["resolve_to"]
        )
    return out


def deserialize_json(data: dict) -> ComputationModelResolveToResourceSummary:
    out: ComputationModelResolveToResourceSummary = {}  # type: ignore[typeddict-item]
    if "resolveTo" in data:
        import aws_sdk_iotsitewise.types.resolve_to

        out["resolve_to"] = aws_sdk_iotsitewise.types.resolve_to.deserialize_json(
            data["resolveTo"]
        )
    return out

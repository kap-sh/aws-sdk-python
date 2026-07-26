"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ComputationModelResolveToResourceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.resolve_to


class ComputationModelResolveToResourceSummary(TypedDict, closed=True):
    resolve_to: NotRequired["capo_iotsitewise.types.resolve_to.ResolveTo"]


# --- restJson1 ser/de ---
def serialize_json(value: ComputationModelResolveToResourceSummary) -> dict:
    out: dict = {}
    if "resolve_to" in value:
        import capo_iotsitewise.types.resolve_to

        out["resolveTo"] = capo_iotsitewise.types.resolve_to.serialize_json(
            value["resolve_to"]
        )
    return out


def deserialize_json(data: dict) -> ComputationModelResolveToResourceSummary:
    out: ComputationModelResolveToResourceSummary = {}  # type: ignore[typeddict-item]
    if "resolveTo" in data:
        import capo_iotsitewise.types.resolve_to

        out["resolve_to"] = capo_iotsitewise.types.resolve_to.deserialize_json(
            data["resolveTo"]
        )
    return out

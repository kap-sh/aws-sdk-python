"""Generated from Smithy shape ``com.amazonaws.amplify#GetBranchResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amplify.types.branch


class GetBranchResult(TypedDict, closed=True):
    branch: "capo_amplify.types.branch.Branch"


# --- restJson1 ser/de ---
def serialize_json(value: GetBranchResult) -> dict:
    out: dict = {}
    import capo_amplify.types.branch

    out["branch"] = capo_amplify.types.branch.serialize_json(value["branch"])
    return out


def deserialize_json(data: dict) -> GetBranchResult:
    out: GetBranchResult = {}  # type: ignore[typeddict-item]
    if "branch" in data:
        import capo_amplify.types.branch

        out["branch"] = capo_amplify.types.branch.deserialize_json(data["branch"])
    else:
        raise DeserializationError("GetBranchResult.branch required")
    return out

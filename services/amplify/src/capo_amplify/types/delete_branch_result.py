"""Generated from Smithy shape ``com.amazonaws.amplify#DeleteBranchResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amplify.types.branch


class DeleteBranchResult(TypedDict, closed=True):
    branch: "capo_amplify.types.branch.Branch"
    """<p>The branch for an Amplify app, which maps to a third-party repository branch. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBranchResult) -> dict:
    out: dict = {}
    import capo_amplify.types.branch

    out["branch"] = capo_amplify.types.branch.serialize_json(value["branch"])
    return out


def deserialize_json(data: dict) -> DeleteBranchResult:
    out: DeleteBranchResult = {}  # type: ignore[typeddict-item]
    if "branch" in data:
        import capo_amplify.types.branch

        out["branch"] = capo_amplify.types.branch.deserialize_json(data["branch"])
    else:
        raise DeserializationError("DeleteBranchResult.branch required")
    return out

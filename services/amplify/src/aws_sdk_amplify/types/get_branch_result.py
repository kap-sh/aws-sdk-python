"""Generated from Smithy shape ``com.amazonaws.amplify#GetBranchResult``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplify.types.branch


class GetBranchResult(TypedDict):
    branch: "aws_sdk_amplify.types.branch.Branch"


# --- restJson1 ser/de ---
def serialize_json(value: GetBranchResult) -> dict:
    out: dict = {}
    import aws_sdk_amplify.types.branch

    out["branch"] = aws_sdk_amplify.types.branch.serialize_json(value["branch"])
    return out


def deserialize_json(data: dict) -> GetBranchResult:
    out: GetBranchResult = {}  # type: ignore[typeddict-item]
    if "branch" in data:
        import aws_sdk_amplify.types.branch

        out["branch"] = aws_sdk_amplify.types.branch.deserialize_json(data["branch"])
    else:
        raise DeserializationError("GetBranchResult.branch required")
    return out

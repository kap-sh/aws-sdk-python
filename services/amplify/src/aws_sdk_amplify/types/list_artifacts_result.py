"""Generated from Smithy shape ``com.amazonaws.amplify#ListArtifactsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplify.types.artifacts
    import aws_sdk_amplify.types.next_token


class ListArtifactsResult(TypedDict, closed=True):
    artifacts: "aws_sdk_amplify.types.artifacts.Artifacts"
    """<p>A list of artifacts. </p>"""
    next_token: NotRequired["aws_sdk_amplify.types.next_token.NextToken"]
    """<p>A pagination token. If a non-null pagination token is returned in a result, pass its value in another request to retrieve more entries. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListArtifactsResult) -> dict:
    out: dict = {}
    import aws_sdk_amplify.types.artifacts

    out["artifacts"] = aws_sdk_amplify.types.artifacts.serialize_json(
        value["artifacts"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListArtifactsResult:
    out: ListArtifactsResult = {}  # type: ignore[typeddict-item]
    if "artifacts" in data:
        import aws_sdk_amplify.types.artifacts

        out["artifacts"] = aws_sdk_amplify.types.artifacts.deserialize_json(
            data["artifacts"]
        )
    else:
        raise DeserializationError("ListArtifactsResult.artifacts required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out

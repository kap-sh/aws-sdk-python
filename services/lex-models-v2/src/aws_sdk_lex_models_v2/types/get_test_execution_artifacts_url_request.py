"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#GetTestExecutionArtifactsUrlRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.id


class GetTestExecutionArtifactsUrlRequest(TypedDict):
    test_execution_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The unique identifier of the completed test execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTestExecutionArtifactsUrlRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTestExecutionArtifactsUrlRequest:
    out: GetTestExecutionArtifactsUrlRequest = {}  # type: ignore[typeddict-item]
    return out

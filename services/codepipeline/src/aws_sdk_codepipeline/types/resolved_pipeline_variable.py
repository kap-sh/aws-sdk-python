"""Generated from Smithy shape ``com.amazonaws.codepipeline#ResolvedPipelineVariable``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.string


class ResolvedPipelineVariable(TypedDict, closed=True):
    name: NotRequired["aws_sdk_codepipeline.types.string.String"]
    """<p>The name of a pipeline-level variable.</p>"""
    resolved_value: NotRequired["aws_sdk_codepipeline.types.string.String"]
    """<p>The resolved value of a pipeline-level variable.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolvedPipelineVariable) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "resolved_value" in value:
        out["resolvedValue"] = value["resolved_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResolvedPipelineVariable:
    out: ResolvedPipelineVariable = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "resolvedValue" in data:
        out["resolved_value"] = data["resolvedValue"]
    return out

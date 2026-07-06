"""Generated from Smithy shape ``com.amazonaws.securityagent#ListArtifactsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.artifact_summary_list
    import aws_sdk_securityagent.types.next_token


class ListArtifactsOutput(TypedDict, closed=True):
    artifact_summaries: (
        "aws_sdk_securityagent.types.artifact_summary_list.ArtifactSummaryList"
    )
    """<p>The list of artifact summaries.</p>"""
    next_token: NotRequired["aws_sdk_securityagent.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListArtifactsOutput) -> dict:
    out: dict = {}
    import aws_sdk_securityagent.types.artifact_summary_list

    out["artifactSummaries"] = (
        aws_sdk_securityagent.types.artifact_summary_list.serialize_json(
            value["artifact_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListArtifactsOutput:
    out: ListArtifactsOutput = {}  # type: ignore[typeddict-item]
    if "artifactSummaries" in data:
        import aws_sdk_securityagent.types.artifact_summary_list

        out["artifact_summaries"] = (
            aws_sdk_securityagent.types.artifact_summary_list.deserialize_json(
                data["artifactSummaries"]
            )
        )
    else:
        raise DeserializationError("ListArtifactsOutput.artifact_summaries required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out

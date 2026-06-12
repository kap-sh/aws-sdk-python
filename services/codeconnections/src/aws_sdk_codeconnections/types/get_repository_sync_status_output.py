"""Generated from Smithy shape ``com.amazonaws.codeconnections#GetRepositorySyncStatusOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codeconnections.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeconnections.types.repository_sync_attempt


class GetRepositorySyncStatusOutput(TypedDict):
    latest_sync: (
        "aws_sdk_codeconnections.types.repository_sync_attempt.RepositorySyncAttempt"
    )
    """<p>The status of the latest sync returned for a specified repository and branch.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetRepositorySyncStatusOutput) -> dict:
    out: dict = {}
    import aws_sdk_codeconnections.types.repository_sync_attempt

    out["LatestSync"] = (
        aws_sdk_codeconnections.types.repository_sync_attempt.serialize_aws_json_1_0(
            value["latest_sync"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetRepositorySyncStatusOutput:
    out: GetRepositorySyncStatusOutput = {}  # type: ignore[typeddict-item]
    if "LatestSync" in data:
        import aws_sdk_codeconnections.types.repository_sync_attempt

        out["latest_sync"] = (
            aws_sdk_codeconnections.types.repository_sync_attempt.deserialize_aws_json_1_0(
                data["LatestSync"]
            )
        )
    else:
        raise DeserializationError("GetRepositorySyncStatusOutput.latest_sync required")
    return out

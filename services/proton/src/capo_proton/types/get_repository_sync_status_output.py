"""Generated from Smithy shape ``com.amazonaws.proton#GetRepositorySyncStatusOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_proton.types.repository_sync_attempt


class GetRepositorySyncStatusOutput(TypedDict, closed=True):
    latest_sync: NotRequired[
        "capo_proton.types.repository_sync_attempt.RepositorySyncAttempt"
    ]
    """<p>The repository sync status detail data that's returned by Proton.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetRepositorySyncStatusOutput) -> dict:
    out: dict = {}
    if "latest_sync" in value:
        import capo_proton.types.repository_sync_attempt

        out["latestSync"] = (
            capo_proton.types.repository_sync_attempt.serialize_aws_json_1_0(
                value["latest_sync"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetRepositorySyncStatusOutput:
    out: GetRepositorySyncStatusOutput = {}  # type: ignore[typeddict-item]
    if "latestSync" in data:
        import capo_proton.types.repository_sync_attempt

        out["latest_sync"] = (
            capo_proton.types.repository_sync_attempt.deserialize_aws_json_1_0(
                data["latestSync"]
            )
        )
    return out

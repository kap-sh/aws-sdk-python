"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ListVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__list_of_job_engine_version
    import aws_sdk_mediaconvert.types.__string


class ListVersionsResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """Optional. Use this string, provided with the response to a previous request, to request the next batch of Job engine versions."""
    versions: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of_job_engine_version.__listOfJobEngineVersion"
    ]
    """Retrieve a JSON array of all available Job engine versions and the date they expire."""


# --- restJson1 ser/de ---
def serialize_json(value: ListVersionsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "versions" in value:
        import aws_sdk_mediaconvert.types.__list_of_job_engine_version

        out["versions"] = (
            aws_sdk_mediaconvert.types.__list_of_job_engine_version.serialize_json(
                value["versions"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListVersionsResponse:
    out: ListVersionsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "versions" in data:
        import aws_sdk_mediaconvert.types.__list_of_job_engine_version

        out["versions"] = (
            aws_sdk_mediaconvert.types.__list_of_job_engine_version.deserialize_json(
                data["versions"]
            )
        )
    return out

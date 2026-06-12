"""Generated from Smithy shape ``com.amazonaws.m2#ListApplicationVersionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_m2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_m2.types.application_version_summary_list
    import aws_sdk_m2.types.next_token


class ListApplicationVersionsResponse(TypedDict):
    application_versions: "aws_sdk_m2.types.application_version_summary_list.ApplicationVersionSummaryList"
    """<p>The list of application versions.</p>"""
    next_token: NotRequired["aws_sdk_m2.types.next_token.NextToken"]
    """<p>If there are more items to return, this contains a token that is passed to a subsequent call to this operation to retrieve the next set of items.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationVersionsResponse) -> dict:
    out: dict = {}
    import aws_sdk_m2.types.application_version_summary_list

    out["applicationVersions"] = (
        aws_sdk_m2.types.application_version_summary_list.serialize_json(
            value["application_versions"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListApplicationVersionsResponse:
    out: ListApplicationVersionsResponse = {}  # type: ignore[typeddict-item]
    if "applicationVersions" in data:
        import aws_sdk_m2.types.application_version_summary_list

        out["application_versions"] = (
            aws_sdk_m2.types.application_version_summary_list.deserialize_json(
                data["applicationVersions"]
            )
        )
    else:
        raise DeserializationError(
            "ListApplicationVersionsResponse.application_versions required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out

"""Generated from Smithy shape ``com.amazonaws.m2#ListEngineVersionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_m2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_m2.types.engine_versions_summary_list
    import aws_sdk_m2.types.next_token


class ListEngineVersionsResponse(TypedDict):
    engine_versions: (
        "aws_sdk_m2.types.engine_versions_summary_list.EngineVersionsSummaryList"
    )
    """<p>Returns the engine versions.</p>"""
    next_token: NotRequired["aws_sdk_m2.types.next_token.NextToken"]
    """<p>If there are more items to return, this contains a token that is passed to a subsequent call to this operation to retrieve the next set of items.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEngineVersionsResponse) -> dict:
    out: dict = {}
    import aws_sdk_m2.types.engine_versions_summary_list

    out["engineVersions"] = (
        aws_sdk_m2.types.engine_versions_summary_list.serialize_json(
            value["engine_versions"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEngineVersionsResponse:
    out: ListEngineVersionsResponse = {}  # type: ignore[typeddict-item]
    if "engineVersions" in data:
        import aws_sdk_m2.types.engine_versions_summary_list

        out["engine_versions"] = (
            aws_sdk_m2.types.engine_versions_summary_list.deserialize_json(
                data["engineVersions"]
            )
        )
    else:
        raise DeserializationError(
            "ListEngineVersionsResponse.engine_versions required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out

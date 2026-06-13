"""Generated from Smithy shape ``com.amazonaws.odb#ListGiVersionsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_odb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_odb.types.gi_version_list


class ListGiVersionsOutput(TypedDict):
    next_token: NotRequired["str"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    gi_versions: "aws_sdk_odb.types.gi_version_list.GiVersionList"
    """<p>The list of GI versions and their properties.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListGiVersionsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_odb.types.gi_version_list

    out["giVersions"] = aws_sdk_odb.types.gi_version_list.serialize_aws_json_1_0(
        value["gi_versions"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListGiVersionsOutput:
    out: ListGiVersionsOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "giVersions" in data:
        import aws_sdk_odb.types.gi_version_list

        out["gi_versions"] = aws_sdk_odb.types.gi_version_list.deserialize_aws_json_1_0(
            data["giVersions"]
        )
    else:
        raise DeserializationError("ListGiVersionsOutput.gi_versions required")
    return out

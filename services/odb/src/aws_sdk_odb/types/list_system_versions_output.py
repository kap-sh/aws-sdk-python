"""Generated from Smithy shape ``com.amazonaws.odb#ListSystemVersionsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_odb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_odb.types.system_version_list


class ListSystemVersionsOutput(TypedDict):
    next_token: NotRequired["str"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    system_versions: "aws_sdk_odb.types.system_version_list.SystemVersionList"
    """<p>The list of system versions.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListSystemVersionsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_odb.types.system_version_list

    out["systemVersions"] = (
        aws_sdk_odb.types.system_version_list.serialize_aws_json_1_0(
            value["system_versions"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListSystemVersionsOutput:
    out: ListSystemVersionsOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "systemVersions" in data:
        import aws_sdk_odb.types.system_version_list

        out["system_versions"] = (
            aws_sdk_odb.types.system_version_list.deserialize_aws_json_1_0(
                data["systemVersions"]
            )
        )
    else:
        raise DeserializationError("ListSystemVersionsOutput.system_versions required")
    return out

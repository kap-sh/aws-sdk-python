"""Generated from Smithy shape ``com.amazonaws.synthetics#DescribeRuntimeVersionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.runtime_version_list
    import aws_sdk_synthetics.types.token


class DescribeRuntimeVersionsResponse(TypedDict):
    runtime_versions: NotRequired[
        "aws_sdk_synthetics.types.runtime_version_list.RuntimeVersionList"
    ]
    """<p>An array of objects that display the details about each Synthetics canary runtime version.</p>"""
    next_token: NotRequired["aws_sdk_synthetics.types.token.Token"]
    """<p>A token that indicates that there is more data available. You can use this token in a subsequent <code>DescribeRuntimeVersions</code> operation to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRuntimeVersionsResponse) -> dict:
    out: dict = {}
    if "runtime_versions" in value:
        import aws_sdk_synthetics.types.runtime_version_list

        out["RuntimeVersions"] = (
            aws_sdk_synthetics.types.runtime_version_list.serialize_json(
                value["runtime_versions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeRuntimeVersionsResponse:
    out: DescribeRuntimeVersionsResponse = {}  # type: ignore[typeddict-item]
    if "RuntimeVersions" in data:
        import aws_sdk_synthetics.types.runtime_version_list

        out["runtime_versions"] = (
            aws_sdk_synthetics.types.runtime_version_list.deserialize_json(
                data["RuntimeVersions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

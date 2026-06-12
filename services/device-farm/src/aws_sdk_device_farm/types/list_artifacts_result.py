"""Generated from Smithy shape ``com.amazonaws.devicefarm#ListArtifactsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.artifacts
    import aws_sdk_device_farm.types.pagination_token


class ListArtifactsResult(TypedDict):
    artifacts: NotRequired["aws_sdk_device_farm.types.artifacts.Artifacts"]
    """<p>Information about the artifacts.</p>"""
    next_token: NotRequired[
        "aws_sdk_device_farm.types.pagination_token.PaginationToken"
    ]
    """<p>If the number of items that are returned is significantly large, this is an identifier that is also returned. It can be used in a subsequent call to this operation to return the next set of items in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListArtifactsResult) -> dict:
    out: dict = {}
    if "artifacts" in value:
        import aws_sdk_device_farm.types.artifacts

        out["artifacts"] = aws_sdk_device_farm.types.artifacts.serialize_aws_json_1_1(
            value["artifacts"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListArtifactsResult:
    out: ListArtifactsResult = {}  # type: ignore[typeddict-item]
    if "artifacts" in data:
        import aws_sdk_device_farm.types.artifacts

        out["artifacts"] = aws_sdk_device_farm.types.artifacts.deserialize_aws_json_1_1(
            data["artifacts"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out

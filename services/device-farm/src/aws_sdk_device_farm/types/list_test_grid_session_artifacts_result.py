"""Generated from Smithy shape ``com.amazonaws.devicefarm#ListTestGridSessionArtifactsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.pagination_token
    import aws_sdk_device_farm.types.test_grid_session_artifacts


class ListTestGridSessionArtifactsResult(TypedDict):
    artifacts: NotRequired[
        "aws_sdk_device_farm.types.test_grid_session_artifacts.TestGridSessionArtifacts"
    ]
    """<p>A list of test grid session artifacts for a <a>TestGridSession</a>.</p>"""
    next_token: NotRequired[
        "aws_sdk_device_farm.types.pagination_token.PaginationToken"
    ]
    """<p>Pagination token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTestGridSessionArtifactsResult) -> dict:
    out: dict = {}
    if "artifacts" in value:
        import aws_sdk_device_farm.types.test_grid_session_artifacts

        out["artifacts"] = (
            aws_sdk_device_farm.types.test_grid_session_artifacts.serialize_aws_json_1_1(
                value["artifacts"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTestGridSessionArtifactsResult:
    out: ListTestGridSessionArtifactsResult = {}  # type: ignore[typeddict-item]
    if "artifacts" in data:
        import aws_sdk_device_farm.types.test_grid_session_artifacts

        out["artifacts"] = (
            aws_sdk_device_farm.types.test_grid_session_artifacts.deserialize_aws_json_1_1(
                data["artifacts"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out

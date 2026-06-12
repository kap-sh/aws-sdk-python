"""Generated from Smithy shape ``com.amazonaws.devicefarm#ListTestGridProjectsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.pagination_token
    import aws_sdk_device_farm.types.test_grid_projects


class ListTestGridProjectsResult(TypedDict):
    test_grid_projects: NotRequired[
        "aws_sdk_device_farm.types.test_grid_projects.TestGridProjects"
    ]
    """<p>The list of TestGridProjects, based on a <a>ListTestGridProjectsRequest</a>.</p>"""
    next_token: NotRequired[
        "aws_sdk_device_farm.types.pagination_token.PaginationToken"
    ]
    """<p>Used for pagination. Pass into <a>ListTestGridProjects</a> to get more results in a paginated request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTestGridProjectsResult) -> dict:
    out: dict = {}
    if "test_grid_projects" in value:
        import aws_sdk_device_farm.types.test_grid_projects

        out["testGridProjects"] = (
            aws_sdk_device_farm.types.test_grid_projects.serialize_aws_json_1_1(
                value["test_grid_projects"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTestGridProjectsResult:
    out: ListTestGridProjectsResult = {}  # type: ignore[typeddict-item]
    if "testGridProjects" in data:
        import aws_sdk_device_farm.types.test_grid_projects

        out["test_grid_projects"] = (
            aws_sdk_device_farm.types.test_grid_projects.deserialize_aws_json_1_1(
                data["testGridProjects"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out

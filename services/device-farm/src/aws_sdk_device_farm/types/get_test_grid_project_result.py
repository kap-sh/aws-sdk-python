"""Generated from Smithy shape ``com.amazonaws.devicefarm#GetTestGridProjectResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.test_grid_project


class GetTestGridProjectResult(TypedDict, closed=True):
    test_grid_project: NotRequired[
        "aws_sdk_device_farm.types.test_grid_project.TestGridProject"
    ]
    """<p>A <a>TestGridProject</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTestGridProjectResult) -> dict:
    out: dict = {}
    if "test_grid_project" in value:
        import aws_sdk_device_farm.types.test_grid_project

        out["testGridProject"] = (
            aws_sdk_device_farm.types.test_grid_project.serialize_aws_json_1_1(
                value["test_grid_project"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTestGridProjectResult:
    out: GetTestGridProjectResult = {}  # type: ignore[typeddict-item]
    if "testGridProject" in data:
        import aws_sdk_device_farm.types.test_grid_project

        out["test_grid_project"] = (
            aws_sdk_device_farm.types.test_grid_project.deserialize_aws_json_1_1(
                data["testGridProject"]
            )
        )
    return out

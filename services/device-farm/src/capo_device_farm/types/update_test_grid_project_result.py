"""Generated from Smithy shape ``com.amazonaws.devicefarm#UpdateTestGridProjectResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.test_grid_project


class UpdateTestGridProjectResult(TypedDict, closed=True):
    test_grid_project: NotRequired[
        "capo_device_farm.types.test_grid_project.TestGridProject"
    ]
    """<p>The project, including updated information.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTestGridProjectResult) -> dict:
    out: dict = {}
    if "test_grid_project" in value:
        import capo_device_farm.types.test_grid_project

        out["testGridProject"] = (
            capo_device_farm.types.test_grid_project.serialize_aws_json_1_1(
                value["test_grid_project"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateTestGridProjectResult:
    out: UpdateTestGridProjectResult = {}  # type: ignore[typeddict-item]
    if "testGridProject" in data:
        import capo_device_farm.types.test_grid_project

        out["test_grid_project"] = (
            capo_device_farm.types.test_grid_project.deserialize_aws_json_1_1(
                data["testGridProject"]
            )
        )
    return out

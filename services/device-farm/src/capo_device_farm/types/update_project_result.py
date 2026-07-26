"""Generated from Smithy shape ``com.amazonaws.devicefarm#UpdateProjectResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.project


class UpdateProjectResult(TypedDict, closed=True):
    project: NotRequired["capo_device_farm.types.project.Project"]
    """<p>The project to update.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateProjectResult) -> dict:
    out: dict = {}
    if "project" in value:
        import capo_device_farm.types.project

        out["project"] = capo_device_farm.types.project.serialize_aws_json_1_1(
            value["project"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateProjectResult:
    out: UpdateProjectResult = {}  # type: ignore[typeddict-item]
    if "project" in data:
        import capo_device_farm.types.project

        out["project"] = capo_device_farm.types.project.deserialize_aws_json_1_1(
            data["project"]
        )
    return out

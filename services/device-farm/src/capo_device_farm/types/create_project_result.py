"""Generated from Smithy shape ``com.amazonaws.devicefarm#CreateProjectResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.project


class CreateProjectResult(TypedDict, closed=True):
    project: NotRequired["capo_device_farm.types.project.Project"]
    """<p>The newly created project.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateProjectResult) -> dict:
    out: dict = {}
    if "project" in value:
        import capo_device_farm.types.project

        out["project"] = capo_device_farm.types.project.serialize_aws_json_1_1(
            value["project"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateProjectResult:
    out: CreateProjectResult = {}  # type: ignore[typeddict-item]
    if "project" in data:
        import capo_device_farm.types.project

        out["project"] = capo_device_farm.types.project.deserialize_aws_json_1_1(
            data["project"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.devicefarm#GetProjectResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.project


class GetProjectResult(TypedDict, closed=True):
    project: NotRequired["capo_device_farm.types.project.Project"]
    """<p>The project to get information about.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetProjectResult) -> dict:
    out: dict = {}
    if "project" in value:
        import capo_device_farm.types.project

        out["project"] = capo_device_farm.types.project.serialize_aws_json_1_1(
            value["project"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetProjectResult:
    out: GetProjectResult = {}  # type: ignore[typeddict-item]
    if "project" in data:
        import capo_device_farm.types.project

        out["project"] = capo_device_farm.types.project.deserialize_aws_json_1_1(
            data["project"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.devicefarm#CreateProjectResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.project


class CreateProjectResult(TypedDict):
    project: NotRequired["aws_sdk_device_farm.types.project.Project"]
    """<p>The newly created project.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateProjectResult) -> dict:
    out: dict = {}
    if "project" in value:
        import aws_sdk_device_farm.types.project

        out["project"] = aws_sdk_device_farm.types.project.serialize_aws_json_1_1(
            value["project"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateProjectResult:
    out: CreateProjectResult = {}  # type: ignore[typeddict-item]
    if "project" in data:
        import aws_sdk_device_farm.types.project

        out["project"] = aws_sdk_device_farm.types.project.deserialize_aws_json_1_1(
            data["project"]
        )
    return out

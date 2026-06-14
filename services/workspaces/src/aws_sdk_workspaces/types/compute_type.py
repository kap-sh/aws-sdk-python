"""Generated from Smithy shape ``com.amazonaws.workspaces#ComputeType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.compute


class ComputeType(TypedDict):
    name: NotRequired["aws_sdk_workspaces.types.compute.Compute"]
    """<p>The compute type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComputeType) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_workspaces.types.compute

        out["Name"] = aws_sdk_workspaces.types.compute.serialize_aws_json_1_1(
            value["name"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ComputeType:
    out: ComputeType = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import aws_sdk_workspaces.types.compute

        out["name"] = aws_sdk_workspaces.types.compute.deserialize_aws_json_1_1(
            data["Name"]
        )
    return out

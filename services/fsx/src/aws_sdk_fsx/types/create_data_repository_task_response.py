"""Generated from Smithy shape ``com.amazonaws.fsx#CreateDataRepositoryTaskResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.data_repository_task


class CreateDataRepositoryTaskResponse(TypedDict):
    data_repository_task: NotRequired[
        "aws_sdk_fsx.types.data_repository_task.DataRepositoryTask"
    ]
    """<p>The description of the data repository task that you just created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDataRepositoryTaskResponse) -> dict:
    out: dict = {}
    if "data_repository_task" in value:
        import aws_sdk_fsx.types.data_repository_task

        out["DataRepositoryTask"] = (
            aws_sdk_fsx.types.data_repository_task.serialize_aws_json_1_1(
                value["data_repository_task"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDataRepositoryTaskResponse:
    out: CreateDataRepositoryTaskResponse = {}  # type: ignore[typeddict-item]
    if "DataRepositoryTask" in data:
        import aws_sdk_fsx.types.data_repository_task

        out["data_repository_task"] = (
            aws_sdk_fsx.types.data_repository_task.deserialize_aws_json_1_1(
                data["DataRepositoryTask"]
            )
        )
    return out

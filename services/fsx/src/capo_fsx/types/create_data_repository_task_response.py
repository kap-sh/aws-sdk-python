"""Generated from Smithy shape ``com.amazonaws.fsx#CreateDataRepositoryTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.data_repository_task


class CreateDataRepositoryTaskResponse(TypedDict, closed=True):
    data_repository_task: NotRequired[
        "capo_fsx.types.data_repository_task.DataRepositoryTask"
    ]
    """<p>The description of the data repository task that you just created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDataRepositoryTaskResponse) -> dict:
    out: dict = {}
    if "data_repository_task" in value:
        import capo_fsx.types.data_repository_task

        out["DataRepositoryTask"] = (
            capo_fsx.types.data_repository_task.serialize_aws_json_1_1(
                value["data_repository_task"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDataRepositoryTaskResponse:
    out: CreateDataRepositoryTaskResponse = {}  # type: ignore[typeddict-item]
    if "DataRepositoryTask" in data:
        import capo_fsx.types.data_repository_task

        out["data_repository_task"] = (
            capo_fsx.types.data_repository_task.deserialize_aws_json_1_1(
                data["DataRepositoryTask"]
            )
        )
    return out

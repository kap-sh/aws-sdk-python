"""Generated from Smithy shape ``com.amazonaws.translate#DeleteParallelDataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_translate.types.parallel_data_status
    import capo_translate.types.resource_name


class DeleteParallelDataResponse(TypedDict, closed=True):
    name: NotRequired["capo_translate.types.resource_name.ResourceName"]
    """<p>The name of the parallel data resource that is being deleted.</p>"""
    status: NotRequired["capo_translate.types.parallel_data_status.ParallelDataStatus"]
    """<p>The status of the parallel data deletion.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteParallelDataResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import capo_translate.types.parallel_data_status

        out["Status"] = (
            capo_translate.types.parallel_data_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteParallelDataResponse:
    out: DeleteParallelDataResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Status" in data:
        import capo_translate.types.parallel_data_status

        out["status"] = (
            capo_translate.types.parallel_data_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    return out

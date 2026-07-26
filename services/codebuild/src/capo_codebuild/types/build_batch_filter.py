"""Generated from Smithy shape ``com.amazonaws.codebuild#BuildBatchFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.status_type


class BuildBatchFilter(TypedDict, closed=True):
    status: NotRequired["capo_codebuild.types.status_type.StatusType"]
    """<p>The status of the batch builds to retrieve. Only batch builds that have this status will be retrieved.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BuildBatchFilter) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_codebuild.types.status_type

        out["status"] = capo_codebuild.types.status_type.serialize_aws_json_1_1(
            value["status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BuildBatchFilter:
    out: BuildBatchFilter = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import capo_codebuild.types.status_type

        out["status"] = capo_codebuild.types.status_type.deserialize_aws_json_1_1(
            data["status"]
        )
    return out

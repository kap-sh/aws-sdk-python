"""Generated from Smithy shape ``com.amazonaws.opensearch#DescribeDomainChangeProgressResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.change_progress_status_details


class DescribeDomainChangeProgressResponse(TypedDict):
    change_progress_status: NotRequired[
        "aws_sdk_opensearch.types.change_progress_status_details.ChangeProgressStatusDetails"
    ]
    """<p>Container for information about the stages of a configuration change happening on a domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDomainChangeProgressResponse) -> dict:
    out: dict = {}
    if "change_progress_status" in value:
        import aws_sdk_opensearch.types.change_progress_status_details

        out["ChangeProgressStatus"] = (
            aws_sdk_opensearch.types.change_progress_status_details.serialize_json(
                value["change_progress_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeDomainChangeProgressResponse:
    out: DescribeDomainChangeProgressResponse = {}  # type: ignore[typeddict-item]
    if "ChangeProgressStatus" in data:
        import aws_sdk_opensearch.types.change_progress_status_details

        out["change_progress_status"] = (
            aws_sdk_opensearch.types.change_progress_status_details.deserialize_json(
                data["ChangeProgressStatus"]
            )
        )
    return out

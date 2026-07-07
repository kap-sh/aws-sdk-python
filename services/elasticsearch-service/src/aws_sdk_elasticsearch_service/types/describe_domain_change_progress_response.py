"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DescribeDomainChangeProgressResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.change_progress_status_details


class DescribeDomainChangeProgressResponse(TypedDict, closed=True):
    change_progress_status: NotRequired[
        "aws_sdk_elasticsearch_service.types.change_progress_status_details.ChangeProgressStatusDetails"
    ]
    """<p>Progress information for the configuration change that is requested in the <code>DescribeDomainChangeProgress</code> request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDomainChangeProgressResponse) -> dict:
    out: dict = {}
    if "change_progress_status" in value:
        import aws_sdk_elasticsearch_service.types.change_progress_status_details

        out["ChangeProgressStatus"] = (
            aws_sdk_elasticsearch_service.types.change_progress_status_details.serialize_json(
                value["change_progress_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeDomainChangeProgressResponse:
    out: DescribeDomainChangeProgressResponse = {}  # type: ignore[typeddict-item]
    if "ChangeProgressStatus" in data:
        import aws_sdk_elasticsearch_service.types.change_progress_status_details

        out["change_progress_status"] = (
            aws_sdk_elasticsearch_service.types.change_progress_status_details.deserialize_json(
                data["ChangeProgressStatus"]
            )
        )
    return out

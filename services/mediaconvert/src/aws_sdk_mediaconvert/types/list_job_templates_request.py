"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ListJobTemplatesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min1_max20
    import aws_sdk_mediaconvert.types.__string
    import aws_sdk_mediaconvert.types.job_template_list_by
    import aws_sdk_mediaconvert.types.order


class ListJobTemplatesRequest(TypedDict, closed=True):
    category: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """Optionally, specify a job template category to limit responses to only job templates from that category."""
    list_by: NotRequired[
        "aws_sdk_mediaconvert.types.job_template_list_by.JobTemplateListBy"
    ]
    """Optional. When you request a list of job templates, you can choose to list them alphabetically by NAME or chronologically by CREATION_DATE. If you don't specify, the service will list them by name."""
    max_results: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1_max20.__integerMin1Max20"
    ]
    """Optional. Number of job templates, up to twenty, that will be returned at one time."""
    next_token: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """Use this string, provided with the response to a previous request, to request the next batch of job templates."""
    order: NotRequired["aws_sdk_mediaconvert.types.order.Order"]
    """Optional. When you request lists of resources, you can specify whether they are sorted in ASCENDING or DESCENDING order. Default varies by resource."""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobTemplatesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListJobTemplatesRequest:
    out: ListJobTemplatesRequest = {}  # type: ignore[typeddict-item]
    return out

"""Generated from Smithy shape ``com.amazonaws.emrcontainers#ListJobTemplatesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.date
    import aws_sdk_emr_containers.types.java_integer
    import aws_sdk_emr_containers.types.next_token


class ListJobTemplatesRequest(TypedDict):
    created_after: NotRequired["aws_sdk_emr_containers.types.date.Date"]
    """<p>The date and time after which the job templates were created.</p>"""
    created_before: NotRequired["aws_sdk_emr_containers.types.date.Date"]
    """<p> The date and time before which the job templates were created.</p>"""
    max_results: NotRequired["aws_sdk_emr_containers.types.java_integer.JavaInteger"]
    """<p> The maximum number of job templates that can be listed.</p>"""
    next_token: NotRequired["aws_sdk_emr_containers.types.next_token.NextToken"]
    """<p> The token for the next set of job templates to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobTemplatesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListJobTemplatesRequest:
    out: ListJobTemplatesRequest = {}  # type: ignore[typeddict-item]
    return out

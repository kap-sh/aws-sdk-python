"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ListJobTemplatesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__list_of_job_template
    import aws_sdk_mediaconvert.types.__string


class ListJobTemplatesResponse(TypedDict, closed=True):
    job_templates: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of_job_template.__listOfJobTemplate"
    ]
    """List of Job templates."""
    next_token: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """Use this string to request the next batch of job templates."""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobTemplatesResponse) -> dict:
    out: dict = {}
    if "job_templates" in value:
        import aws_sdk_mediaconvert.types.__list_of_job_template

        out["jobTemplates"] = (
            aws_sdk_mediaconvert.types.__list_of_job_template.serialize_json(
                value["job_templates"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListJobTemplatesResponse:
    out: ListJobTemplatesResponse = {}  # type: ignore[typeddict-item]
    if "jobTemplates" in data:
        import aws_sdk_mediaconvert.types.__list_of_job_template

        out["job_templates"] = (
            aws_sdk_mediaconvert.types.__list_of_job_template.deserialize_json(
                data["jobTemplates"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out

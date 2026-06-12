"""Generated from Smithy shape ``com.amazonaws.emrcontainers#ListJobTemplatesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.job_templates
    import aws_sdk_emr_containers.types.next_token


class ListJobTemplatesResponse(TypedDict):
    templates: NotRequired["aws_sdk_emr_containers.types.job_templates.JobTemplates"]
    """<p>This output lists information about the specified job templates.</p>"""
    next_token: NotRequired["aws_sdk_emr_containers.types.next_token.NextToken"]
    """<p> This output displays the token for the next set of job templates.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobTemplatesResponse) -> dict:
    out: dict = {}
    if "templates" in value:
        import aws_sdk_emr_containers.types.job_templates

        out["templates"] = aws_sdk_emr_containers.types.job_templates.serialize_json(
            value["templates"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListJobTemplatesResponse:
    out: ListJobTemplatesResponse = {}  # type: ignore[typeddict-item]
    if "templates" in data:
        import aws_sdk_emr_containers.types.job_templates

        out["templates"] = aws_sdk_emr_containers.types.job_templates.deserialize_json(
            data["templates"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out

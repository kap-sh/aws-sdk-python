"""Generated from Smithy shape ``com.amazonaws.datazone#ProjectPolicyGrantPrincipal``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.project_designation
    import aws_sdk_datazone.types.project_grant_filter
    import aws_sdk_datazone.types.project_id


class ProjectPolicyGrantPrincipal(TypedDict):
    project_designation: "aws_sdk_datazone.types.project_designation.ProjectDesignation"
    """<p>The project designation of the project policy grant principal.</p>"""
    project_identifier: NotRequired["aws_sdk_datazone.types.project_id.ProjectId"]
    """<p>The project ID of the project policy grant principal.</p>"""
    project_grant_filter: NotRequired[
        "aws_sdk_datazone.types.project_grant_filter.ProjectGrantFilter"
    ]
    """<p>The project grant filter of the project policy grant principal.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProjectPolicyGrantPrincipal) -> dict:
    out: dict = {}
    import aws_sdk_datazone.types.project_designation

    out["projectDesignation"] = (
        aws_sdk_datazone.types.project_designation.serialize_json(
            value["project_designation"]
        )
    )
    if "project_identifier" in value:
        out["projectIdentifier"] = value["project_identifier"]
    if "project_grant_filter" in value:
        import aws_sdk_datazone.types.project_grant_filter

        out["projectGrantFilter"] = (
            aws_sdk_datazone.types.project_grant_filter.serialize_json(
                value["project_grant_filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> ProjectPolicyGrantPrincipal:
    out: ProjectPolicyGrantPrincipal = {}  # type: ignore[typeddict-item]
    if "projectDesignation" in data:
        import aws_sdk_datazone.types.project_designation

        out["project_designation"] = (
            aws_sdk_datazone.types.project_designation.deserialize_json(
                data["projectDesignation"]
            )
        )
    else:
        raise DeserializationError(
            "ProjectPolicyGrantPrincipal.project_designation required"
        )
    if "projectIdentifier" in data:
        out["project_identifier"] = data["projectIdentifier"]
    if "projectGrantFilter" in data:
        import aws_sdk_datazone.types.project_grant_filter

        out["project_grant_filter"] = (
            aws_sdk_datazone.types.project_grant_filter.deserialize_json(
                data["projectGrantFilter"]
            )
        )
    return out

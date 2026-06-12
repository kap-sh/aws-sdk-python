"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ListApplicationAssignmentsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.application_assignments_list
    import aws_sdk_sso_admin.types.token


class ListApplicationAssignmentsResponse(TypedDict):
    application_assignments: NotRequired[
        "aws_sdk_sso_admin.types.application_assignments_list.ApplicationAssignmentsList"
    ]
    """<p>The list of users assigned to an application.</p>"""
    next_token: NotRequired["aws_sdk_sso_admin.types.token.Token"]
    """<p>If present, this value indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>. This indicates that this is the last page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListApplicationAssignmentsResponse) -> dict:
    out: dict = {}
    if "application_assignments" in value:
        import aws_sdk_sso_admin.types.application_assignments_list

        out["ApplicationAssignments"] = (
            aws_sdk_sso_admin.types.application_assignments_list.serialize_aws_json_1_1(
                value["application_assignments"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListApplicationAssignmentsResponse:
    out: ListApplicationAssignmentsResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationAssignments" in data:
        import aws_sdk_sso_admin.types.application_assignments_list

        out["application_assignments"] = (
            aws_sdk_sso_admin.types.application_assignments_list.deserialize_aws_json_1_1(
                data["ApplicationAssignments"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

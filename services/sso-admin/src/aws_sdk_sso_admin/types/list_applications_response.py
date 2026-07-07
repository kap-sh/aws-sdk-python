"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ListApplicationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.application_list
    import aws_sdk_sso_admin.types.token


class ListApplicationsResponse(TypedDict, closed=True):
    applications: NotRequired[
        "aws_sdk_sso_admin.types.application_list.ApplicationList"
    ]
    """<p>Retrieves all applications associated with the instance.</p>"""
    next_token: NotRequired["aws_sdk_sso_admin.types.token.Token"]
    """<p>If present, this value indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>. This indicates that this is the last page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListApplicationsResponse) -> dict:
    out: dict = {}
    if "applications" in value:
        import aws_sdk_sso_admin.types.application_list

        out["Applications"] = (
            aws_sdk_sso_admin.types.application_list.serialize_aws_json_1_1(
                value["applications"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListApplicationsResponse:
    out: ListApplicationsResponse = {}  # type: ignore[typeddict-item]
    if "Applications" in data:
        import aws_sdk_sso_admin.types.application_list

        out["applications"] = (
            aws_sdk_sso_admin.types.application_list.deserialize_aws_json_1_1(
                data["Applications"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

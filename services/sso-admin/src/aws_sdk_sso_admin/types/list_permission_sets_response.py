"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ListPermissionSetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.permission_set_list
    import aws_sdk_sso_admin.types.token


class ListPermissionSetsResponse(TypedDict, closed=True):
    permission_sets: NotRequired[
        "aws_sdk_sso_admin.types.permission_set_list.PermissionSetList"
    ]
    """<p>Defines the level of access on an Amazon Web Services account.</p>"""
    next_token: NotRequired["aws_sdk_sso_admin.types.token.Token"]
    """<p>The pagination token for the list API. Initially the value is null. Use the output of previous API calls to make subsequent calls.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPermissionSetsResponse) -> dict:
    out: dict = {}
    if "permission_sets" in value:
        import aws_sdk_sso_admin.types.permission_set_list

        out["PermissionSets"] = (
            aws_sdk_sso_admin.types.permission_set_list.serialize_aws_json_1_1(
                value["permission_sets"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPermissionSetsResponse:
    out: ListPermissionSetsResponse = {}  # type: ignore[typeddict-item]
    if "PermissionSets" in data:
        import aws_sdk_sso_admin.types.permission_set_list

        out["permission_sets"] = (
            aws_sdk_sso_admin.types.permission_set_list.deserialize_aws_json_1_1(
                data["PermissionSets"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

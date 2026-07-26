"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ListInstancesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.instance_list
    import capo_sso_admin.types.token


class ListInstancesResponse(TypedDict, closed=True):
    instances: NotRequired["capo_sso_admin.types.instance_list.InstanceList"]
    """<p>Lists the IAM Identity Center instances that the caller has access to.</p>"""
    next_token: NotRequired["capo_sso_admin.types.token.Token"]
    """<p>The pagination token for the list API. Initially the value is null. Use the output of previous API calls to make subsequent calls.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListInstancesResponse) -> dict:
    out: dict = {}
    if "instances" in value:
        import capo_sso_admin.types.instance_list

        out["Instances"] = capo_sso_admin.types.instance_list.serialize_aws_json_1_1(
            value["instances"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListInstancesResponse:
    out: ListInstancesResponse = {}  # type: ignore[typeddict-item]
    if "Instances" in data:
        import capo_sso_admin.types.instance_list

        out["instances"] = capo_sso_admin.types.instance_list.deserialize_aws_json_1_1(
            data["Instances"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

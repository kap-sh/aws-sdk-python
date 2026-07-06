"""Generated from Smithy shape ``com.amazonaws.organizations#ListDelegatedAdministratorsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_organizations.types.delegated_administrators
    import aws_sdk_organizations.types.next_token


class ListDelegatedAdministratorsResponse(TypedDict, closed=True):
    delegated_administrators: NotRequired[
        "aws_sdk_organizations.types.delegated_administrators.DelegatedAdministrators"
    ]
    """<p>The list of delegated administrators in your organization.</p>"""
    next_token: NotRequired["aws_sdk_organizations.types.next_token.NextToken"]
    """<p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDelegatedAdministratorsResponse) -> dict:
    out: dict = {}
    if "delegated_administrators" in value:
        import aws_sdk_organizations.types.delegated_administrators

        out["DelegatedAdministrators"] = (
            aws_sdk_organizations.types.delegated_administrators.serialize_aws_json_1_1(
                value["delegated_administrators"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDelegatedAdministratorsResponse:
    out: ListDelegatedAdministratorsResponse = {}  # type: ignore[typeddict-item]
    if "DelegatedAdministrators" in data:
        import aws_sdk_organizations.types.delegated_administrators

        out["delegated_administrators"] = (
            aws_sdk_organizations.types.delegated_administrators.deserialize_aws_json_1_1(
                data["DelegatedAdministrators"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

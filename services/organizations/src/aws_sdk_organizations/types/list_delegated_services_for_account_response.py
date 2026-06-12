"""Generated from Smithy shape ``com.amazonaws.organizations#ListDelegatedServicesForAccountResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_organizations.types.delegated_services
    import aws_sdk_organizations.types.next_token


class ListDelegatedServicesForAccountResponse(TypedDict):
    delegated_services: NotRequired[
        "aws_sdk_organizations.types.delegated_services.DelegatedServices"
    ]
    """<p>The services for which the account is a delegated administrator.</p>"""
    next_token: NotRequired["aws_sdk_organizations.types.next_token.NextToken"]
    """<p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDelegatedServicesForAccountResponse) -> dict:
    out: dict = {}
    if "delegated_services" in value:
        import aws_sdk_organizations.types.delegated_services

        out["DelegatedServices"] = (
            aws_sdk_organizations.types.delegated_services.serialize_aws_json_1_1(
                value["delegated_services"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDelegatedServicesForAccountResponse:
    out: ListDelegatedServicesForAccountResponse = {}  # type: ignore[typeddict-item]
    if "DelegatedServices" in data:
        import aws_sdk_organizations.types.delegated_services

        out["delegated_services"] = (
            aws_sdk_organizations.types.delegated_services.deserialize_aws_json_1_1(
                data["DelegatedServices"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

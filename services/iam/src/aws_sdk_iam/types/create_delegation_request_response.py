"""Generated from Smithy shape ``com.amazonaws.iam#CreateDelegationRequestResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.console_deep_link_type
    import aws_sdk_iam.types.delegation_request_id_type


class CreateDelegationRequestResponse(TypedDict, closed=True):
    console_deep_link: NotRequired[
        "aws_sdk_iam.types.console_deep_link_type.consoleDeepLinkType"
    ]
    """<p>A deep link URL to the Amazon Web Services Management Console for managing the delegation request.</p> <p>For a console based workflow, partners should redirect the customer to this URL. If the customer is not logged in to any Amazon Web Services account, the Amazon Web Services workflow will automatically direct the customer to log in and then display the delegation request approval page.</p>"""
    delegation_request_id: NotRequired[
        "aws_sdk_iam.types.delegation_request_id_type.delegationRequestIdType"
    ]
    """<p>The unique identifier for the created delegation request.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateDelegationRequestResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "console_deep_link" in value:
        pairs.append((f"{prefix}.ConsoleDeepLink", str(value["console_deep_link"])))
    if "delegation_request_id" in value:
        pairs.append(
            (f"{prefix}.DelegationRequestId", str(value["delegation_request_id"]))
        )


def deserialize_query(el: Element) -> CreateDelegationRequestResponse:
    out: CreateDelegationRequestResponse = {}  # type: ignore[typeddict-item]
    child_console_deep_link = el.find("ConsoleDeepLink")
    if child_console_deep_link is not None:
        out["console_deep_link"] = str(child_console_deep_link.text or "")
    child_delegation_request_id = el.find("DelegationRequestId")
    if child_delegation_request_id is not None:
        out["delegation_request_id"] = str(child_delegation_request_id.text or "")
    return out

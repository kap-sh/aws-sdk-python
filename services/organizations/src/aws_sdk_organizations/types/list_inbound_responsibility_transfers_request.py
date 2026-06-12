"""Generated from Smithy shape ``com.amazonaws.organizations#ListInboundResponsibilityTransfersRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_organizations.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_organizations.types.max_results
    import aws_sdk_organizations.types.next_token
    import aws_sdk_organizations.types.responsibility_transfer_id
    import aws_sdk_organizations.types.responsibility_transfer_type


class ListInboundResponsibilityTransfersRequest(TypedDict):
    type: "aws_sdk_organizations.types.responsibility_transfer_type.ResponsibilityTransferType"
    """<p>The type of responsibility. Currently, only <code>BILLING</code> is supported.</p>"""
    id: NotRequired[
        "aws_sdk_organizations.types.responsibility_transfer_id.ResponsibilityTransferId"
    ]
    """<p>ID for the transfer.</p>"""
    next_token: NotRequired["aws_sdk_organizations.types.next_token.NextToken"]
    """<p>The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value of the previous call's <code>NextToken</code> response to indicate where the output should continue from.</p>"""
    max_results: NotRequired["aws_sdk_organizations.types.max_results.MaxResults"]
    """<p>The maximum number of items to return in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that you can retrieve the remaining results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListInboundResponsibilityTransfersRequest) -> dict:
    out: dict = {}
    import aws_sdk_organizations.types.responsibility_transfer_type

    out["Type"] = (
        aws_sdk_organizations.types.responsibility_transfer_type.serialize_aws_json_1_1(
            value["type"]
        )
    )
    if "id" in value:
        out["Id"] = value["id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListInboundResponsibilityTransfersRequest:
    out: ListInboundResponsibilityTransfersRequest = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_organizations.types.responsibility_transfer_type

        out["type"] = (
            aws_sdk_organizations.types.responsibility_transfer_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    else:
        raise DeserializationError(
            "ListInboundResponsibilityTransfersRequest.type required"
        )
    if "Id" in data:
        out["id"] = data["Id"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out

"""Generated from Smithy shape ``com.amazonaws.artifact#ListCustomerAgreementsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_artifact.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_artifact.types.customer_agreement_list
    import aws_sdk_artifact.types.next_token_attribute


class ListCustomerAgreementsResponse(TypedDict):
    customer_agreements: (
        "aws_sdk_artifact.types.customer_agreement_list.CustomerAgreementList"
    )
    """<p>List of customer-agreement resources.</p>"""
    next_token: NotRequired[
        "aws_sdk_artifact.types.next_token_attribute.NextTokenAttribute"
    ]
    """<p>Pagination token to request the next page of resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCustomerAgreementsResponse) -> dict:
    out: dict = {}
    import aws_sdk_artifact.types.customer_agreement_list

    out["customerAgreements"] = (
        aws_sdk_artifact.types.customer_agreement_list.serialize_json(
            value["customer_agreements"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCustomerAgreementsResponse:
    out: ListCustomerAgreementsResponse = {}  # type: ignore[typeddict-item]
    if "customerAgreements" in data:
        import aws_sdk_artifact.types.customer_agreement_list

        out["customer_agreements"] = (
            aws_sdk_artifact.types.customer_agreement_list.deserialize_json(
                data["customerAgreements"]
            )
        )
    else:
        raise DeserializationError(
            "ListCustomerAgreementsResponse.customer_agreements required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out

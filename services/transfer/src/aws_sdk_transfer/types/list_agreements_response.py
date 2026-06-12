"""Generated from Smithy shape ``com.amazonaws.transfer#ListAgreementsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.listed_agreements
    import aws_sdk_transfer.types.next_token


class ListAgreementsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_transfer.types.next_token.NextToken"]
    """<p>Returns a token that you can use to call <code>ListAgreements</code> again and receive additional results, if there are any.</p>"""
    agreements: "aws_sdk_transfer.types.listed_agreements.ListedAgreements"
    """<p>Returns an array, where each item contains the details of an agreement.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAgreementsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import aws_sdk_transfer.types.listed_agreements

    out["Agreements"] = aws_sdk_transfer.types.listed_agreements.serialize_aws_json_1_1(
        value["agreements"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAgreementsResponse:
    out: ListAgreementsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Agreements" in data:
        import aws_sdk_transfer.types.listed_agreements

        out["agreements"] = (
            aws_sdk_transfer.types.listed_agreements.deserialize_aws_json_1_1(
                data["Agreements"]
            )
        )
    else:
        raise DeserializationError("ListAgreementsResponse.agreements required")
    return out

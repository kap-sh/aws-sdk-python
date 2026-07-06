"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#Acceptor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.aws_account_id


class Acceptor(TypedDict, closed=True):
    account_id: NotRequired[
        "aws_sdk_marketplace_agreement.types.aws_account_id.AWSAccountId"
    ]
    """<p>The AWS account ID of the acceptor.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Acceptor) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Acceptor:
    out: Acceptor = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    return out

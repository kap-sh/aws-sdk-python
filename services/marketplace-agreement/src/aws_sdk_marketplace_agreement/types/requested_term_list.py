"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#RequestedTermList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.requested_term

RequestedTermList: TypeAlias = list[
    "aws_sdk_marketplace_agreement.types.requested_term.RequestedTerm"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RequestedTermList) -> list:
    import aws_sdk_marketplace_agreement.types.requested_term

    out: list = []
    for item in value:
        out.append(
            aws_sdk_marketplace_agreement.types.requested_term.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RequestedTermList:
    import aws_sdk_marketplace_agreement.types.requested_term

    out: RequestedTermList = []
    for item in data:
        out.append(
            aws_sdk_marketplace_agreement.types.requested_term.deserialize_aws_json_1_0(
                item
            )
        )
    return out

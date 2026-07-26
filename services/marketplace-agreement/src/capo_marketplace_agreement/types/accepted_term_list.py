"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AcceptedTermList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.accepted_term

AcceptedTermList: TypeAlias = list[
    "capo_marketplace_agreement.types.accepted_term.AcceptedTerm"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AcceptedTermList) -> list:
    import capo_marketplace_agreement.types.accepted_term

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.accepted_term.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AcceptedTermList:
    import capo_marketplace_agreement.types.accepted_term

    out: AcceptedTermList = []
    for item in data:
        out.append(
            capo_marketplace_agreement.types.accepted_term.deserialize_aws_json_1_0(
                item
            )
        )
    return out

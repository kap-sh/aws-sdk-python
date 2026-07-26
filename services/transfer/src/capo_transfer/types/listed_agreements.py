"""Generated from Smithy shape ``com.amazonaws.transfer#ListedAgreements``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transfer.types.listed_agreement

ListedAgreements: TypeAlias = list[
    "capo_transfer.types.listed_agreement.ListedAgreement"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListedAgreements) -> list:
    import capo_transfer.types.listed_agreement

    out: list = []
    for item in value:
        out.append(capo_transfer.types.listed_agreement.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ListedAgreements:
    import capo_transfer.types.listed_agreement

    out: ListedAgreements = []
    for item in data:
        out.append(capo_transfer.types.listed_agreement.deserialize_aws_json_1_1(item))
    return out

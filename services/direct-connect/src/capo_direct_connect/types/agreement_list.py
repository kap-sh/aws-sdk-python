"""Generated from Smithy shape ``com.amazonaws.directconnect#AgreementList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_direct_connect.types.customer_agreement

AgreementList: TypeAlias = list[
    "capo_direct_connect.types.customer_agreement.CustomerAgreement"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AgreementList) -> list:
    import capo_direct_connect.types.customer_agreement

    out: list = []
    for item in value:
        out.append(
            capo_direct_connect.types.customer_agreement.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AgreementList:
    import capo_direct_connect.types.customer_agreement

    out: AgreementList = []
    for item in data:
        out.append(
            capo_direct_connect.types.customer_agreement.deserialize_aws_json_1_1(item)
        )
    return out

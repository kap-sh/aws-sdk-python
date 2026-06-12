"""Generated from Smithy shape ``com.amazonaws.artifact#CustomerAgreementList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_artifact.types.customer_agreement_summary

CustomerAgreementList: TypeAlias = list[
    "aws_sdk_artifact.types.customer_agreement_summary.CustomerAgreementSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomerAgreementList) -> list:
    import aws_sdk_artifact.types.customer_agreement_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_artifact.types.customer_agreement_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CustomerAgreementList:
    import aws_sdk_artifact.types.customer_agreement_summary

    out: CustomerAgreementList = []
    for item in data:
        out.append(
            aws_sdk_artifact.types.customer_agreement_summary.deserialize_json(item)
        )
    return out

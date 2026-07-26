"""Generated from Smithy shape ``com.amazonaws.acm#DomainValidationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_acm.types.domain_validation

DomainValidationList: TypeAlias = list[
    "capo_acm.types.domain_validation.DomainValidation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DomainValidationList) -> list:
    import capo_acm.types.domain_validation

    out: list = []
    for item in value:
        out.append(capo_acm.types.domain_validation.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DomainValidationList:
    import capo_acm.types.domain_validation

    out: DomainValidationList = []
    for item in data:
        out.append(capo_acm.types.domain_validation.deserialize_aws_json_1_1(item))
    return out

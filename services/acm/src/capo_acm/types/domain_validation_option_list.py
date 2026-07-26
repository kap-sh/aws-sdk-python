"""Generated from Smithy shape ``com.amazonaws.acm#DomainValidationOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_acm.types.domain_validation_option

DomainValidationOptionList: TypeAlias = list[
    "capo_acm.types.domain_validation_option.DomainValidationOption"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DomainValidationOptionList) -> list:
    import capo_acm.types.domain_validation_option

    out: list = []
    for item in value:
        out.append(capo_acm.types.domain_validation_option.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DomainValidationOptionList:
    import capo_acm.types.domain_validation_option

    out: DomainValidationOptionList = []
    for item in data:
        out.append(
            capo_acm.types.domain_validation_option.deserialize_aws_json_1_1(item)
        )
    return out

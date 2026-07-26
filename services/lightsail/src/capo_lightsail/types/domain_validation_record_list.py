"""Generated from Smithy shape ``com.amazonaws.lightsail#DomainValidationRecordList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.domain_validation_record

DomainValidationRecordList: TypeAlias = list[
    "capo_lightsail.types.domain_validation_record.DomainValidationRecord"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DomainValidationRecordList) -> list:
    import capo_lightsail.types.domain_validation_record

    out: list = []
    for item in value:
        out.append(
            capo_lightsail.types.domain_validation_record.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DomainValidationRecordList:
    import capo_lightsail.types.domain_validation_record

    out: DomainValidationRecordList = []
    for item in data:
        out.append(
            capo_lightsail.types.domain_validation_record.deserialize_aws_json_1_1(item)
        )
    return out

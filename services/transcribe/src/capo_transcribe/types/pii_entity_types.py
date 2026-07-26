"""Generated from Smithy shape ``com.amazonaws.transcribe#PiiEntityTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transcribe.types.pii_entity_type

PiiEntityTypes: TypeAlias = list["capo_transcribe.types.pii_entity_type.PiiEntityType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PiiEntityTypes) -> list:
    import capo_transcribe.types.pii_entity_type

    out: list = []
    for item in value:
        out.append(capo_transcribe.types.pii_entity_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PiiEntityTypes:
    import capo_transcribe.types.pii_entity_type

    out: PiiEntityTypes = []
    for item in data:
        out.append(capo_transcribe.types.pii_entity_type.deserialize_aws_json_1_1(item))
    return out

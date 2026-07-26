"""Generated from Smithy shape ``com.amazonaws.b2bi#KeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_b2bi.types.sample_document_keys

KeyList: TypeAlias = list["capo_b2bi.types.sample_document_keys.SampleDocumentKeys"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KeyList) -> list:
    import capo_b2bi.types.sample_document_keys

    out: list = []
    for item in value:
        out.append(capo_b2bi.types.sample_document_keys.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> KeyList:
    import capo_b2bi.types.sample_document_keys

    out: KeyList = []
    for item in data:
        out.append(capo_b2bi.types.sample_document_keys.deserialize_aws_json_1_0(item))
    return out

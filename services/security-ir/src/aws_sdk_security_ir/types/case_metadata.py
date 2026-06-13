"""Generated from Smithy shape ``com.amazonaws.securityir#CaseMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_security_ir.types.case_metadata_entry

CaseMetadata: TypeAlias = list[
    "aws_sdk_security_ir.types.case_metadata_entry.CaseMetadataEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: CaseMetadata) -> list:
    import aws_sdk_security_ir.types.case_metadata_entry

    out: list = []
    for item in value:
        out.append(aws_sdk_security_ir.types.case_metadata_entry.serialize_json(item))
    return out


def deserialize_json(data: list) -> CaseMetadata:
    import aws_sdk_security_ir.types.case_metadata_entry

    out: CaseMetadata = []
    for item in data:
        out.append(aws_sdk_security_ir.types.case_metadata_entry.deserialize_json(item))
    return out

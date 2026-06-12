"""Generated from Smithy shape ``com.amazonaws.workdocs#AdditionalResponseFieldsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.additional_response_field_type

AdditionalResponseFieldsList: TypeAlias = list[
    "aws_sdk_workdocs.types.additional_response_field_type.AdditionalResponseFieldType"
]


# --- restJson1 ser/de ---
def serialize_json(value: AdditionalResponseFieldsList) -> list:
    import aws_sdk_workdocs.types.additional_response_field_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workdocs.types.additional_response_field_type.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AdditionalResponseFieldsList:
    import aws_sdk_workdocs.types.additional_response_field_type

    out: AdditionalResponseFieldsList = []
    for item in data:
        out.append(
            aws_sdk_workdocs.types.additional_response_field_type.deserialize_json(item)
        )
    return out

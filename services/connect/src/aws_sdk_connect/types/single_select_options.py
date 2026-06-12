"""Generated from Smithy shape ``com.amazonaws.connect#SingleSelectOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.task_template_single_select_option

SingleSelectOptions: TypeAlias = list[
    "aws_sdk_connect.types.task_template_single_select_option.TaskTemplateSingleSelectOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: SingleSelectOptions) -> list:
    return list(value)


def deserialize_json(data: list) -> SingleSelectOptions:
    return list(data)

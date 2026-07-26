"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#ValidationExceptionFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces_instances.types.validation_exception_field

ValidationExceptionFieldList: TypeAlias = list[
    "capo_workspaces_instances.types.validation_exception_field.ValidationExceptionField"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationExceptionFieldList) -> list:
    import capo_workspaces_instances.types.validation_exception_field

    out: list = []
    for item in value:
        out.append(
            capo_workspaces_instances.types.validation_exception_field.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ValidationExceptionFieldList:
    import capo_workspaces_instances.types.validation_exception_field

    out: ValidationExceptionFieldList = []
    for item in data:
        out.append(
            capo_workspaces_instances.types.validation_exception_field.deserialize_aws_json_1_0(
                item
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#QuickSetupTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_quicksetup.types.quick_setup_type_output

QuickSetupTypeList: TypeAlias = list[
    "aws_sdk_ssm_quicksetup.types.quick_setup_type_output.QuickSetupTypeOutput"
]


# --- restJson1 ser/de ---
def serialize_json(value: QuickSetupTypeList) -> list:
    import aws_sdk_ssm_quicksetup.types.quick_setup_type_output

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm_quicksetup.types.quick_setup_type_output.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> QuickSetupTypeList:
    import aws_sdk_ssm_quicksetup.types.quick_setup_type_output

    out: QuickSetupTypeList = []
    for item in data:
        out.append(
            aws_sdk_ssm_quicksetup.types.quick_setup_type_output.deserialize_json(item)
        )
    return out

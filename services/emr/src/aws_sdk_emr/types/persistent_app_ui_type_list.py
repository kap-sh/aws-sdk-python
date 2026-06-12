"""Generated from Smithy shape ``com.amazonaws.emr#PersistentAppUITypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr.types.persistent_app_ui_type

PersistentAppUITypeList: TypeAlias = list[
    "aws_sdk_emr.types.persistent_app_ui_type.PersistentAppUIType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PersistentAppUITypeList) -> list:
    import aws_sdk_emr.types.persistent_app_ui_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_emr.types.persistent_app_ui_type.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PersistentAppUITypeList:
    import aws_sdk_emr.types.persistent_app_ui_type

    out: PersistentAppUITypeList = []
    for item in data:
        out.append(
            aws_sdk_emr.types.persistent_app_ui_type.deserialize_aws_json_1_1(item)
        )
    return out

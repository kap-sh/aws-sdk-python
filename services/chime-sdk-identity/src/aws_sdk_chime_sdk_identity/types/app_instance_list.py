"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#AppInstanceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.app_instance_summary

AppInstanceList: TypeAlias = list[
    "aws_sdk_chime_sdk_identity.types.app_instance_summary.AppInstanceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AppInstanceList) -> list:
    import aws_sdk_chime_sdk_identity.types.app_instance_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_chime_sdk_identity.types.app_instance_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AppInstanceList:
    import aws_sdk_chime_sdk_identity.types.app_instance_summary

    out: AppInstanceList = []
    for item in data:
        out.append(
            aws_sdk_chime_sdk_identity.types.app_instance_summary.deserialize_json(item)
        )
    return out

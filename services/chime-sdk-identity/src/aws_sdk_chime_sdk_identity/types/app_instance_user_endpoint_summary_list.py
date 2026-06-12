"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#AppInstanceUserEndpointSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.app_instance_user_endpoint_summary

AppInstanceUserEndpointSummaryList: TypeAlias = list[
    "aws_sdk_chime_sdk_identity.types.app_instance_user_endpoint_summary.AppInstanceUserEndpointSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AppInstanceUserEndpointSummaryList) -> list:
    import aws_sdk_chime_sdk_identity.types.app_instance_user_endpoint_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_chime_sdk_identity.types.app_instance_user_endpoint_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AppInstanceUserEndpointSummaryList:
    import aws_sdk_chime_sdk_identity.types.app_instance_user_endpoint_summary

    out: AppInstanceUserEndpointSummaryList = []
    for item in data:
        out.append(
            aws_sdk_chime_sdk_identity.types.app_instance_user_endpoint_summary.deserialize_json(
                item
            )
        )
    return out

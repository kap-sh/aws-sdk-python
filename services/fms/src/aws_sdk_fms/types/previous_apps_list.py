"""Generated from Smithy shape ``com.amazonaws.fms#PreviousAppsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fms.types.apps_list
    import aws_sdk_fms.types.previous_list_version

PreviousAppsList: TypeAlias = dict[
    "aws_sdk_fms.types.previous_list_version.PreviousListVersion",
    "aws_sdk_fms.types.apps_list.AppsList",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: PreviousAppsList) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_fms.types.apps_list

        out[key] = aws_sdk_fms.types.apps_list.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> PreviousAppsList:
    out: PreviousAppsList = {}
    for key, value in data.items():
        import aws_sdk_fms.types.apps_list

        out[key] = aws_sdk_fms.types.apps_list.deserialize_aws_json_1_1(value)
    return out

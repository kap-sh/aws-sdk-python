"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AdditionalInfoMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.additional_info_value_list
    import aws_sdk_resiliencehub.types.string128_without_whitespace

AdditionalInfoMap: TypeAlias = dict[
    "aws_sdk_resiliencehub.types.string128_without_whitespace.String128WithoutWhitespace",
    "aws_sdk_resiliencehub.types.additional_info_value_list.AdditionalInfoValueList",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AdditionalInfoMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_resiliencehub.types.additional_info_value_list

        out[key] = (
            aws_sdk_resiliencehub.types.additional_info_value_list.serialize_json(value)
        )
    return out


def deserialize_json(data: dict) -> AdditionalInfoMap:
    out: AdditionalInfoMap = {}
    for key, value in data.items():
        import aws_sdk_resiliencehub.types.additional_info_value_list

        out[key] = (
            aws_sdk_resiliencehub.types.additional_info_value_list.deserialize_json(
                value
            )
        )
    return out

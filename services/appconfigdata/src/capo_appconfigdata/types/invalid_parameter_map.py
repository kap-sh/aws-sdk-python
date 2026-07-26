"""Generated from Smithy shape ``com.amazonaws.appconfigdata#InvalidParameterMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appconfigdata.types.invalid_parameter_detail
    import capo_appconfigdata.types.string

InvalidParameterMap: TypeAlias = dict[
    "capo_appconfigdata.types.string.String",
    "capo_appconfigdata.types.invalid_parameter_detail.InvalidParameterDetail",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: InvalidParameterMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_appconfigdata.types.invalid_parameter_detail

        out[key] = capo_appconfigdata.types.invalid_parameter_detail.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> InvalidParameterMap:
    out: InvalidParameterMap = {}
    for key, value in data.items():
        import capo_appconfigdata.types.invalid_parameter_detail

        out[key] = capo_appconfigdata.types.invalid_parameter_detail.deserialize_json(
            value
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.databrew#PathParametersMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_databrew.types.dataset_parameter
    import aws_sdk_databrew.types.path_parameter_name

PathParametersMap: TypeAlias = dict[
    "aws_sdk_databrew.types.path_parameter_name.PathParameterName",
    "aws_sdk_databrew.types.dataset_parameter.DatasetParameter",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: PathParametersMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_databrew.types.dataset_parameter

        out[key] = aws_sdk_databrew.types.dataset_parameter.serialize_json(value)
    return out


def deserialize_json(data: dict) -> PathParametersMap:
    out: PathParametersMap = {}
    for key, value in data.items():
        import aws_sdk_databrew.types.dataset_parameter

        out[key] = aws_sdk_databrew.types.dataset_parameter.deserialize_json(value)
    return out

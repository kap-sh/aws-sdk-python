"""Generated from Smithy shape ``com.amazonaws.gamelift#LocationalDeployments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.locational_deployment
    import aws_sdk_gamelift.types.non_zero_and128_max_ascii_string

LocationalDeployments: TypeAlias = dict[
    "aws_sdk_gamelift.types.non_zero_and128_max_ascii_string.NonZeroAnd128MaxAsciiString",
    "aws_sdk_gamelift.types.locational_deployment.LocationalDeployment",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: LocationalDeployments) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_gamelift.types.locational_deployment

        out[key] = aws_sdk_gamelift.types.locational_deployment.serialize_aws_json_1_1(
            value
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LocationalDeployments:
    out: LocationalDeployments = {}
    for key, value in data.items():
        import aws_sdk_gamelift.types.locational_deployment

        out[key] = (
            aws_sdk_gamelift.types.locational_deployment.deserialize_aws_json_1_1(value)
        )
    return out

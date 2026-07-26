"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#S3AccessPointConfigurationsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_accessanalyzer.types.access_point_arn
    import capo_accessanalyzer.types.s3_access_point_configuration

S3AccessPointConfigurationsMap: TypeAlias = dict[
    "capo_accessanalyzer.types.access_point_arn.AccessPointArn",
    "capo_accessanalyzer.types.s3_access_point_configuration.S3AccessPointConfiguration",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: S3AccessPointConfigurationsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_accessanalyzer.types.s3_access_point_configuration

        out[key] = (
            capo_accessanalyzer.types.s3_access_point_configuration.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> S3AccessPointConfigurationsMap:
    out: S3AccessPointConfigurationsMap = {}
    for key, value in data.items():
        import capo_accessanalyzer.types.s3_access_point_configuration

        out[key] = (
            capo_accessanalyzer.types.s3_access_point_configuration.deserialize_json(
                value
            )
        )
    return out

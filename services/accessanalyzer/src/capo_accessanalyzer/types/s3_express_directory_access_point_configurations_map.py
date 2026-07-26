"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#S3ExpressDirectoryAccessPointConfigurationsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_accessanalyzer.types.s3_express_directory_access_point_arn
    import capo_accessanalyzer.types.s3_express_directory_access_point_configuration

S3ExpressDirectoryAccessPointConfigurationsMap: TypeAlias = dict[
    "capo_accessanalyzer.types.s3_express_directory_access_point_arn.S3ExpressDirectoryAccessPointArn",
    "capo_accessanalyzer.types.s3_express_directory_access_point_configuration.S3ExpressDirectoryAccessPointConfiguration",
]


# --- restJson1 ser/de ---
def serialize_json(
    input_to_serialize: S3ExpressDirectoryAccessPointConfigurationsMap,
) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_accessanalyzer.types.s3_express_directory_access_point_configuration

        out[key] = (
            capo_accessanalyzer.types.s3_express_directory_access_point_configuration.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> S3ExpressDirectoryAccessPointConfigurationsMap:
    out: S3ExpressDirectoryAccessPointConfigurationsMap = {}
    for key, value in data.items():
        import capo_accessanalyzer.types.s3_express_directory_access_point_configuration

        out[key] = (
            capo_accessanalyzer.types.s3_express_directory_access_point_configuration.deserialize_json(
                value
            )
        )
    return out

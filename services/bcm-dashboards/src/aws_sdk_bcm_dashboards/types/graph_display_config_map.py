"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#GraphDisplayConfigMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bcm_dashboards.types.generic_string
    import aws_sdk_bcm_dashboards.types.graph_display_config

GraphDisplayConfigMap: TypeAlias = dict[
    "aws_sdk_bcm_dashboards.types.generic_string.GenericString",
    "aws_sdk_bcm_dashboards.types.graph_display_config.GraphDisplayConfig",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: GraphDisplayConfigMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_bcm_dashboards.types.graph_display_config

        out[key] = (
            aws_sdk_bcm_dashboards.types.graph_display_config.serialize_aws_json_1_0(
                value
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GraphDisplayConfigMap:
    out: GraphDisplayConfigMap = {}
    for key, value in data.items():
        import aws_sdk_bcm_dashboards.types.graph_display_config

        out[key] = (
            aws_sdk_bcm_dashboards.types.graph_display_config.deserialize_aws_json_1_0(
                value
            )
        )
    return out

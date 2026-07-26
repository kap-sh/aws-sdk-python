"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#GraphDisplayConfigMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bcm_dashboards.types.generic_string
    import capo_bcm_dashboards.types.graph_display_config

GraphDisplayConfigMap: TypeAlias = dict[
    "capo_bcm_dashboards.types.generic_string.GenericString",
    "capo_bcm_dashboards.types.graph_display_config.GraphDisplayConfig",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: GraphDisplayConfigMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_bcm_dashboards.types.graph_display_config

        out[key] = (
            capo_bcm_dashboards.types.graph_display_config.serialize_aws_json_1_0(value)
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GraphDisplayConfigMap:
    out: GraphDisplayConfigMap = {}
    for key, value in data.items():
        import capo_bcm_dashboards.types.graph_display_config

        out[key] = (
            capo_bcm_dashboards.types.graph_display_config.deserialize_aws_json_1_0(
                value
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#DisplayConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bcm_dashboards.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_dashboards.types.graph_display_config_map
    import aws_sdk_bcm_dashboards.types.table_display_config_struct


class _DisplayConfig_graph(TypedDict, closed=True):
    graph: "aws_sdk_bcm_dashboards.types.graph_display_config_map.GraphDisplayConfigMap"


class _DisplayConfig_table(TypedDict, closed=True):
    table: "aws_sdk_bcm_dashboards.types.table_display_config_struct.TableDisplayConfigStruct"


DisplayConfig: TypeAlias = _DisplayConfig_graph | _DisplayConfig_table


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DisplayConfig) -> dict:
    if "graph" in value:
        import aws_sdk_bcm_dashboards.types.graph_display_config_map

        return {
            "graph": aws_sdk_bcm_dashboards.types.graph_display_config_map.serialize_aws_json_1_0(
                value["graph"]
            )
        }
    elif "table" in value:
        import aws_sdk_bcm_dashboards.types.table_display_config_struct

        return {
            "table": aws_sdk_bcm_dashboards.types.table_display_config_struct.serialize_aws_json_1_0(
                value["table"]
            )
        }
    else:
        raise SerializationError("DisplayConfig: no variant present")


def deserialize_aws_json_1_0(data: dict) -> DisplayConfig:
    if "graph" in data:
        import aws_sdk_bcm_dashboards.types.graph_display_config_map

        return {
            "graph": aws_sdk_bcm_dashboards.types.graph_display_config_map.deserialize_aws_json_1_0(
                data["graph"]
            )
        }
    elif "table" in data:
        import aws_sdk_bcm_dashboards.types.table_display_config_struct

        return {
            "table": aws_sdk_bcm_dashboards.types.table_display_config_struct.deserialize_aws_json_1_0(
                data["table"]
            )
        }
    else:
        raise DeserializationError("DisplayConfig: no recognized variant key")

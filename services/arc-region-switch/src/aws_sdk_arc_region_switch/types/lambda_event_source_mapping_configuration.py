"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#LambdaEventSourceMappingConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_arc_region_switch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.event_source_mapping_action
    import aws_sdk_arc_region_switch.types.lambda_event_source_mapping_ungraceful
    import aws_sdk_arc_region_switch.types.region_event_source_mapping_map


class LambdaEventSourceMappingConfiguration(TypedDict):
    timeout_minutes: "int"
    """<p>The timeout value specified for the configuration.</p>"""
    action: "aws_sdk_arc_region_switch.types.event_source_mapping_action.EventSourceMappingAction"
    """<p>The action to take - whether to <code>enable</code> or <code>disable</code> an event source mapping.</p>"""
    region_event_source_mappings: "aws_sdk_arc_region_switch.types.region_event_source_mapping_map.RegionEventSourceMappingMap"
    """<p>Per-region configuration for which Lambda event source mapping to enable or disable when activating or deactivating a region.</p>"""
    ungraceful: NotRequired[
        "aws_sdk_arc_region_switch.types.lambda_event_source_mapping_ungraceful.LambdaEventSourceMappingUngraceful"
    ]
    """<p>The settings for ungraceful execution.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LambdaEventSourceMappingConfiguration) -> dict:
    out: dict = {}
    out["timeoutMinutes"] = value.get("timeout_minutes", 60)
    import aws_sdk_arc_region_switch.types.event_source_mapping_action

    out["action"] = (
        aws_sdk_arc_region_switch.types.event_source_mapping_action.serialize_aws_json_1_0(
            value["action"]
        )
    )
    import aws_sdk_arc_region_switch.types.region_event_source_mapping_map

    out["regionEventSourceMappings"] = (
        aws_sdk_arc_region_switch.types.region_event_source_mapping_map.serialize_aws_json_1_0(
            value["region_event_source_mappings"]
        )
    )
    if "ungraceful" in value:
        import aws_sdk_arc_region_switch.types.lambda_event_source_mapping_ungraceful

        out["ungraceful"] = (
            aws_sdk_arc_region_switch.types.lambda_event_source_mapping_ungraceful.serialize_aws_json_1_0(
                value["ungraceful"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> LambdaEventSourceMappingConfiguration:
    out: LambdaEventSourceMappingConfiguration = {}  # type: ignore[typeddict-item]
    if "timeoutMinutes" in data:
        out["timeout_minutes"] = data["timeoutMinutes"]
    else:
        out["timeout_minutes"] = 60
    if "action" in data:
        import aws_sdk_arc_region_switch.types.event_source_mapping_action

        out["action"] = (
            aws_sdk_arc_region_switch.types.event_source_mapping_action.deserialize_aws_json_1_0(
                data["action"]
            )
        )
    else:
        raise DeserializationError(
            "LambdaEventSourceMappingConfiguration.action required"
        )
    if "regionEventSourceMappings" in data:
        import aws_sdk_arc_region_switch.types.region_event_source_mapping_map

        out["region_event_source_mappings"] = (
            aws_sdk_arc_region_switch.types.region_event_source_mapping_map.deserialize_aws_json_1_0(
                data["regionEventSourceMappings"]
            )
        )
    else:
        raise DeserializationError(
            "LambdaEventSourceMappingConfiguration.region_event_source_mappings required"
        )
    if "ungraceful" in data:
        import aws_sdk_arc_region_switch.types.lambda_event_source_mapping_ungraceful

        out["ungraceful"] = (
            aws_sdk_arc_region_switch.types.lambda_event_source_mapping_ungraceful.deserialize_aws_json_1_0(
                data["ungraceful"]
            )
        )
    return out

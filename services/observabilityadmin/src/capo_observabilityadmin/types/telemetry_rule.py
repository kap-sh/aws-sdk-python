"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TelemetryRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_observabilityadmin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_observabilityadmin.types.all_regions
    import capo_observabilityadmin.types.regions
    import capo_observabilityadmin.types.resource_type
    import capo_observabilityadmin.types.telemetry_destination_configuration
    import capo_observabilityadmin.types.telemetry_source_types
    import capo_observabilityadmin.types.telemetry_type


class TelemetryRule(TypedDict, closed=True):
    resource_type: NotRequired[
        "capo_observabilityadmin.types.resource_type.ResourceType"
    ]
    r"""<p> The type of Amazon Web Services resource to configure telemetry for (e.g., \"AWS::EC2::VPC\", \"AWS::EKS::Cluster\", \"AWS::WAFv2::WebACL\"). </p>"""
    telemetry_type: "capo_observabilityadmin.types.telemetry_type.TelemetryType"
    """<p> The type of telemetry to collect (Logs, Metrics, or Traces). </p>"""
    telemetry_source_types: NotRequired[
        "capo_observabilityadmin.types.telemetry_source_types.TelemetrySourceTypes"
    ]
    """<p> The specific telemetry source types to configure for the resource, such as VPC_FLOW_LOGS or EKS_AUDIT_LOGS. TelemetrySourceTypes must be correlated with the specific resource type. </p>"""
    destination_configuration: NotRequired[
        "capo_observabilityadmin.types.telemetry_destination_configuration.TelemetryDestinationConfiguration"
    ]
    """<p> Configuration specifying where and how the telemetry data should be delivered. </p>"""
    scope: NotRequired["str"]
    """<p> The organizational scope to which the rule applies, specified using accounts or organizational units. </p>"""
    selection_criteria: NotRequired["str"]
    """<p> Criteria for selecting which resources the rule applies to, such as resource tags. </p>"""
    allow_field_updates: NotRequired["bool"]
    """<p> If set to <code>true</code>, Amazon CloudWatch Observability Admin detects and remediates configuration drift in telemetry resources that it manages. For example, if a VPC flow log's format, traffic type, or aggregation interval no longer matches the rule's destination configuration, the flow log is replaced with one that matches. Only Observability Admin-managed resources are updated; customer-created resources are never modified. Currently supported for <code>AWS::EC2::VPC</code> resources (VPC flow logs). </p>"""
    regions: NotRequired["capo_observabilityadmin.types.regions.Regions"]
    """<p> An optional list of Amazon Web Services Regions where this telemetry rule should be replicated. When specified, the rule is created in the home region and automatically replicated to all listed regions. Mutually exclusive with <code>AllRegions</code>. </p>"""
    all_regions: NotRequired["capo_observabilityadmin.types.all_regions.AllRegions"]
    """<p> If set to <code>true</code>, the telemetry rule is replicated to all Amazon Web Services Regions where Amazon CloudWatch Observability Admin is available in the current partition. When new regions become available, the rule automatically replicates to them. Mutually exclusive with <code>Regions</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TelemetryRule) -> dict:
    out: dict = {}
    if "resource_type" in value:
        import capo_observabilityadmin.types.resource_type

        out["ResourceType"] = (
            capo_observabilityadmin.types.resource_type.serialize_json(
                value["resource_type"]
            )
        )
    import capo_observabilityadmin.types.telemetry_type

    out["TelemetryType"] = capo_observabilityadmin.types.telemetry_type.serialize_json(
        value["telemetry_type"]
    )
    if "telemetry_source_types" in value:
        import capo_observabilityadmin.types.telemetry_source_types

        out["TelemetrySourceTypes"] = (
            capo_observabilityadmin.types.telemetry_source_types.serialize_json(
                value["telemetry_source_types"]
            )
        )
    if "destination_configuration" in value:
        import capo_observabilityadmin.types.telemetry_destination_configuration

        out["DestinationConfiguration"] = (
            capo_observabilityadmin.types.telemetry_destination_configuration.serialize_json(
                value["destination_configuration"]
            )
        )
    if "scope" in value:
        out["Scope"] = value["scope"]
    if "selection_criteria" in value:
        out["SelectionCriteria"] = value["selection_criteria"]
    if "allow_field_updates" in value:
        out["AllowFieldUpdates"] = value["allow_field_updates"]
    if "regions" in value:
        import capo_observabilityadmin.types.regions

        out["Regions"] = capo_observabilityadmin.types.regions.serialize_json(
            value["regions"]
        )
    if "all_regions" in value:
        out["AllRegions"] = value["all_regions"]
    return out


def deserialize_json(data: dict) -> TelemetryRule:
    out: TelemetryRule = {}  # type: ignore[typeddict-item]
    if "ResourceType" in data:
        import capo_observabilityadmin.types.resource_type

        out["resource_type"] = (
            capo_observabilityadmin.types.resource_type.deserialize_json(
                data["ResourceType"]
            )
        )
    if "TelemetryType" in data:
        import capo_observabilityadmin.types.telemetry_type

        out["telemetry_type"] = (
            capo_observabilityadmin.types.telemetry_type.deserialize_json(
                data["TelemetryType"]
            )
        )
    else:
        raise DeserializationError("TelemetryRule.telemetry_type required")
    if "TelemetrySourceTypes" in data:
        import capo_observabilityadmin.types.telemetry_source_types

        out["telemetry_source_types"] = (
            capo_observabilityadmin.types.telemetry_source_types.deserialize_json(
                data["TelemetrySourceTypes"]
            )
        )
    if "DestinationConfiguration" in data:
        import capo_observabilityadmin.types.telemetry_destination_configuration

        out["destination_configuration"] = (
            capo_observabilityadmin.types.telemetry_destination_configuration.deserialize_json(
                data["DestinationConfiguration"]
            )
        )
    if "Scope" in data:
        out["scope"] = data["Scope"]
    if "SelectionCriteria" in data:
        out["selection_criteria"] = data["SelectionCriteria"]
    if "AllowFieldUpdates" in data:
        out["allow_field_updates"] = data["AllowFieldUpdates"]
    if "Regions" in data:
        import capo_observabilityadmin.types.regions

        out["regions"] = capo_observabilityadmin.types.regions.deserialize_json(
            data["Regions"]
        )
    if "AllRegions" in data:
        out["all_regions"] = data["AllRegions"]
    return out

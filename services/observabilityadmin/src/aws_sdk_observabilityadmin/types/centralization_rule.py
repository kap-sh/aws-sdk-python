"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#CentralizationRule``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_observabilityadmin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.centralization_rule_destination
    import aws_sdk_observabilityadmin.types.centralization_rule_source


class CentralizationRule(TypedDict):
    source: "aws_sdk_observabilityadmin.types.centralization_rule_source.CentralizationRuleSource"
    """<p>Configuration determining the source of the telemetry data to be centralized.</p>"""
    destination: "aws_sdk_observabilityadmin.types.centralization_rule_destination.CentralizationRuleDestination"
    """<p>Configuration determining where the telemetry data should be centralized, backed up, as well as encryption configuration for the primary and backup destinations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CentralizationRule) -> dict:
    out: dict = {}
    import aws_sdk_observabilityadmin.types.centralization_rule_source

    out["Source"] = (
        aws_sdk_observabilityadmin.types.centralization_rule_source.serialize_json(
            value["source"]
        )
    )
    import aws_sdk_observabilityadmin.types.centralization_rule_destination

    out["Destination"] = (
        aws_sdk_observabilityadmin.types.centralization_rule_destination.serialize_json(
            value["destination"]
        )
    )
    return out


def deserialize_json(data: dict) -> CentralizationRule:
    out: CentralizationRule = {}  # type: ignore[typeddict-item]
    if "Source" in data:
        import aws_sdk_observabilityadmin.types.centralization_rule_source

        out["source"] = (
            aws_sdk_observabilityadmin.types.centralization_rule_source.deserialize_json(
                data["Source"]
            )
        )
    else:
        raise DeserializationError("CentralizationRule.source required")
    if "Destination" in data:
        import aws_sdk_observabilityadmin.types.centralization_rule_destination

        out["destination"] = (
            aws_sdk_observabilityadmin.types.centralization_rule_destination.deserialize_json(
                data["Destination"]
            )
        )
    else:
        raise DeserializationError("CentralizationRule.destination required")
    return out

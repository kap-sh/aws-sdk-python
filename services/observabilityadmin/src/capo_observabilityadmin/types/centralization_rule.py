"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#CentralizationRule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_observabilityadmin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_observabilityadmin.types.centralization_rule_destination
    import capo_observabilityadmin.types.centralization_rule_source


class CentralizationRule(TypedDict, closed=True):
    source: "capo_observabilityadmin.types.centralization_rule_source.CentralizationRuleSource"
    """<p>Configuration determining the source of the telemetry data to be centralized.</p>"""
    destination: "capo_observabilityadmin.types.centralization_rule_destination.CentralizationRuleDestination"
    """<p>Configuration determining where the telemetry data should be centralized, backed up, as well as encryption configuration for the primary and backup destinations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CentralizationRule) -> dict:
    out: dict = {}
    import capo_observabilityadmin.types.centralization_rule_source

    out["Source"] = (
        capo_observabilityadmin.types.centralization_rule_source.serialize_json(
            value["source"]
        )
    )
    import capo_observabilityadmin.types.centralization_rule_destination

    out["Destination"] = (
        capo_observabilityadmin.types.centralization_rule_destination.serialize_json(
            value["destination"]
        )
    )
    return out


def deserialize_json(data: dict) -> CentralizationRule:
    out: CentralizationRule = {}  # type: ignore[typeddict-item]
    if "Source" in data:
        import capo_observabilityadmin.types.centralization_rule_source

        out["source"] = (
            capo_observabilityadmin.types.centralization_rule_source.deserialize_json(
                data["Source"]
            )
        )
    else:
        raise DeserializationError("CentralizationRule.source required")
    if "Destination" in data:
        import capo_observabilityadmin.types.centralization_rule_destination

        out["destination"] = (
            capo_observabilityadmin.types.centralization_rule_destination.deserialize_json(
                data["Destination"]
            )
        )
    else:
        raise DeserializationError("CentralizationRule.destination required")
    return out

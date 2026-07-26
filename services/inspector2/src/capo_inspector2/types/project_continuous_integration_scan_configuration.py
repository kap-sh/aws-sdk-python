"""Generated from Smithy shape ``com.amazonaws.inspector2#ProjectContinuousIntegrationScanConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.continuous_integration_scan_event
    import capo_inspector2.types.rule_set_categories


class ProjectContinuousIntegrationScanConfiguration(TypedDict, closed=True):
    supported_event: NotRequired[
        "capo_inspector2.types.continuous_integration_scan_event.ContinuousIntegrationScanEvent"
    ]
    """<p>The repository event that triggers continuous integration scans for the project.</p>"""
    rule_set_categories: NotRequired[
        "capo_inspector2.types.rule_set_categories.RuleSetCategories"
    ]
    """<p>The categories of security rules applied during continuous integration scans for the project.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProjectContinuousIntegrationScanConfiguration) -> dict:
    out: dict = {}
    if "supported_event" in value:
        import capo_inspector2.types.continuous_integration_scan_event

        out["supportedEvent"] = (
            capo_inspector2.types.continuous_integration_scan_event.serialize_json(
                value["supported_event"]
            )
        )
    if "rule_set_categories" in value:
        import capo_inspector2.types.rule_set_categories

        out["ruleSetCategories"] = (
            capo_inspector2.types.rule_set_categories.serialize_json(
                value["rule_set_categories"]
            )
        )
    return out


def deserialize_json(data: dict) -> ProjectContinuousIntegrationScanConfiguration:
    out: ProjectContinuousIntegrationScanConfiguration = {}  # type: ignore[typeddict-item]
    if "supportedEvent" in data:
        import capo_inspector2.types.continuous_integration_scan_event

        out["supported_event"] = (
            capo_inspector2.types.continuous_integration_scan_event.deserialize_json(
                data["supportedEvent"]
            )
        )
    if "ruleSetCategories" in data:
        import capo_inspector2.types.rule_set_categories

        out["rule_set_categories"] = (
            capo_inspector2.types.rule_set_categories.deserialize_json(
                data["ruleSetCategories"]
            )
        )
    return out

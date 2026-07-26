"""Generated from Smithy shape ``com.amazonaws.securityhub#AutomationRulesMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.automation_rules_metadata

AutomationRulesMetadataList: TypeAlias = list[
    "capo_securityhub.types.automation_rules_metadata.AutomationRulesMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomationRulesMetadataList) -> list:
    import capo_securityhub.types.automation_rules_metadata

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.automation_rules_metadata.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AutomationRulesMetadataList:
    import capo_securityhub.types.automation_rules_metadata

    out: AutomationRulesMetadataList = []
    for item in data:
        out.append(
            capo_securityhub.types.automation_rules_metadata.deserialize_json(item)
        )
    return out

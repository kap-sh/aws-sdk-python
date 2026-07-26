"""Generated from Smithy shape ``com.amazonaws.securityhub#AutomationRulesMetadataListV2``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.automation_rules_metadata_v2

AutomationRulesMetadataListV2: TypeAlias = list[
    "capo_securityhub.types.automation_rules_metadata_v2.AutomationRulesMetadataV2"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomationRulesMetadataListV2) -> list:
    import capo_securityhub.types.automation_rules_metadata_v2

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.automation_rules_metadata_v2.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AutomationRulesMetadataListV2:
    import capo_securityhub.types.automation_rules_metadata_v2

    out: AutomationRulesMetadataListV2 = []
    for item in data:
        out.append(
            capo_securityhub.types.automation_rules_metadata_v2.deserialize_json(item)
        )
    return out

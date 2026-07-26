"""Generated from Smithy shape ``com.amazonaws.auditmanager#ControlDomainInsightsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_auditmanager.types.control_domain_insights

ControlDomainInsightsList: TypeAlias = list[
    "capo_auditmanager.types.control_domain_insights.ControlDomainInsights"
]


# --- restJson1 ser/de ---
def serialize_json(value: ControlDomainInsightsList) -> list:
    import capo_auditmanager.types.control_domain_insights

    out: list = []
    for item in value:
        out.append(capo_auditmanager.types.control_domain_insights.serialize_json(item))
    return out


def deserialize_json(data: list) -> ControlDomainInsightsList:
    import capo_auditmanager.types.control_domain_insights

    out: ControlDomainInsightsList = []
    for item in data:
        out.append(
            capo_auditmanager.types.control_domain_insights.deserialize_json(item)
        )
    return out

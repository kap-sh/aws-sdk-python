"""Generated from Smithy shape ``com.amazonaws.grafana#ServiceAccountList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_grafana.types.service_account_summary

ServiceAccountList: TypeAlias = list[
    "capo_grafana.types.service_account_summary.ServiceAccountSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceAccountList) -> list:
    import capo_grafana.types.service_account_summary

    out: list = []
    for item in value:
        out.append(capo_grafana.types.service_account_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ServiceAccountList:
    import capo_grafana.types.service_account_summary

    out: ServiceAccountList = []
    for item in data:
        out.append(capo_grafana.types.service_account_summary.deserialize_json(item))
    return out

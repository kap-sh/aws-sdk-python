"""Generated from Smithy shape ``com.amazonaws.grafana#ServiceAccountTokenList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_grafana.types.service_account_token_summary

ServiceAccountTokenList: TypeAlias = list[
    "capo_grafana.types.service_account_token_summary.ServiceAccountTokenSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceAccountTokenList) -> list:
    import capo_grafana.types.service_account_token_summary

    out: list = []
    for item in value:
        out.append(
            capo_grafana.types.service_account_token_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ServiceAccountTokenList:
    import capo_grafana.types.service_account_token_summary

    out: ServiceAccountTokenList = []
    for item in data:
        out.append(
            capo_grafana.types.service_account_token_summary.deserialize_json(item)
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#ConnectorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pca_connector_scep.types.connector_summary

ConnectorList: TypeAlias = list[
    "capo_pca_connector_scep.types.connector_summary.ConnectorSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorList) -> list:
    import capo_pca_connector_scep.types.connector_summary

    out: list = []
    for item in value:
        out.append(capo_pca_connector_scep.types.connector_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ConnectorList:
    import capo_pca_connector_scep.types.connector_summary

    out: ConnectorList = []
    for item in data:
        out.append(
            capo_pca_connector_scep.types.connector_summary.deserialize_json(item)
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#TemplateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pca_connector_ad.types.template_summary

TemplateList: TypeAlias = list[
    "capo_pca_connector_ad.types.template_summary.TemplateSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: TemplateList) -> list:
    import capo_pca_connector_ad.types.template_summary

    out: list = []
    for item in value:
        out.append(capo_pca_connector_ad.types.template_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> TemplateList:
    import capo_pca_connector_ad.types.template_summary

    out: TemplateList = []
    for item in data:
        out.append(capo_pca_connector_ad.types.template_summary.deserialize_json(item))
    return out

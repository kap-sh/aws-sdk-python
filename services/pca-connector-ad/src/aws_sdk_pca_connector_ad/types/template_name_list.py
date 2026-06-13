"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#TemplateNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pca_connector_ad.types.template_name

TemplateNameList: TypeAlias = list[
    "aws_sdk_pca_connector_ad.types.template_name.TemplateName"
]


# --- restJson1 ser/de ---
def serialize_json(value: TemplateNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> TemplateNameList:
    return list(data)

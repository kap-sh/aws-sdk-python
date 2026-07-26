"""Generated from Smithy shape ``com.amazonaws.acmpca#CustomExtensionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_acm_pca.types.custom_extension

CustomExtensionList: TypeAlias = list[
    "capo_acm_pca.types.custom_extension.CustomExtension"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomExtensionList) -> list:
    import capo_acm_pca.types.custom_extension

    out: list = []
    for item in value:
        out.append(capo_acm_pca.types.custom_extension.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CustomExtensionList:
    import capo_acm_pca.types.custom_extension

    out: CustomExtensionList = []
    for item in data:
        out.append(capo_acm_pca.types.custom_extension.deserialize_aws_json_1_1(item))
    return out

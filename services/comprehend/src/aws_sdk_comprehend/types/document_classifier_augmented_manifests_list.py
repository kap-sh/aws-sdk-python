"""Generated from Smithy shape ``com.amazonaws.comprehend#DocumentClassifierAugmentedManifestsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.augmented_manifests_list_item

DocumentClassifierAugmentedManifestsList: TypeAlias = list[
    "aws_sdk_comprehend.types.augmented_manifests_list_item.AugmentedManifestsListItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentClassifierAugmentedManifestsList) -> list:
    import aws_sdk_comprehend.types.augmented_manifests_list_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_comprehend.types.augmented_manifests_list_item.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DocumentClassifierAugmentedManifestsList:
    import aws_sdk_comprehend.types.augmented_manifests_list_item

    out: DocumentClassifierAugmentedManifestsList = []
    for item in data:
        out.append(
            aws_sdk_comprehend.types.augmented_manifests_list_item.deserialize_aws_json_1_1(
                item
            )
        )
    return out

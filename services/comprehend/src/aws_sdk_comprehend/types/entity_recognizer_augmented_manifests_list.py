"""Generated from Smithy shape ``com.amazonaws.comprehend#EntityRecognizerAugmentedManifestsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.augmented_manifests_list_item

EntityRecognizerAugmentedManifestsList: TypeAlias = list[
    "aws_sdk_comprehend.types.augmented_manifests_list_item.AugmentedManifestsListItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityRecognizerAugmentedManifestsList) -> list:
    import aws_sdk_comprehend.types.augmented_manifests_list_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_comprehend.types.augmented_manifests_list_item.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EntityRecognizerAugmentedManifestsList:
    import aws_sdk_comprehend.types.augmented_manifests_list_item

    out: EntityRecognizerAugmentedManifestsList = []
    for item in data:
        out.append(
            aws_sdk_comprehend.types.augmented_manifests_list_item.deserialize_aws_json_1_1(
                item
            )
        )
    return out

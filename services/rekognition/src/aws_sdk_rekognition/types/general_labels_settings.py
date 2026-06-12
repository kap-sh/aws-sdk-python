"""Generated from Smithy shape ``com.amazonaws.rekognition#GeneralLabelsSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.general_labels_filter_list


class GeneralLabelsSettings(TypedDict):
    label_inclusion_filters: NotRequired[
        "aws_sdk_rekognition.types.general_labels_filter_list.GeneralLabelsFilterList"
    ]
    """<p>The labels that should be included in the return from DetectLabels.</p>"""
    label_exclusion_filters: NotRequired[
        "aws_sdk_rekognition.types.general_labels_filter_list.GeneralLabelsFilterList"
    ]
    """<p>The labels that should be excluded from the return from DetectLabels.</p>"""
    label_category_inclusion_filters: NotRequired[
        "aws_sdk_rekognition.types.general_labels_filter_list.GeneralLabelsFilterList"
    ]
    """<p>The label categories that should be included in the return from DetectLabels.</p>"""
    label_category_exclusion_filters: NotRequired[
        "aws_sdk_rekognition.types.general_labels_filter_list.GeneralLabelsFilterList"
    ]
    """<p>The label categories that should be excluded from the return from DetectLabels.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GeneralLabelsSettings) -> dict:
    out: dict = {}
    if "label_inclusion_filters" in value:
        import aws_sdk_rekognition.types.general_labels_filter_list

        out["LabelInclusionFilters"] = (
            aws_sdk_rekognition.types.general_labels_filter_list.serialize_aws_json_1_1(
                value["label_inclusion_filters"]
            )
        )
    if "label_exclusion_filters" in value:
        import aws_sdk_rekognition.types.general_labels_filter_list

        out["LabelExclusionFilters"] = (
            aws_sdk_rekognition.types.general_labels_filter_list.serialize_aws_json_1_1(
                value["label_exclusion_filters"]
            )
        )
    if "label_category_inclusion_filters" in value:
        import aws_sdk_rekognition.types.general_labels_filter_list

        out["LabelCategoryInclusionFilters"] = (
            aws_sdk_rekognition.types.general_labels_filter_list.serialize_aws_json_1_1(
                value["label_category_inclusion_filters"]
            )
        )
    if "label_category_exclusion_filters" in value:
        import aws_sdk_rekognition.types.general_labels_filter_list

        out["LabelCategoryExclusionFilters"] = (
            aws_sdk_rekognition.types.general_labels_filter_list.serialize_aws_json_1_1(
                value["label_category_exclusion_filters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GeneralLabelsSettings:
    out: GeneralLabelsSettings = {}  # type: ignore[typeddict-item]
    if "LabelInclusionFilters" in data:
        import aws_sdk_rekognition.types.general_labels_filter_list

        out["label_inclusion_filters"] = (
            aws_sdk_rekognition.types.general_labels_filter_list.deserialize_aws_json_1_1(
                data["LabelInclusionFilters"]
            )
        )
    if "LabelExclusionFilters" in data:
        import aws_sdk_rekognition.types.general_labels_filter_list

        out["label_exclusion_filters"] = (
            aws_sdk_rekognition.types.general_labels_filter_list.deserialize_aws_json_1_1(
                data["LabelExclusionFilters"]
            )
        )
    if "LabelCategoryInclusionFilters" in data:
        import aws_sdk_rekognition.types.general_labels_filter_list

        out["label_category_inclusion_filters"] = (
            aws_sdk_rekognition.types.general_labels_filter_list.deserialize_aws_json_1_1(
                data["LabelCategoryInclusionFilters"]
            )
        )
    if "LabelCategoryExclusionFilters" in data:
        import aws_sdk_rekognition.types.general_labels_filter_list

        out["label_category_exclusion_filters"] = (
            aws_sdk_rekognition.types.general_labels_filter_list.deserialize_aws_json_1_1(
                data["LabelCategoryExclusionFilters"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.quicksight#WordCloudOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.word_cloud_cloud_layout
    import aws_sdk_quicksight.types.word_cloud_maximum_string_length
    import aws_sdk_quicksight.types.word_cloud_word_casing
    import aws_sdk_quicksight.types.word_cloud_word_orientation
    import aws_sdk_quicksight.types.word_cloud_word_padding
    import aws_sdk_quicksight.types.word_cloud_word_scaling


class WordCloudOptions(TypedDict, closed=True):
    word_orientation: NotRequired[
        "aws_sdk_quicksight.types.word_cloud_word_orientation.WordCloudWordOrientation"
    ]
    """<p>The word orientation options (horizontal, horizontal_and_vertical) for the words in a word cloud.</p>"""
    word_scaling: NotRequired[
        "aws_sdk_quicksight.types.word_cloud_word_scaling.WordCloudWordScaling"
    ]
    """<p>The word scaling options (emphasize, normal) for the words in a word cloud.</p>"""
    cloud_layout: NotRequired[
        "aws_sdk_quicksight.types.word_cloud_cloud_layout.WordCloudCloudLayout"
    ]
    """<p>The cloud layout options (fluid, normal) of a word cloud.</p>"""
    word_casing: NotRequired[
        "aws_sdk_quicksight.types.word_cloud_word_casing.WordCloudWordCasing"
    ]
    """<p>The word casing options (lower_case, existing_case) for the words in a word cloud.</p>"""
    word_padding: NotRequired[
        "aws_sdk_quicksight.types.word_cloud_word_padding.WordCloudWordPadding"
    ]
    """<p>The word padding options (none, small, medium, large) for the words in a word cloud.</p>"""
    maximum_string_length: NotRequired[
        "aws_sdk_quicksight.types.word_cloud_maximum_string_length.WordCloudMaximumStringLength"
    ]
    """<p>The length limit of each word from 1-100.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WordCloudOptions) -> dict:
    out: dict = {}
    if "word_orientation" in value:
        import aws_sdk_quicksight.types.word_cloud_word_orientation

        out["WordOrientation"] = (
            aws_sdk_quicksight.types.word_cloud_word_orientation.serialize_json(
                value["word_orientation"]
            )
        )
    if "word_scaling" in value:
        import aws_sdk_quicksight.types.word_cloud_word_scaling

        out["WordScaling"] = (
            aws_sdk_quicksight.types.word_cloud_word_scaling.serialize_json(
                value["word_scaling"]
            )
        )
    if "cloud_layout" in value:
        import aws_sdk_quicksight.types.word_cloud_cloud_layout

        out["CloudLayout"] = (
            aws_sdk_quicksight.types.word_cloud_cloud_layout.serialize_json(
                value["cloud_layout"]
            )
        )
    if "word_casing" in value:
        import aws_sdk_quicksight.types.word_cloud_word_casing

        out["WordCasing"] = (
            aws_sdk_quicksight.types.word_cloud_word_casing.serialize_json(
                value["word_casing"]
            )
        )
    if "word_padding" in value:
        import aws_sdk_quicksight.types.word_cloud_word_padding

        out["WordPadding"] = (
            aws_sdk_quicksight.types.word_cloud_word_padding.serialize_json(
                value["word_padding"]
            )
        )
    if "maximum_string_length" in value:
        out["MaximumStringLength"] = value["maximum_string_length"]
    return out


def deserialize_json(data: dict) -> WordCloudOptions:
    out: WordCloudOptions = {}  # type: ignore[typeddict-item]
    if "WordOrientation" in data:
        import aws_sdk_quicksight.types.word_cloud_word_orientation

        out["word_orientation"] = (
            aws_sdk_quicksight.types.word_cloud_word_orientation.deserialize_json(
                data["WordOrientation"]
            )
        )
    if "WordScaling" in data:
        import aws_sdk_quicksight.types.word_cloud_word_scaling

        out["word_scaling"] = (
            aws_sdk_quicksight.types.word_cloud_word_scaling.deserialize_json(
                data["WordScaling"]
            )
        )
    if "CloudLayout" in data:
        import aws_sdk_quicksight.types.word_cloud_cloud_layout

        out["cloud_layout"] = (
            aws_sdk_quicksight.types.word_cloud_cloud_layout.deserialize_json(
                data["CloudLayout"]
            )
        )
    if "WordCasing" in data:
        import aws_sdk_quicksight.types.word_cloud_word_casing

        out["word_casing"] = (
            aws_sdk_quicksight.types.word_cloud_word_casing.deserialize_json(
                data["WordCasing"]
            )
        )
    if "WordPadding" in data:
        import aws_sdk_quicksight.types.word_cloud_word_padding

        out["word_padding"] = (
            aws_sdk_quicksight.types.word_cloud_word_padding.deserialize_json(
                data["WordPadding"]
            )
        )
    if "MaximumStringLength" in data:
        out["maximum_string_length"] = data["MaximumStringLength"]
    return out

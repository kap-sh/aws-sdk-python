"""Generated from Smithy shape ``com.amazonaws.macie2#AllowListCriteria``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string_min1_max512_pattern_ss
    import aws_sdk_macie2.types.s3_words_list


class AllowListCriteria(TypedDict):
    regex: NotRequired[
        "aws_sdk_macie2.types.__string_min1_max512_pattern_ss.__stringMin1Max512PatternSS"
    ]
    """<p>The regular expression (<i>regex</i>) that defines the text pattern to ignore. The expression can contain as many as 512 characters.</p>"""
    s3_words_list: NotRequired["aws_sdk_macie2.types.s3_words_list.S3WordsList"]
    """<p>The location and name of the S3 object that lists specific text to ignore.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AllowListCriteria) -> dict:
    out: dict = {}
    if "regex" in value:
        out["regex"] = value["regex"]
    if "s3_words_list" in value:
        import aws_sdk_macie2.types.s3_words_list

        out["s3WordsList"] = aws_sdk_macie2.types.s3_words_list.serialize_json(
            value["s3_words_list"]
        )
    return out


def deserialize_json(data: dict) -> AllowListCriteria:
    out: AllowListCriteria = {}  # type: ignore[typeddict-item]
    if "regex" in data:
        out["regex"] = data["regex"]
    if "s3WordsList" in data:
        import aws_sdk_macie2.types.s3_words_list

        out["s3_words_list"] = aws_sdk_macie2.types.s3_words_list.deserialize_json(
            data["s3WordsList"]
        )
    return out

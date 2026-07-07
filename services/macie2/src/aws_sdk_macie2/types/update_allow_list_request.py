"""Generated from Smithy shape ``com.amazonaws.macie2#UpdateAllowListRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string
    import aws_sdk_macie2.types.__string_min1_max128_pattern
    import aws_sdk_macie2.types.__string_min1_max512_pattern_ss
    import aws_sdk_macie2.types.allow_list_criteria


class UpdateAllowListRequest(TypedDict, closed=True):
    criteria: NotRequired["aws_sdk_macie2.types.allow_list_criteria.AllowListCriteria"]
    """<p>The criteria that specify the text or text pattern to ignore. The criteria can be the location and name of an S3 object that lists specific text to ignore (s3WordsList), or a regular expression that defines a text pattern to ignore (regex).</p> <p>You can change a list's underlying criteria, such as the name of the S3 object or the regular expression to use. However, you can't change the type from s3WordsList to regex or the other way around.</p>"""
    description: NotRequired[
        "aws_sdk_macie2.types.__string_min1_max512_pattern_ss.__stringMin1Max512PatternSS"
    ]
    """<p>A custom description of the allow list. The description can contain as many as 512 characters.</p>"""
    id: "aws_sdk_macie2.types.__string.__string"
    """<p>The unique identifier for the Amazon Macie resource that the request applies to.</p>"""
    name: NotRequired[
        "aws_sdk_macie2.types.__string_min1_max128_pattern.__stringMin1Max128Pattern"
    ]
    """<p>A custom name for the allow list. The name can contain as many as 128 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAllowListRequest) -> dict:
    out: dict = {}
    if "criteria" in value:
        import aws_sdk_macie2.types.allow_list_criteria

        out["criteria"] = aws_sdk_macie2.types.allow_list_criteria.serialize_json(
            value["criteria"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdateAllowListRequest:
    out: UpdateAllowListRequest = {}  # type: ignore[typeddict-item]
    if "criteria" in data:
        import aws_sdk_macie2.types.allow_list_criteria

        out["criteria"] = aws_sdk_macie2.types.allow_list_criteria.deserialize_json(
            data["criteria"]
        )
    if "description" in data:
        out["description"] = data["description"]
    if "name" in data:
        out["name"] = data["name"]
    return out

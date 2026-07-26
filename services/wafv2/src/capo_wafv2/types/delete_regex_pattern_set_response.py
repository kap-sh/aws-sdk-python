"""Generated from Smithy shape ``com.amazonaws.wafv2#DeleteRegexPatternSetResponse``."""

from typing_extensions import TypedDict


class DeleteRegexPatternSetResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteRegexPatternSetResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteRegexPatternSetResponse:
    out: DeleteRegexPatternSetResponse = {}  # type: ignore[typeddict-item]
    return out

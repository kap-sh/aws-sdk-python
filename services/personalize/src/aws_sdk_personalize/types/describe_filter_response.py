"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeFilterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_personalize.types.filter


class DescribeFilterResponse(TypedDict, closed=True):
    filter: NotRequired["aws_sdk_personalize.types.filter.Filter"]
    """<p>The filter's details.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFilterResponse) -> dict:
    out: dict = {}
    if "filter" in value:
        import aws_sdk_personalize.types.filter

        out["filter"] = aws_sdk_personalize.types.filter.serialize_aws_json_1_1(
            value["filter"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFilterResponse:
    out: DescribeFilterResponse = {}  # type: ignore[typeddict-item]
    if "filter" in data:
        import aws_sdk_personalize.types.filter

        out["filter"] = aws_sdk_personalize.types.filter.deserialize_aws_json_1_1(
            data["filter"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.opensearch#DescribeInsightDetailsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.insight_field_list


class DescribeInsightDetailsResponse(TypedDict, closed=True):
    fields: "aws_sdk_opensearch.types.insight_field_list.InsightFieldList"
    """<p>The list of fields that contain detailed information about the insight.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeInsightDetailsResponse) -> dict:
    out: dict = {}
    import aws_sdk_opensearch.types.insight_field_list

    out["Fields"] = aws_sdk_opensearch.types.insight_field_list.serialize_json(
        value["fields"]
    )
    return out


def deserialize_json(data: dict) -> DescribeInsightDetailsResponse:
    out: DescribeInsightDetailsResponse = {}  # type: ignore[typeddict-item]
    if "Fields" in data:
        import aws_sdk_opensearch.types.insight_field_list

        out["fields"] = aws_sdk_opensearch.types.insight_field_list.deserialize_json(
            data["Fields"]
        )
    else:
        raise DeserializationError("DescribeInsightDetailsResponse.fields required")
    return out

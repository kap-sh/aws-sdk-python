"""Generated from Smithy shape ``com.amazonaws.inspector#DescribeExclusionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector.types.exclusion_map
    import aws_sdk_inspector.types.failed_items


class DescribeExclusionsResponse(TypedDict, closed=True):
    exclusions: "aws_sdk_inspector.types.exclusion_map.ExclusionMap"
    """<p>Information about the exclusions.</p>"""
    failed_items: "aws_sdk_inspector.types.failed_items.FailedItems"
    """<p>Exclusion details that cannot be described. An error code is provided for each failed item.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeExclusionsResponse) -> dict:
    out: dict = {}
    import aws_sdk_inspector.types.exclusion_map

    out["exclusions"] = aws_sdk_inspector.types.exclusion_map.serialize_aws_json_1_1(
        value["exclusions"]
    )
    import aws_sdk_inspector.types.failed_items

    out["failedItems"] = aws_sdk_inspector.types.failed_items.serialize_aws_json_1_1(
        value["failed_items"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeExclusionsResponse:
    out: DescribeExclusionsResponse = {}  # type: ignore[typeddict-item]
    if "exclusions" in data:
        import aws_sdk_inspector.types.exclusion_map

        out["exclusions"] = (
            aws_sdk_inspector.types.exclusion_map.deserialize_aws_json_1_1(
                data["exclusions"]
            )
        )
    else:
        raise DeserializationError("DescribeExclusionsResponse.exclusions required")
    if "failedItems" in data:
        import aws_sdk_inspector.types.failed_items

        out["failed_items"] = (
            aws_sdk_inspector.types.failed_items.deserialize_aws_json_1_1(
                data["failedItems"]
            )
        )
    else:
        raise DeserializationError("DescribeExclusionsResponse.failed_items required")
    return out

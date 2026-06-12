"""Generated from Smithy shape ``com.amazonaws.inspector#DescribeFindingsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector.types.failed_items
    import aws_sdk_inspector.types.finding_list


class DescribeFindingsResponse(TypedDict):
    findings: "aws_sdk_inspector.types.finding_list.FindingList"
    """<p>Information about the finding.</p>"""
    failed_items: "aws_sdk_inspector.types.failed_items.FailedItems"
    """<p>Finding details that cannot be described. An error code is provided for each failed item.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFindingsResponse) -> dict:
    out: dict = {}
    import aws_sdk_inspector.types.finding_list

    out["findings"] = aws_sdk_inspector.types.finding_list.serialize_aws_json_1_1(
        value["findings"]
    )
    import aws_sdk_inspector.types.failed_items

    out["failedItems"] = aws_sdk_inspector.types.failed_items.serialize_aws_json_1_1(
        value["failed_items"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFindingsResponse:
    out: DescribeFindingsResponse = {}  # type: ignore[typeddict-item]
    if "findings" in data:
        import aws_sdk_inspector.types.finding_list

        out["findings"] = aws_sdk_inspector.types.finding_list.deserialize_aws_json_1_1(
            data["findings"]
        )
    else:
        raise DeserializationError("DescribeFindingsResponse.findings required")
    if "failedItems" in data:
        import aws_sdk_inspector.types.failed_items

        out["failed_items"] = (
            aws_sdk_inspector.types.failed_items.deserialize_aws_json_1_1(
                data["failedItems"]
            )
        )
    else:
        raise DeserializationError("DescribeFindingsResponse.failed_items required")
    return out

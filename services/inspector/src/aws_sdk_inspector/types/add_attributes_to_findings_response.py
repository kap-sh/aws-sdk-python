"""Generated from Smithy shape ``com.amazonaws.inspector#AddAttributesToFindingsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector.types.failed_items


class AddAttributesToFindingsResponse(TypedDict):
    failed_items: "aws_sdk_inspector.types.failed_items.FailedItems"
    """<p>Attribute details that cannot be described. An error code is provided for each failed item.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddAttributesToFindingsResponse) -> dict:
    out: dict = {}
    import aws_sdk_inspector.types.failed_items

    out["failedItems"] = aws_sdk_inspector.types.failed_items.serialize_aws_json_1_1(
        value["failed_items"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AddAttributesToFindingsResponse:
    out: AddAttributesToFindingsResponse = {}  # type: ignore[typeddict-item]
    if "failedItems" in data:
        import aws_sdk_inspector.types.failed_items

        out["failed_items"] = (
            aws_sdk_inspector.types.failed_items.deserialize_aws_json_1_1(
                data["failedItems"]
            )
        )
    else:
        raise DeserializationError(
            "AddAttributesToFindingsResponse.failed_items required"
        )
    return out

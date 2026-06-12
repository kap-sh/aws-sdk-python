"""Generated from Smithy shape ``com.amazonaws.fms#BatchAssociateResourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_fms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_fms.types.failed_item_list
    import aws_sdk_fms.types.identifier


class BatchAssociateResourceResponse(TypedDict):
    resource_set_identifier: "aws_sdk_fms.types.identifier.Identifier"
    """<p>A unique identifier for the resource set, used in a request to refer to the resource set.</p>"""
    failed_items: "aws_sdk_fms.types.failed_item_list.FailedItemList"
    """<p>The resources that failed to associate to the resource set.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchAssociateResourceResponse) -> dict:
    out: dict = {}
    out["ResourceSetIdentifier"] = value["resource_set_identifier"]
    import aws_sdk_fms.types.failed_item_list

    out["FailedItems"] = aws_sdk_fms.types.failed_item_list.serialize_aws_json_1_1(
        value["failed_items"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchAssociateResourceResponse:
    out: BatchAssociateResourceResponse = {}  # type: ignore[typeddict-item]
    if "ResourceSetIdentifier" in data:
        out["resource_set_identifier"] = data["ResourceSetIdentifier"]
    else:
        raise DeserializationError(
            "BatchAssociateResourceResponse.resource_set_identifier required"
        )
    if "FailedItems" in data:
        import aws_sdk_fms.types.failed_item_list

        out["failed_items"] = (
            aws_sdk_fms.types.failed_item_list.deserialize_aws_json_1_1(
                data["FailedItems"]
            )
        )
    else:
        raise DeserializationError(
            "BatchAssociateResourceResponse.failed_items required"
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.billingconductor#BatchDisassociateResourcesFromCustomLineItemOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.disassociate_resources_response_list


class BatchDisassociateResourcesFromCustomLineItemOutput(TypedDict, closed=True):
    successfully_disassociated_resources: NotRequired[
        "aws_sdk_billingconductor.types.disassociate_resources_response_list.DisassociateResourcesResponseList"
    ]
    """<p> A list of <code>DisassociateResourceResponseElement</code> for each resource that's been disassociated from a percentage custom line item successfully. </p>"""
    failed_disassociated_resources: NotRequired[
        "aws_sdk_billingconductor.types.disassociate_resources_response_list.DisassociateResourcesResponseList"
    ]
    """<p> A list of <code>DisassociateResourceResponseElement</code> for each resource that failed disassociation from a percentage custom line item. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDisassociateResourcesFromCustomLineItemOutput) -> dict:
    out: dict = {}
    if "successfully_disassociated_resources" in value:
        import aws_sdk_billingconductor.types.disassociate_resources_response_list

        out["SuccessfullyDisassociatedResources"] = (
            aws_sdk_billingconductor.types.disassociate_resources_response_list.serialize_json(
                value["successfully_disassociated_resources"]
            )
        )
    if "failed_disassociated_resources" in value:
        import aws_sdk_billingconductor.types.disassociate_resources_response_list

        out["FailedDisassociatedResources"] = (
            aws_sdk_billingconductor.types.disassociate_resources_response_list.serialize_json(
                value["failed_disassociated_resources"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchDisassociateResourcesFromCustomLineItemOutput:
    out: BatchDisassociateResourcesFromCustomLineItemOutput = {}  # type: ignore[typeddict-item]
    if "SuccessfullyDisassociatedResources" in data:
        import aws_sdk_billingconductor.types.disassociate_resources_response_list

        out["successfully_disassociated_resources"] = (
            aws_sdk_billingconductor.types.disassociate_resources_response_list.deserialize_json(
                data["SuccessfullyDisassociatedResources"]
            )
        )
    if "FailedDisassociatedResources" in data:
        import aws_sdk_billingconductor.types.disassociate_resources_response_list

        out["failed_disassociated_resources"] = (
            aws_sdk_billingconductor.types.disassociate_resources_response_list.deserialize_json(
                data["FailedDisassociatedResources"]
            )
        )
    return out

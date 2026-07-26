"""Generated from Smithy shape ``com.amazonaws.billingconductor#BatchAssociateResourcesToCustomLineItemOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.associate_resources_response_list


class BatchAssociateResourcesToCustomLineItemOutput(TypedDict, closed=True):
    successfully_associated_resources: NotRequired[
        "capo_billingconductor.types.associate_resources_response_list.AssociateResourcesResponseList"
    ]
    """<p> A list of <code>AssociateResourceResponseElement</code> for each resource that's been associated to a percentage custom line item successfully. </p>"""
    failed_associated_resources: NotRequired[
        "capo_billingconductor.types.associate_resources_response_list.AssociateResourcesResponseList"
    ]
    """<p> A list of <code>AssociateResourceResponseElement</code> for each resource that failed association to a percentage custom line item. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchAssociateResourcesToCustomLineItemOutput) -> dict:
    out: dict = {}
    if "successfully_associated_resources" in value:
        import capo_billingconductor.types.associate_resources_response_list

        out["SuccessfullyAssociatedResources"] = (
            capo_billingconductor.types.associate_resources_response_list.serialize_json(
                value["successfully_associated_resources"]
            )
        )
    if "failed_associated_resources" in value:
        import capo_billingconductor.types.associate_resources_response_list

        out["FailedAssociatedResources"] = (
            capo_billingconductor.types.associate_resources_response_list.serialize_json(
                value["failed_associated_resources"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchAssociateResourcesToCustomLineItemOutput:
    out: BatchAssociateResourcesToCustomLineItemOutput = {}  # type: ignore[typeddict-item]
    if "SuccessfullyAssociatedResources" in data:
        import capo_billingconductor.types.associate_resources_response_list

        out["successfully_associated_resources"] = (
            capo_billingconductor.types.associate_resources_response_list.deserialize_json(
                data["SuccessfullyAssociatedResources"]
            )
        )
    if "FailedAssociatedResources" in data:
        import capo_billingconductor.types.associate_resources_response_list

        out["failed_associated_resources"] = (
            capo_billingconductor.types.associate_resources_response_list.deserialize_json(
                data["FailedAssociatedResources"]
            )
        )
    return out

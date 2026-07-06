"""Generated from Smithy shape ``com.amazonaws.servicecatalog#BatchDisassociateServiceActionFromProvisioningArtifactOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.failed_service_action_associations


class BatchDisassociateServiceActionFromProvisioningArtifactOutput(
    TypedDict, closed=True
):
    failed_service_action_associations: NotRequired[
        "aws_sdk_service_catalog.types.failed_service_action_associations.FailedServiceActionAssociations"
    ]
    """<p>An object that contains a list of errors, along with information to help you identify the self-service action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: BatchDisassociateServiceActionFromProvisioningArtifactOutput,
) -> dict:
    out: dict = {}
    if "failed_service_action_associations" in value:
        import aws_sdk_service_catalog.types.failed_service_action_associations

        out["FailedServiceActionAssociations"] = (
            aws_sdk_service_catalog.types.failed_service_action_associations.serialize_aws_json_1_1(
                value["failed_service_action_associations"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> BatchDisassociateServiceActionFromProvisioningArtifactOutput:
    out: BatchDisassociateServiceActionFromProvisioningArtifactOutput = {}  # type: ignore[typeddict-item]
    if "FailedServiceActionAssociations" in data:
        import aws_sdk_service_catalog.types.failed_service_action_associations

        out["failed_service_action_associations"] = (
            aws_sdk_service_catalog.types.failed_service_action_associations.deserialize_aws_json_1_1(
                data["FailedServiceActionAssociations"]
            )
        )
    return out

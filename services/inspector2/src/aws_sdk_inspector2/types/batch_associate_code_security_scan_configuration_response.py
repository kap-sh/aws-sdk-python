"""Generated from Smithy shape ``com.amazonaws.inspector2#BatchAssociateCodeSecurityScanConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.failed_association_result_list
    import aws_sdk_inspector2.types.successful_association_result_list


class BatchAssociateCodeSecurityScanConfigurationResponse(TypedDict):
    failed_associations: NotRequired[
        "aws_sdk_inspector2.types.failed_association_result_list.FailedAssociationResultList"
    ]
    """<p>Details of any code repositories that failed to be associated with the scan configuration.</p>"""
    successful_associations: NotRequired[
        "aws_sdk_inspector2.types.successful_association_result_list.SuccessfulAssociationResultList"
    ]
    """<p>Details of code repositories that were successfully associated with the scan configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchAssociateCodeSecurityScanConfigurationResponse) -> dict:
    out: dict = {}
    if "failed_associations" in value:
        import aws_sdk_inspector2.types.failed_association_result_list

        out["failedAssociations"] = (
            aws_sdk_inspector2.types.failed_association_result_list.serialize_json(
                value["failed_associations"]
            )
        )
    if "successful_associations" in value:
        import aws_sdk_inspector2.types.successful_association_result_list

        out["successfulAssociations"] = (
            aws_sdk_inspector2.types.successful_association_result_list.serialize_json(
                value["successful_associations"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchAssociateCodeSecurityScanConfigurationResponse:
    out: BatchAssociateCodeSecurityScanConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "failedAssociations" in data:
        import aws_sdk_inspector2.types.failed_association_result_list

        out["failed_associations"] = (
            aws_sdk_inspector2.types.failed_association_result_list.deserialize_json(
                data["failedAssociations"]
            )
        )
    if "successfulAssociations" in data:
        import aws_sdk_inspector2.types.successful_association_result_list

        out["successful_associations"] = (
            aws_sdk_inspector2.types.successful_association_result_list.deserialize_json(
                data["successfulAssociations"]
            )
        )
    return out

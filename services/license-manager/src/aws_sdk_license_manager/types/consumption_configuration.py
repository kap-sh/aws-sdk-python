"""Generated from Smithy shape ``com.amazonaws.licensemanager#ConsumptionConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.borrow_configuration
    import aws_sdk_license_manager.types.provisional_configuration
    import aws_sdk_license_manager.types.renew_type


class ConsumptionConfiguration(TypedDict):
    renew_type: NotRequired["aws_sdk_license_manager.types.renew_type.RenewType"]
    """<p>Renewal frequency.</p>"""
    provisional_configuration: NotRequired[
        "aws_sdk_license_manager.types.provisional_configuration.ProvisionalConfiguration"
    ]
    """<p>Details about a provisional configuration.</p>"""
    borrow_configuration: NotRequired[
        "aws_sdk_license_manager.types.borrow_configuration.BorrowConfiguration"
    ]
    """<p>Details about a borrow configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConsumptionConfiguration) -> dict:
    out: dict = {}
    if "renew_type" in value:
        import aws_sdk_license_manager.types.renew_type

        out["RenewType"] = (
            aws_sdk_license_manager.types.renew_type.serialize_aws_json_1_1(
                value["renew_type"]
            )
        )
    if "provisional_configuration" in value:
        import aws_sdk_license_manager.types.provisional_configuration

        out["ProvisionalConfiguration"] = (
            aws_sdk_license_manager.types.provisional_configuration.serialize_aws_json_1_1(
                value["provisional_configuration"]
            )
        )
    if "borrow_configuration" in value:
        import aws_sdk_license_manager.types.borrow_configuration

        out["BorrowConfiguration"] = (
            aws_sdk_license_manager.types.borrow_configuration.serialize_aws_json_1_1(
                value["borrow_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConsumptionConfiguration:
    out: ConsumptionConfiguration = {}  # type: ignore[typeddict-item]
    if "RenewType" in data:
        import aws_sdk_license_manager.types.renew_type

        out["renew_type"] = (
            aws_sdk_license_manager.types.renew_type.deserialize_aws_json_1_1(
                data["RenewType"]
            )
        )
    if "ProvisionalConfiguration" in data:
        import aws_sdk_license_manager.types.provisional_configuration

        out["provisional_configuration"] = (
            aws_sdk_license_manager.types.provisional_configuration.deserialize_aws_json_1_1(
                data["ProvisionalConfiguration"]
            )
        )
    if "BorrowConfiguration" in data:
        import aws_sdk_license_manager.types.borrow_configuration

        out["borrow_configuration"] = (
            aws_sdk_license_manager.types.borrow_configuration.deserialize_aws_json_1_1(
                data["BorrowConfiguration"]
            )
        )
    return out

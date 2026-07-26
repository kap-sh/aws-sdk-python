"""Generated from Smithy shape ``com.amazonaws.licensemanager#ConsumptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.borrow_configuration
    import capo_license_manager.types.provisional_configuration
    import capo_license_manager.types.renew_type


class ConsumptionConfiguration(TypedDict, closed=True):
    renew_type: NotRequired["capo_license_manager.types.renew_type.RenewType"]
    """<p>Renewal frequency.</p>"""
    provisional_configuration: NotRequired[
        "capo_license_manager.types.provisional_configuration.ProvisionalConfiguration"
    ]
    """<p>Details about a provisional configuration.</p>"""
    borrow_configuration: NotRequired[
        "capo_license_manager.types.borrow_configuration.BorrowConfiguration"
    ]
    """<p>Details about a borrow configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConsumptionConfiguration) -> dict:
    out: dict = {}
    if "renew_type" in value:
        import capo_license_manager.types.renew_type

        out["RenewType"] = capo_license_manager.types.renew_type.serialize_aws_json_1_1(
            value["renew_type"]
        )
    if "provisional_configuration" in value:
        import capo_license_manager.types.provisional_configuration

        out["ProvisionalConfiguration"] = (
            capo_license_manager.types.provisional_configuration.serialize_aws_json_1_1(
                value["provisional_configuration"]
            )
        )
    if "borrow_configuration" in value:
        import capo_license_manager.types.borrow_configuration

        out["BorrowConfiguration"] = (
            capo_license_manager.types.borrow_configuration.serialize_aws_json_1_1(
                value["borrow_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConsumptionConfiguration:
    out: ConsumptionConfiguration = {}  # type: ignore[typeddict-item]
    if "RenewType" in data:
        import capo_license_manager.types.renew_type

        out["renew_type"] = (
            capo_license_manager.types.renew_type.deserialize_aws_json_1_1(
                data["RenewType"]
            )
        )
    if "ProvisionalConfiguration" in data:
        import capo_license_manager.types.provisional_configuration

        out["provisional_configuration"] = (
            capo_license_manager.types.provisional_configuration.deserialize_aws_json_1_1(
                data["ProvisionalConfiguration"]
            )
        )
    if "BorrowConfiguration" in data:
        import capo_license_manager.types.borrow_configuration

        out["borrow_configuration"] = (
            capo_license_manager.types.borrow_configuration.deserialize_aws_json_1_1(
                data["BorrowConfiguration"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#DisassociateUserResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_license_manager_user_subscriptions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager_user_subscriptions.types.instance_user_summary


class DisassociateUserResponse(TypedDict, closed=True):
    instance_user_summary: "aws_sdk_license_manager_user_subscriptions.types.instance_user_summary.InstanceUserSummary"
    """<p>Metadata that describes the associate user operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateUserResponse) -> dict:
    out: dict = {}
    import aws_sdk_license_manager_user_subscriptions.types.instance_user_summary

    out["InstanceUserSummary"] = (
        aws_sdk_license_manager_user_subscriptions.types.instance_user_summary.serialize_json(
            value["instance_user_summary"]
        )
    )
    return out


def deserialize_json(data: dict) -> DisassociateUserResponse:
    out: DisassociateUserResponse = {}  # type: ignore[typeddict-item]
    if "InstanceUserSummary" in data:
        import aws_sdk_license_manager_user_subscriptions.types.instance_user_summary

        out["instance_user_summary"] = (
            aws_sdk_license_manager_user_subscriptions.types.instance_user_summary.deserialize_json(
                data["InstanceUserSummary"]
            )
        )
    else:
        raise DeserializationError(
            "DisassociateUserResponse.instance_user_summary required"
        )
    return out

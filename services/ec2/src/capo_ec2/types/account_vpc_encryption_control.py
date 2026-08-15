"""Generated from Smithy shape ``com.amazonaws.ec2#AccountVpcEncryptionControl``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.account_vpc_encryption_control_exclusions
    import capo_ec2.types.account_vpc_encryption_control_mode
    import capo_ec2.types.account_vpc_encryption_control_state
    import capo_ec2.types.managed_by
    import capo_ec2.types.millisecond_date_time


class AccountVpcEncryptionControl(TypedDict, closed=True):
    state: NotRequired[
        "capo_ec2.types.account_vpc_encryption_control_state.AccountVpcEncryptionControlState"
    ]
    """<p>The current state of the account-level VPC Encryption Control configuration.</p>"""
    mode: NotRequired[
        "capo_ec2.types.account_vpc_encryption_control_mode.AccountVpcEncryptionControlMode"
    ]
    """<p>The encryption mode for the account-level VPC Encryption Control configuration.</p>"""
    exclusions: NotRequired[
        "capo_ec2.types.account_vpc_encryption_control_exclusions.AccountVpcEncryptionControlExclusions"
    ]
    """<p>Information about the traffic exclusions for the account-level VPC Encryption Control configuration.</p>"""
    managed_by: NotRequired["capo_ec2.types.managed_by.ManagedBy"]
    """<p>The entity that manages the account-level VPC Encryption Control configuration.</p>"""
    last_update_timestamp: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when the account-level VPC Encryption Control configuration was last updated.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AccountVpcEncryptionControl, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "state" in value:
        import capo_ec2.types.account_vpc_encryption_control_state

        capo_ec2.types.account_vpc_encryption_control_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "mode" in value:
        import capo_ec2.types.account_vpc_encryption_control_mode

        capo_ec2.types.account_vpc_encryption_control_mode.serialize_ec2_query(
            value["mode"], pairs, f"{key_prefix}Mode"
        )
    if "exclusions" in value:
        import capo_ec2.types.account_vpc_encryption_control_exclusions

        capo_ec2.types.account_vpc_encryption_control_exclusions.serialize_ec2_query(
            value["exclusions"], pairs, f"{key_prefix}Exclusions"
        )
    if "managed_by" in value:
        import capo_ec2.types.managed_by

        capo_ec2.types.managed_by.serialize_ec2_query(
            value["managed_by"], pairs, f"{key_prefix}ManagedBy"
        )
    if "last_update_timestamp" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["last_update_timestamp"], pairs, f"{key_prefix}LastUpdateTimestamp"
        )


def deserialize_ec2_query(el: Element) -> AccountVpcEncryptionControl:
    out: AccountVpcEncryptionControl = {}  # type: ignore[typeddict-item]
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.account_vpc_encryption_control_state

        out["state"] = (
            capo_ec2.types.account_vpc_encryption_control_state.deserialize_ec2_query(
                child_state
            )
        )
    child_mode = el.find("mode")
    if child_mode is not None:
        import capo_ec2.types.account_vpc_encryption_control_mode

        out["mode"] = (
            capo_ec2.types.account_vpc_encryption_control_mode.deserialize_ec2_query(
                child_mode
            )
        )
    child_exclusions = el.find("exclusions")
    if child_exclusions is not None:
        import capo_ec2.types.account_vpc_encryption_control_exclusions

        out["exclusions"] = (
            capo_ec2.types.account_vpc_encryption_control_exclusions.deserialize_ec2_query(
                child_exclusions
            )
        )
    child_managed_by = el.find("managedBy")
    if child_managed_by is not None:
        import capo_ec2.types.managed_by

        out["managed_by"] = capo_ec2.types.managed_by.deserialize_ec2_query(
            child_managed_by
        )
    child_last_update_timestamp = el.find("lastUpdateTimestamp")
    if child_last_update_timestamp is not None:
        import capo_ec2.types.millisecond_date_time

        out["last_update_timestamp"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_last_update_timestamp
            )
        )
    return out

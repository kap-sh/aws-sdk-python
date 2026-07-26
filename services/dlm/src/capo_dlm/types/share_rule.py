"""Generated from Smithy shape ``com.amazonaws.dlm#ShareRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dlm.types.interval
    import capo_dlm.types.retention_interval_unit_values
    import capo_dlm.types.share_target_account_list


class ShareRule(TypedDict, closed=True):
    target_accounts: NotRequired[
        "capo_dlm.types.share_target_account_list.ShareTargetAccountList"
    ]
    """<p>The IDs of the Amazon Web Services accounts with which to share the snapshots.</p>"""
    unshare_interval: NotRequired["capo_dlm.types.interval.Interval"]
    """<p>The period after which snapshots that are shared with other Amazon Web Services accounts are automatically unshared.</p>"""
    unshare_interval_unit: NotRequired[
        "capo_dlm.types.retention_interval_unit_values.RetentionIntervalUnitValues"
    ]
    """<p>The unit of time for the automatic unsharing interval.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ShareRule) -> dict:
    out: dict = {}
    if "target_accounts" in value:
        import capo_dlm.types.share_target_account_list

        out["TargetAccounts"] = capo_dlm.types.share_target_account_list.serialize_json(
            value["target_accounts"]
        )
    if "unshare_interval" in value:
        out["UnshareInterval"] = value["unshare_interval"]
    if "unshare_interval_unit" in value:
        import capo_dlm.types.retention_interval_unit_values

        out["UnshareIntervalUnit"] = (
            capo_dlm.types.retention_interval_unit_values.serialize_json(
                value["unshare_interval_unit"]
            )
        )
    return out


def deserialize_json(data: dict) -> ShareRule:
    out: ShareRule = {}  # type: ignore[typeddict-item]
    if "TargetAccounts" in data:
        import capo_dlm.types.share_target_account_list

        out["target_accounts"] = (
            capo_dlm.types.share_target_account_list.deserialize_json(
                data["TargetAccounts"]
            )
        )
    if "UnshareInterval" in data:
        out["unshare_interval"] = data["UnshareInterval"]
    if "UnshareIntervalUnit" in data:
        import capo_dlm.types.retention_interval_unit_values

        out["unshare_interval_unit"] = (
            capo_dlm.types.retention_interval_unit_values.deserialize_json(
                data["UnshareIntervalUnit"]
            )
        )
    return out

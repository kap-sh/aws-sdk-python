"""Generated from Smithy shape ``com.amazonaws.inspector2#DescribeOrganizationConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.auto_enable


class DescribeOrganizationConfigurationResponse(TypedDict, closed=True):
    auto_enable: NotRequired["capo_inspector2.types.auto_enable.AutoEnable"]
    """<p>The scan types are automatically enabled for new members of your organization.</p>"""
    max_account_limit_reached: NotRequired["bool"]
    """<p>Represents whether your organization has reached the maximum Amazon Web Services account limit for Amazon Inspector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeOrganizationConfigurationResponse) -> dict:
    out: dict = {}
    if "auto_enable" in value:
        import capo_inspector2.types.auto_enable

        out["autoEnable"] = capo_inspector2.types.auto_enable.serialize_json(
            value["auto_enable"]
        )
    if "max_account_limit_reached" in value:
        out["maxAccountLimitReached"] = value["max_account_limit_reached"]
    return out


def deserialize_json(data: dict) -> DescribeOrganizationConfigurationResponse:
    out: DescribeOrganizationConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "autoEnable" in data:
        import capo_inspector2.types.auto_enable

        out["auto_enable"] = capo_inspector2.types.auto_enable.deserialize_json(
            data["autoEnable"]
        )
    if "maxAccountLimitReached" in data:
        out["max_account_limit_reached"] = data["maxAccountLimitReached"]
    return out

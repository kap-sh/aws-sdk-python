"""Generated from Smithy shape ``com.amazonaws.macie2#DescribeOrganizationConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__boolean


class DescribeOrganizationConfigurationResponse(TypedDict):
    auto_enable: NotRequired["aws_sdk_macie2.types.__boolean.__boolean"]
    """<p>Specifies whether Amazon Macie is enabled automatically for accounts that are added to the organization.</p>"""
    max_account_limit_reached: NotRequired["aws_sdk_macie2.types.__boolean.__boolean"]
    """<p>Specifies whether the maximum number of Amazon Macie member accounts are part of the organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeOrganizationConfigurationResponse) -> dict:
    out: dict = {}
    if "auto_enable" in value:
        out["autoEnable"] = value["auto_enable"]
    if "max_account_limit_reached" in value:
        out["maxAccountLimitReached"] = value["max_account_limit_reached"]
    return out


def deserialize_json(data: dict) -> DescribeOrganizationConfigurationResponse:
    out: DescribeOrganizationConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "autoEnable" in data:
        out["auto_enable"] = data["autoEnable"]
    if "maxAccountLimitReached" in data:
        out["max_account_limit_reached"] = data["maxAccountLimitReached"]
    return out

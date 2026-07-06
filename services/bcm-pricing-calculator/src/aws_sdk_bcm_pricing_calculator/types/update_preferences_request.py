"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#UpdatePreferencesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.rate_types


class UpdatePreferencesRequest(TypedDict, closed=True):
    management_account_rate_type_selections: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.rate_types.RateTypes"
    ]
    """<p> The updated preferred rate types for the management account. </p>"""
    member_account_rate_type_selections: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.rate_types.RateTypes"
    ]
    """<p> The updated preferred rate types for member accounts. </p>"""
    standalone_account_rate_type_selections: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.rate_types.RateTypes"
    ]
    """<p> The updated preferred rate types for a standalone account. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdatePreferencesRequest) -> dict:
    out: dict = {}
    if "management_account_rate_type_selections" in value:
        import aws_sdk_bcm_pricing_calculator.types.rate_types

        out["managementAccountRateTypeSelections"] = (
            aws_sdk_bcm_pricing_calculator.types.rate_types.serialize_aws_json_1_0(
                value["management_account_rate_type_selections"]
            )
        )
    if "member_account_rate_type_selections" in value:
        import aws_sdk_bcm_pricing_calculator.types.rate_types

        out["memberAccountRateTypeSelections"] = (
            aws_sdk_bcm_pricing_calculator.types.rate_types.serialize_aws_json_1_0(
                value["member_account_rate_type_selections"]
            )
        )
    if "standalone_account_rate_type_selections" in value:
        import aws_sdk_bcm_pricing_calculator.types.rate_types

        out["standaloneAccountRateTypeSelections"] = (
            aws_sdk_bcm_pricing_calculator.types.rate_types.serialize_aws_json_1_0(
                value["standalone_account_rate_type_selections"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdatePreferencesRequest:
    out: UpdatePreferencesRequest = {}  # type: ignore[typeddict-item]
    if "managementAccountRateTypeSelections" in data:
        import aws_sdk_bcm_pricing_calculator.types.rate_types

        out["management_account_rate_type_selections"] = (
            aws_sdk_bcm_pricing_calculator.types.rate_types.deserialize_aws_json_1_0(
                data["managementAccountRateTypeSelections"]
            )
        )
    if "memberAccountRateTypeSelections" in data:
        import aws_sdk_bcm_pricing_calculator.types.rate_types

        out["member_account_rate_type_selections"] = (
            aws_sdk_bcm_pricing_calculator.types.rate_types.deserialize_aws_json_1_0(
                data["memberAccountRateTypeSelections"]
            )
        )
    if "standaloneAccountRateTypeSelections" in data:
        import aws_sdk_bcm_pricing_calculator.types.rate_types

        out["standalone_account_rate_type_selections"] = (
            aws_sdk_bcm_pricing_calculator.types.rate_types.deserialize_aws_json_1_0(
                data["standaloneAccountRateTypeSelections"]
            )
        )
    return out

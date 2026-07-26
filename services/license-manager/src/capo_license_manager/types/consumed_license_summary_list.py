"""Generated from Smithy shape ``com.amazonaws.licensemanager#ConsumedLicenseSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_license_manager.types.consumed_license_summary

ConsumedLicenseSummaryList: TypeAlias = list[
    "capo_license_manager.types.consumed_license_summary.ConsumedLicenseSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConsumedLicenseSummaryList) -> list:
    import capo_license_manager.types.consumed_license_summary

    out: list = []
    for item in value:
        out.append(
            capo_license_manager.types.consumed_license_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConsumedLicenseSummaryList:
    import capo_license_manager.types.consumed_license_summary

    out: ConsumedLicenseSummaryList = []
    for item in data:
        out.append(
            capo_license_manager.types.consumed_license_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out

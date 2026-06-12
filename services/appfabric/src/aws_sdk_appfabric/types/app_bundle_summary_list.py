"""Generated from Smithy shape ``com.amazonaws.appfabric#AppBundleSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appfabric.types.app_bundle_summary

AppBundleSummaryList: TypeAlias = list[
    "aws_sdk_appfabric.types.app_bundle_summary.AppBundleSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AppBundleSummaryList) -> list:
    import aws_sdk_appfabric.types.app_bundle_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_appfabric.types.app_bundle_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AppBundleSummaryList:
    import aws_sdk_appfabric.types.app_bundle_summary

    out: AppBundleSummaryList = []
    for item in data:
        out.append(aws_sdk_appfabric.types.app_bundle_summary.deserialize_json(item))
    return out

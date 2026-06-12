"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#MatchOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bcm_dashboards.types.match_option

MatchOptions: TypeAlias = list["aws_sdk_bcm_dashboards.types.match_option.MatchOption"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MatchOptions) -> list:
    import aws_sdk_bcm_dashboards.types.match_option

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bcm_dashboards.types.match_option.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> MatchOptions:
    import aws_sdk_bcm_dashboards.types.match_option

    out: MatchOptions = []
    for item in data:
        out.append(
            aws_sdk_bcm_dashboards.types.match_option.deserialize_aws_json_1_0(item)
        )
    return out

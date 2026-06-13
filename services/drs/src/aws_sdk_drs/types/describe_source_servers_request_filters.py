"""Generated from Smithy shape ``com.amazonaws.drs#DescribeSourceServersRequestFilters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_drs.types.account_i_ds
    import aws_sdk_drs.types.bounded_string
    import aws_sdk_drs.types.describe_source_servers_request_filters_i_ds


class DescribeSourceServersRequestFilters(TypedDict):
    source_server_i_ds: NotRequired[
        "aws_sdk_drs.types.describe_source_servers_request_filters_i_ds.DescribeSourceServersRequestFiltersIDs"
    ]
    """<p>An array of Source Servers IDs that should be returned. An empty array means all Source Servers.</p>"""
    hardware_id: NotRequired["aws_sdk_drs.types.bounded_string.BoundedString"]
    """<p>An ID that describes the hardware of the Source Server. This is either an EC2 instance id, a VMware uuid or a mac address.</p>"""
    staging_account_i_ds: NotRequired["aws_sdk_drs.types.account_i_ds.AccountIDs"]
    """<p>An array of staging account IDs that extended source servers belong to. An empty array means all source servers will be shown.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSourceServersRequestFilters) -> dict:
    out: dict = {}
    if "source_server_i_ds" in value:
        import aws_sdk_drs.types.describe_source_servers_request_filters_i_ds

        out["sourceServerIDs"] = (
            aws_sdk_drs.types.describe_source_servers_request_filters_i_ds.serialize_json(
                value["source_server_i_ds"]
            )
        )
    if "hardware_id" in value:
        out["hardwareId"] = value["hardware_id"]
    if "staging_account_i_ds" in value:
        import aws_sdk_drs.types.account_i_ds

        out["stagingAccountIDs"] = aws_sdk_drs.types.account_i_ds.serialize_json(
            value["staging_account_i_ds"]
        )
    return out


def deserialize_json(data: dict) -> DescribeSourceServersRequestFilters:
    out: DescribeSourceServersRequestFilters = {}  # type: ignore[typeddict-item]
    if "sourceServerIDs" in data:
        import aws_sdk_drs.types.describe_source_servers_request_filters_i_ds

        out["source_server_i_ds"] = (
            aws_sdk_drs.types.describe_source_servers_request_filters_i_ds.deserialize_json(
                data["sourceServerIDs"]
            )
        )
    if "hardwareId" in data:
        out["hardware_id"] = data["hardwareId"]
    if "stagingAccountIDs" in data:
        import aws_sdk_drs.types.account_i_ds

        out["staging_account_i_ds"] = aws_sdk_drs.types.account_i_ds.deserialize_json(
            data["stagingAccountIDs"]
        )
    return out

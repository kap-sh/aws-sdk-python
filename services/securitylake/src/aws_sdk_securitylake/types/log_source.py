"""Generated from Smithy shape ``com.amazonaws.securitylake#LogSource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.aws_account_id
    import aws_sdk_securitylake.types.log_source_resource_list
    import aws_sdk_securitylake.types.region


class LogSource(TypedDict):
    account: NotRequired["aws_sdk_securitylake.types.aws_account_id.AwsAccountId"]
    """<p>Specify the account from which you want to collect logs.</p>"""
    region: NotRequired["aws_sdk_securitylake.types.region.Region"]
    """<p>Specify the Regions from which you want to collect logs.</p>"""
    sources: NotRequired[
        "aws_sdk_securitylake.types.log_source_resource_list.LogSourceResourceList"
    ]
    """<p>Specify the sources from which you want to collect logs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogSource) -> dict:
    out: dict = {}
    if "account" in value:
        out["account"] = value["account"]
    if "region" in value:
        out["region"] = value["region"]
    if "sources" in value:
        import aws_sdk_securitylake.types.log_source_resource_list

        out["sources"] = (
            aws_sdk_securitylake.types.log_source_resource_list.serialize_json(
                value["sources"]
            )
        )
    return out


def deserialize_json(data: dict) -> LogSource:
    out: LogSource = {}  # type: ignore[typeddict-item]
    if "account" in data:
        out["account"] = data["account"]
    if "region" in data:
        out["region"] = data["region"]
    if "sources" in data:
        import aws_sdk_securitylake.types.log_source_resource_list

        out["sources"] = (
            aws_sdk_securitylake.types.log_source_resource_list.deserialize_json(
                data["sources"]
            )
        )
    return out

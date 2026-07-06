"""Generated from Smithy shape ``com.amazonaws.securitylake#AwsLogSourceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_securitylake.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.account_list
    import aws_sdk_securitylake.types.aws_log_source_name
    import aws_sdk_securitylake.types.aws_log_source_version
    import aws_sdk_securitylake.types.region_list


class AwsLogSourceConfiguration(TypedDict, closed=True):
    accounts: NotRequired["aws_sdk_securitylake.types.account_list.AccountList"]
    """<p>Specify the Amazon Web Services account information where you want to enable Security Lake.</p>"""
    regions: "aws_sdk_securitylake.types.region_list.RegionList"
    """<p>Specify the Regions where you want to enable Security Lake.</p>"""
    source_name: "aws_sdk_securitylake.types.aws_log_source_name.AwsLogSourceName"
    """<p>The name for a Amazon Web Services source. </p>"""
    source_version: (
        "aws_sdk_securitylake.types.aws_log_source_version.AwsLogSourceVersion"
    )
    """<p>The version for a Amazon Web Services source. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsLogSourceConfiguration) -> dict:
    out: dict = {}
    if "accounts" in value:
        import aws_sdk_securitylake.types.account_list

        out["accounts"] = aws_sdk_securitylake.types.account_list.serialize_json(
            value["accounts"]
        )
    import aws_sdk_securitylake.types.region_list

    out["regions"] = aws_sdk_securitylake.types.region_list.serialize_json(
        value["regions"]
    )
    import aws_sdk_securitylake.types.aws_log_source_name

    out["sourceName"] = aws_sdk_securitylake.types.aws_log_source_name.serialize_json(
        value["source_name"]
    )
    out["sourceVersion"] = value.get("source_version", "latest")
    return out


def deserialize_json(data: dict) -> AwsLogSourceConfiguration:
    out: AwsLogSourceConfiguration = {}  # type: ignore[typeddict-item]
    if "accounts" in data:
        import aws_sdk_securitylake.types.account_list

        out["accounts"] = aws_sdk_securitylake.types.account_list.deserialize_json(
            data["accounts"]
        )
    if "regions" in data:
        import aws_sdk_securitylake.types.region_list

        out["regions"] = aws_sdk_securitylake.types.region_list.deserialize_json(
            data["regions"]
        )
    else:
        raise DeserializationError("AwsLogSourceConfiguration.regions required")
    if "sourceName" in data:
        import aws_sdk_securitylake.types.aws_log_source_name

        out["source_name"] = (
            aws_sdk_securitylake.types.aws_log_source_name.deserialize_json(
                data["sourceName"]
            )
        )
    else:
        raise DeserializationError("AwsLogSourceConfiguration.source_name required")
    if "sourceVersion" in data:
        out["source_version"] = data["sourceVersion"]
    else:
        out["source_version"] = "latest"
    return out

"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#DescribeExportConfigurationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.exports_info
    import aws_sdk_application_discovery_service.types.next_token


class DescribeExportConfigurationsResponse(TypedDict):
    exports_info: NotRequired[
        "aws_sdk_application_discovery_service.types.exports_info.ExportsInfo"
    ]
    """<p></p>"""
    next_token: NotRequired[
        "aws_sdk_application_discovery_service.types.next_token.NextToken"
    ]
    """<p>The token from the previous call to describe-export-tasks.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeExportConfigurationsResponse) -> dict:
    out: dict = {}
    if "exports_info" in value:
        import aws_sdk_application_discovery_service.types.exports_info

        out["exportsInfo"] = (
            aws_sdk_application_discovery_service.types.exports_info.serialize_aws_json_1_1(
                value["exports_info"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeExportConfigurationsResponse:
    out: DescribeExportConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "exportsInfo" in data:
        import aws_sdk_application_discovery_service.types.exports_info

        out["exports_info"] = (
            aws_sdk_application_discovery_service.types.exports_info.deserialize_aws_json_1_1(
                data["exportsInfo"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out

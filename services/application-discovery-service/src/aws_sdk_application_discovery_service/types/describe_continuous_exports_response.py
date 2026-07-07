"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#DescribeContinuousExportsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.continuous_export_descriptions
    import aws_sdk_application_discovery_service.types.next_token


class DescribeContinuousExportsResponse(TypedDict, closed=True):
    descriptions: NotRequired[
        "aws_sdk_application_discovery_service.types.continuous_export_descriptions.ContinuousExportDescriptions"
    ]
    """<p>A list of continuous export descriptions.</p>"""
    next_token: NotRequired[
        "aws_sdk_application_discovery_service.types.next_token.NextToken"
    ]
    """<p>The token from the previous call to <code>DescribeExportTasks</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeContinuousExportsResponse) -> dict:
    out: dict = {}
    if "descriptions" in value:
        import aws_sdk_application_discovery_service.types.continuous_export_descriptions

        out["descriptions"] = (
            aws_sdk_application_discovery_service.types.continuous_export_descriptions.serialize_aws_json_1_1(
                value["descriptions"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeContinuousExportsResponse:
    out: DescribeContinuousExportsResponse = {}  # type: ignore[typeddict-item]
    if "descriptions" in data:
        import aws_sdk_application_discovery_service.types.continuous_export_descriptions

        out["descriptions"] = (
            aws_sdk_application_discovery_service.types.continuous_export_descriptions.deserialize_aws_json_1_1(
                data["descriptions"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out

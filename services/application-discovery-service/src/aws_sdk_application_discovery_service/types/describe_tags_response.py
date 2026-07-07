"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#DescribeTagsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.configuration_tag_set
    import aws_sdk_application_discovery_service.types.next_token


class DescribeTagsResponse(TypedDict, closed=True):
    tags: NotRequired[
        "aws_sdk_application_discovery_service.types.configuration_tag_set.ConfigurationTagSet"
    ]
    """<p>Depending on the input, this is a list of configuration items tagged with a specific tag, or a list of tags for a specific configuration item.</p>"""
    next_token: NotRequired[
        "aws_sdk_application_discovery_service.types.next_token.NextToken"
    ]
    """<p>The call returns a token. Use this token to get the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTagsResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_application_discovery_service.types.configuration_tag_set

        out["tags"] = (
            aws_sdk_application_discovery_service.types.configuration_tag_set.serialize_aws_json_1_1(
                value["tags"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTagsResponse:
    out: DescribeTagsResponse = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_application_discovery_service.types.configuration_tag_set

        out["tags"] = (
            aws_sdk_application_discovery_service.types.configuration_tag_set.deserialize_aws_json_1_1(
                data["tags"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out

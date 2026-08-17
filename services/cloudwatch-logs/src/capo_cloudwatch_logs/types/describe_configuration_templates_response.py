"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeConfigurationTemplatesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.configuration_templates
    import capo_cloudwatch_logs.types.next_token


class DescribeConfigurationTemplatesResponse(TypedDict, closed=True):
    configuration_templates: NotRequired[
        "capo_cloudwatch_logs.types.configuration_templates.ConfigurationTemplates"
    ]
    """<p>An array of objects, where each object describes one configuration template that matches the filters that you specified in the request.</p>"""
    next_token: NotRequired["capo_cloudwatch_logs.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConfigurationTemplatesResponse) -> dict:
    out: dict = {}
    if "configuration_templates" in value:
        import capo_cloudwatch_logs.types.configuration_templates

        out["configurationTemplates"] = (
            capo_cloudwatch_logs.types.configuration_templates.serialize_aws_json_1_1(
                value["configuration_templates"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConfigurationTemplatesResponse:
    out: DescribeConfigurationTemplatesResponse = {}  # type: ignore[typeddict-item]
    if data.get("configurationTemplates") is not None:
        import capo_cloudwatch_logs.types.configuration_templates

        out["configuration_templates"] = (
            capo_cloudwatch_logs.types.configuration_templates.deserialize_aws_json_1_1(
                data["configurationTemplates"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out

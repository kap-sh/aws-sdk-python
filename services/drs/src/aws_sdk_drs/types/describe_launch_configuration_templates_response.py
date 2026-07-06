"""Generated from Smithy shape ``com.amazonaws.drs#DescribeLaunchConfigurationTemplatesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_drs.types.launch_configuration_templates
    import aws_sdk_drs.types.pagination_token


class DescribeLaunchConfigurationTemplatesResponse(TypedDict, closed=True):
    items: NotRequired[
        "aws_sdk_drs.types.launch_configuration_templates.LaunchConfigurationTemplates"
    ]
    """<p>List of items returned by DescribeLaunchConfigurationTemplates.</p>"""
    next_token: NotRequired["aws_sdk_drs.types.pagination_token.PaginationToken"]
    """<p>The token of the next Launch Configuration Template to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeLaunchConfigurationTemplatesResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_drs.types.launch_configuration_templates

        out["items"] = aws_sdk_drs.types.launch_configuration_templates.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeLaunchConfigurationTemplatesResponse:
    out: DescribeLaunchConfigurationTemplatesResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_drs.types.launch_configuration_templates

        out["items"] = (
            aws_sdk_drs.types.launch_configuration_templates.deserialize_json(
                data["items"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out

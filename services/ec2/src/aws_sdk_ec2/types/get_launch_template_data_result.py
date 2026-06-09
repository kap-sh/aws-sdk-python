"""Generated from Smithy shape ``com.amazonaws.ec2#GetLaunchTemplateDataResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.response_launch_template_data


class GetLaunchTemplateDataResult(TypedDict):
    launch_template_data: NotRequired[
        "aws_sdk_ec2.types.response_launch_template_data.ResponseLaunchTemplateData"
    ]
    """<p>The instance data.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetLaunchTemplateDataResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "launch_template_data" in value:
        import aws_sdk_ec2.types.response_launch_template_data

        aws_sdk_ec2.types.response_launch_template_data.serialize_ec2_query(
            value["launch_template_data"], pairs, f"{prefix}.LaunchTemplateData"
        )


def deserialize_ec2_query(el: Element) -> GetLaunchTemplateDataResult:
    out: GetLaunchTemplateDataResult = {}  # type: ignore[typeddict-item]
    child_launch_template_data = el.find("LaunchTemplateData")
    if child_launch_template_data is not None:
        import aws_sdk_ec2.types.response_launch_template_data

        out["launch_template_data"] = (
            aws_sdk_ec2.types.response_launch_template_data.deserialize_ec2_query(
                child_launch_template_data
            )
        )
    return out

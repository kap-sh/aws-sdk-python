"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeLaunchTemplatesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.launch_template_set
    import aws_sdk_ec2.types.string


class DescribeLaunchTemplatesResult(TypedDict, closed=True):
    launch_templates: NotRequired[
        "aws_sdk_ec2.types.launch_template_set.LaunchTemplateSet"
    ]
    """<p>Information about the launch templates.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeLaunchTemplatesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "launch_templates" in value:
        import aws_sdk_ec2.types.launch_template_set

        aws_sdk_ec2.types.launch_template_set.serialize_ec2_query(
            value["launch_templates"], pairs, f"{prefix}.LaunchTemplates"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeLaunchTemplatesResult:
    out: DescribeLaunchTemplatesResult = {}  # type: ignore[typeddict-item]
    if el.find("LaunchTemplates") is not None:
        import aws_sdk_ec2.types.launch_template_set

        out["launch_templates"] = (
            aws_sdk_ec2.types.launch_template_set.deserialize_ec2_query(
                el, "LaunchTemplates"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out

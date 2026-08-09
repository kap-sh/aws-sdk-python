"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeLaunchTemplatesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.launch_template_set
    import capo_ec2.types.string


class DescribeLaunchTemplatesResult(TypedDict, closed=True):
    launch_templates: NotRequired[
        "capo_ec2.types.launch_template_set.LaunchTemplateSet"
    ]
    """<p>Information about the launch templates.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeLaunchTemplatesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "launch_templates" in value:
        import capo_ec2.types.launch_template_set

        capo_ec2.types.launch_template_set.serialize_ec2_query(
            value["launch_templates"], pairs, f"{key_prefix}LaunchTemplates"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeLaunchTemplatesResult:
    out: DescribeLaunchTemplatesResult = {}  # type: ignore[typeddict-item]
    child_launch_templates = el.find("launchTemplates")
    if child_launch_templates is not None:
        import capo_ec2.types.launch_template_set

        out["launch_templates"] = (
            capo_ec2.types.launch_template_set.deserialize_ec2_query(
                child_launch_templates
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out

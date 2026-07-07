"""Generated from Smithy shape ``com.amazonaws.ec2#DeregisterInstanceTagAttributeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.instance_tag_key_set


class DeregisterInstanceTagAttributeRequest(TypedDict, closed=True):
    include_all_tags_of_instance: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to deregister all tag keys in the current Region. Specify <code>false</code> to deregister all tag keys.</p>"""
    instance_tag_keys: NotRequired[
        "aws_sdk_ec2.types.instance_tag_key_set.InstanceTagKeySet"
    ]
    """<p>Information about the tag keys to deregister.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeregisterInstanceTagAttributeRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "include_all_tags_of_instance" in value:
        pairs.append(
            (
                f"{prefix}.IncludeAllTagsOfInstance",
                "true" if value["include_all_tags_of_instance"] else "false",
            )
        )
    if "instance_tag_keys" in value:
        import aws_sdk_ec2.types.instance_tag_key_set

        aws_sdk_ec2.types.instance_tag_key_set.serialize_ec2_query(
            value["instance_tag_keys"], pairs, f"{prefix}.InstanceTagKeys"
        )


def deserialize_ec2_query(el: Element) -> DeregisterInstanceTagAttributeRequest:
    out: DeregisterInstanceTagAttributeRequest = {}  # type: ignore[typeddict-item]
    child_include_all_tags_of_instance = el.find("IncludeAllTagsOfInstance")
    if child_include_all_tags_of_instance is not None:
        out["include_all_tags_of_instance"] = (
            child_include_all_tags_of_instance.text or ""
        ).lower() == "true"
    if el.find("InstanceTagKeys") is not None:
        import aws_sdk_ec2.types.instance_tag_key_set

        out["instance_tag_keys"] = (
            aws_sdk_ec2.types.instance_tag_key_set.deserialize_ec2_query(
                el, "InstanceTagKeys"
            )
        )
    return out

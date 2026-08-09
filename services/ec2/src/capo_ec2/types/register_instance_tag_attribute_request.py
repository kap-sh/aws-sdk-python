"""Generated from Smithy shape ``com.amazonaws.ec2#RegisterInstanceTagAttributeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.instance_tag_key_set


class RegisterInstanceTagAttributeRequest(TypedDict, closed=True):
    include_all_tags_of_instance: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to register all tag keys in the current Region. Specify <code>true</code> to register all tag keys.</p>"""
    instance_tag_keys: NotRequired[
        "capo_ec2.types.instance_tag_key_set.InstanceTagKeySet"
    ]
    """<p>The tag keys to register.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RegisterInstanceTagAttributeRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "include_all_tags_of_instance" in value:
        pairs.append(
            (
                f"{key_prefix}IncludeAllTagsOfInstance",
                "true" if value["include_all_tags_of_instance"] else "false",
            )
        )
    if "instance_tag_keys" in value:
        import capo_ec2.types.instance_tag_key_set

        capo_ec2.types.instance_tag_key_set.serialize_ec2_query(
            value["instance_tag_keys"], pairs, f"{key_prefix}InstanceTagKey"
        )


def deserialize_ec2_query(el: Element) -> RegisterInstanceTagAttributeRequest:
    out: RegisterInstanceTagAttributeRequest = {}  # type: ignore[typeddict-item]
    child_include_all_tags_of_instance = el.find("IncludeAllTagsOfInstance")
    if child_include_all_tags_of_instance is not None:
        out["include_all_tags_of_instance"] = (
            child_include_all_tags_of_instance.text or ""
        ).lower() == "true"
    child_instance_tag_keys = el.find("InstanceTagKey")
    if child_instance_tag_keys is not None:
        import capo_ec2.types.instance_tag_key_set

        out["instance_tag_keys"] = (
            capo_ec2.types.instance_tag_key_set.deserialize_ec2_query(
                child_instance_tag_keys
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.ec2#ResourceStatement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.value_string_list


class ResourceStatement(TypedDict, closed=True):
    resources: NotRequired["capo_ec2.types.value_string_list.ValueStringList"]
    """<p>The resources.</p>"""
    resource_types: NotRequired["capo_ec2.types.value_string_list.ValueStringList"]
    """<p>The resource types.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ResourceStatement, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "resources" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["resources"], pairs, f"{key_prefix}ResourceSet"
        )
    if "resource_types" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["resource_types"], pairs, f"{key_prefix}ResourceTypeSet"
        )


def deserialize_ec2_query(el: Element) -> ResourceStatement:
    out: ResourceStatement = {}  # type: ignore[typeddict-item]
    child_resources = el.find("resourceSet")
    if child_resources is not None:
        import capo_ec2.types.value_string_list

        out["resources"] = capo_ec2.types.value_string_list.deserialize_ec2_query(
            child_resources
        )
    child_resource_types = el.find("resourceTypeSet")
    if child_resource_types is not None:
        import capo_ec2.types.value_string_list

        out["resource_types"] = capo_ec2.types.value_string_list.deserialize_ec2_query(
            child_resource_types
        )
    return out
